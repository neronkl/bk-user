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
import re

from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


TENANT_ID_REGEX = r"^(\d|[a-zA-Z])([a-zA-Z0-9._-]){0,31}"


def validate_id(value):
    if not re.fullmatch(re.compile(TENANT_ID_REGEX), value):
        raise ValidationError(_("{} 不符合 username 命名规范: 由1-32位字母、数字、下划线(_)、点(.)、减号(-)字符组成，以字母或数字开头").format(value))
