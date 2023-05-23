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


from django.urls.conf import path

from . import views

urlpatterns = [
    path(
        "categories/",
        views.RecycleBinCategoryListApi.as_view(),
        name="recycle_bin.category.list",
    ),
    path(
        "categories/check/",
        views.RecycleBinBatchCategoryRevertCheckApi.as_view(),
        name="recycle_bin.category.revert.check",
    ),
    path(
        "categories/revert/",
        views.RecycleBinBatchCategoryRevertApi.as_view(),
        name="recycle_bin.category.revert",
    ),
    path(
        "categories/hard_delete/",
        views.RecycleBinCategoryBatchHardDeleteApi.as_view(),
        name="recycle_bin.category.hard_delete",
    ),
    path(
        "departments/",
        views.RecycleBinDepartmentListApi.as_view(),
        name="recycle_bin.department.list",
    ),
    path(
        "profiles/",
        views.RecycleBinProfileListApi.as_view(),
        name="recycle_bin.profile.list",
    ),
]
