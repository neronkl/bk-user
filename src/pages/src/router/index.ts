import { createRouter, createWebHistory } from "vue-router";

export default createRouter({
  history: createWebHistory(window.SITE_URL),
  routes: [
    {
      path: "/",
      name: "organization",
      component: () => import("@/views/organization/index.vue"),
    },
    {
      path: "/tenantry",
      name: "tenantry",
      redirect: {
        name: "tenantInfo",
      },
      meta: {
        navName: "集团概览",
      },
      component: () => import("@/views/tenantry/index.vue"),
      children: [
        {
          path: "info",
          name: "tenantInfo",
          meta: {
            routeParentName: "tenantry",
            navName: "集团概览",
            isMenu: true,
          },
          component: () => import("@/views/tenantry/group-details/index.vue"),
        },
        // {
        //   path: "setting",
        //   name: "globalSetting",
        //   meta: {
        //     routeParentName: "tenantry",
        //     navName: "全局设置",
        //     isMenu: true,
        //   },
        // },
      ],
    },
    {
      path: "/datasource",
      name: "datasource",
      redirect: {
        name: "local",
      },
      meta: {
        navName: "数据源管理",
      },
      component: () => import("@/views/data-source/index.vue"),
      children: [
        {
          path: "",
          name: "",
          meta: {
            routeParentName: "datasource",
            navName: "数据源管理",
            activeMenu: "dataConf",
          },
          component: () => import("@/views/data-source/LocalCompany.vue"),
          children: [
            {
              path: "local",
              name: "local",
              meta: {
                routeParentName: "datasource",
                navName: "数据源管理",
                activeMenu: "dataConf",
              },
              component: () =>
                import("@/views/data-source/LocalDataSource.vue"),
            },
            {
              path: "other",
              name: "other",
              meta: {
                routeParentName: "datasource",
                navName: "数据源管理",
                activeMenu: "dataConf",
              },
              component: () =>
                import("@/views/data-source/OtherDataSource.vue"),
            },
          ],
        },
        {
          path: "local-details/:name/:type",
          name: "dataConfDetails",
          meta: {
            routeParentName: "datasource",
            navName: "数据源详情",
            activeMenu: "dataConf",
          },
          component: () =>
            import("@/views/data-source/local-details/index.vue"),
        },
        {
          path: "new-local/:type",
          name: "newLocal",
          meta: {
            routeParentName: "datasource",
            navName: "新建数据源",
            activeMenu: "dataConf",
          },
          component: () =>
            import("@/views/data-source/new-data/NewLocalData.vue"),
        },
      ],
    },
    {
      path: "/audit",
      name: "audit",
      component: () => import("@/views/audit/index.vue"),
    },
    {
      path: "/setting",
      name: "setting",
      redirect: {
        name: "userFields",
      },
      meta: {
        navName: "用户字段设置",
      },
      component: () => import("@/views/setting/index.vue"),
      children: [
        {
          path: "fields",
          name: "userFields",
          meta: {
            routeParentName: "setting",
            navName: "用户字段设置",
            isMenu: true,
          },
          component: () => import("@/views/setting/FieldSetting.vue"),
        },
        {
          path: "login",
          name: "login",
          meta: {
            routeParentName: "setting",
            navName: "登录设置",
            isMenu: true,
          },
          component: () => import("@/views/setting/LoginSetting.vue"),
        },
      ],
    },
  ],
});
