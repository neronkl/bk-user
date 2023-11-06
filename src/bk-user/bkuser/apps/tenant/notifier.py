# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-用户管理(Bk-User) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import logging
from typing import Dict, List, Optional

from django.template import Context, Template
from django.utils.translation import gettext_lazy as _
from pydantic import BaseModel, model_validator

from bkuser.apps.tenant.constants import NotificationMethod, NotificationScene
from bkuser.apps.tenant.models import TenantUser, TenantUserValidityPeriodConfig
from bkuser.component import cmsi

logger = logging.getLogger(__name__)


class NotificationTemplate(BaseModel):
    """通知模板"""

    # 通知方式 如短信，邮件
    method: NotificationMethod
    # 通知场景 如将过期，已过期
    scene: NotificationScene
    # 模板标题
    title: Optional[str] = None
    # 模板发送方
    sender: str
    # 模板内容（text）格式
    content: str
    # 模板内容（html）格式
    content_html: str

    @model_validator(mode="after")
    def validate_attrs(self) -> "NotificationTemplate":
        if self.method == NotificationMethod.EMAIL and not self.title:
            raise ValueError(_("邮件通知模板需要提供标题"))

        return self


class ValidityPeriodNotificationTmplContextGenerator:
    """生成通知模板使用的上下文"""

    def __init__(self, user: TenantUser, scene: NotificationScene):
        self.user = user
        self.scene = scene

    def gen(self) -> Dict[str, str]:
        """生成通知模板使用的上下文

        注：为保证模板渲染准确性，value 值类型需为 str
        """
        if self.scene == NotificationScene.TENANT_USER_EXPIRING:
            return self._gen_tenant_user_expiring_ctx()
        if self.scene == NotificationScene.TENANT_USER_EXPIRED:
            return self._gen_tenant_user_expired_ctx()
        return self._gen_base_ctx()

    def _gen_base_ctx(self) -> Dict[str, str]:
        """获取基础信息"""
        return {"username": self.user.data_source_user.username}

    def _gen_tenant_user_expiring_ctx(self) -> Dict[str, str]:
        """账号有效期-临期通知渲染参数"""
        # FIXME (su) 提供修改密码的 URL（settings.BK_USER_URL + xxxx）
        return {
            "expired_at": self.user.account_expired_at_display,
            **self._gen_base_ctx(),
        }

    def _gen_tenant_user_expired_ctx(self) -> Dict[str, str]:
        """账号有效期-过期通知渲染参数"""
        return self._gen_base_ctx()


class TenantUserValidityPeriodNotifier:
    """租户用户用户通知器，支持批量像用户发送某类信息"""

    templates: List[NotificationTemplate] = []

    def __init__(self, tenant_id: str, scene: NotificationScene):
        self.tenant_id = tenant_id
        self.scene = scene

        self.templates = self._get_templates_with_scene(scene)

    def send(self, users: List[TenantUser]) -> None:
        """根据配置，发送对应的通知信息"""
        try:
            for u in users:
                self._send_notifications(u)
        # TODO (su) 细化异常处理
        except Exception:
            logger.exception("send notification failed")

    def _get_templates_with_scene(self, scene: NotificationScene) -> List[NotificationTemplate]:
        """根据场景以及插件配置中设置的通知方式，获取需要发送通知的模板"""

        if scene not in [NotificationScene.TENANT_USER_EXPIRED, NotificationScene.TENANT_USER_EXPIRING]:
            raise ValueError(_("通知场景 {} 未被支持".format(scene)))

        # 获取通知配置
        validity_period_config = TenantUserValidityPeriodConfig.objects.get(tenant_id=self.tenant_id)
        templates = validity_period_config.notification_templates
        enabled_methods = validity_period_config.enabled_notification_methods

        # 返回场景匹配，且被声明启用的模板列表
        return [
            NotificationTemplate(**tmpl)
            for tmpl in templates
            if validity_period_config["scene"] == scene and tmpl["method"] in enabled_methods
        ]

    def _send_notifications(self, user: TenantUser):
        """根据配置的通知模板，逐个用户发送通知"""
        for tmpl in self.templates:
            if tmpl.method == NotificationMethod.EMAIL:
                self._send_email(user, tmpl)
            elif tmpl.method == NotificationMethod.SMS:
                self._send_sms(user, tmpl)

    def _send_email(self, user: TenantUser, tmpl: NotificationTemplate):
        logger.info(
            "send email to user %s, scene %s, title: %s", user.data_source_user.username, tmpl.scene, tmpl.title
        )
        content = self._render_tmpl(user, tmpl.content_html)
        # FIXME (su) 修改为指定用户名
        # 根据继承与否，获取真实邮箱
        email = user.data_source_user.email if user.is_inherited_email else user.custom_email
        cmsi.send_mail([email], tmpl.sender, tmpl.title, content)  # type: ignore

    def _send_sms(self, user: TenantUser, tmpl: NotificationTemplate):
        logger.info("send sms to user %s, scene %s", user.data_source_user.username, tmpl.scene)
        content = self._render_tmpl(user, tmpl.content)
        # FIXME (su) 修改为指定用户名
        # 根据继承与否，获取真实手机号
        phone = user.data_source_user.phone if user.is_inherited_phone else user.custom_phone
        cmsi.send_sms([phone], content)

    def _render_tmpl(self, user: TenantUser, content: str) -> str:
        ctx = ValidityPeriodNotificationTmplContextGenerator(user=user, scene=self.scene).gen()
        return Template(content).render(Context(ctx))
