import Vue from 'vue';
import Router from 'vue-router';

import RouterComponent from './components/RouterComponent.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import(/* webpackChunkName: "start" */ './views/main/Start.vue'),
      children: [
        {
          path: 'login',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "login" */ './views/Login.vue'),
        },
        {
          path: 'recover-password',
          component: () => import(/* webpackChunkName: "recover-password" */ './views/PasswordRecovery.vue'),
        },
        {
          path: 'reset-password',
          component: () => import(/* webpackChunkName: "reset-password" */ './views/ResetPassword.vue'),
        },
        {
          path: 'main',
          component: () => import(/* webpackChunkName: "main" */ './views/main/Main.vue'),
          children: [
            {
              path: 'dashboard',
              component: () => import(/* webpackChunkName: "main-dashboard" */ './views/main/Dashboard.vue'),
            },
            {
              path: 'profile',
              component: RouterComponent,
              redirect: 'profile/view',
              children: [
                {
                  path: 'view',
                  component: () => import(
                    /* webpackChunkName: "main-profile" */ './views/main/profile/UserProfile.vue'),
                },
                {
                  path: 'edit',
                  component: () => import(
                    /* webpackChunkName: "main-profile-edit" */ './views/main/profile/UserProfileEdit.vue'),
                },
                {
                  path: 'password',
                  component: () => import(
                    /* webpackChunkName: "main-profile-password" */ './views/main/profile/UserProfileEditPassword.vue'),
                },
              ],
            },
            {
              path: 'admin',
              component: () => import(/* webpackChunkName: "main-admin" */ './views/main/admin/Admin.vue'),
              redirect: 'admin/users/all',
              children: [
                {
                  path: 'users',
                  redirect: 'users/all',
                },
                {
                  path: 'users/all',
                  component: () => import(
                    /* webpackChunkName: "main-admin-users" */ './views/main/admin/AdminUsers.vue'),
                },
                {
                  path: 'users/edit/:id',
                  name: 'main-admin-users-edit',
                  component: () => import(
                    /* webpackChunkName: "main-admin-users-edit" */ './views/main/admin/EditUser.vue'),
                },
                {
                  path: 'users/create',
                  name: 'main-admin-users-create',
                  component: () => import(
                    /* webpackChunkName: "main-admin-users-create" */ './views/main/admin/CreateUser.vue'),
                },
              ],
            },
            {
              path: 'admin',
              component: () => import(/* webpackChunkName: "main-admin" */ './views/main/admin/Admin.vue'),
              redirect: 'admin/groups/all',
              children: [
                {
                  path: 'groups',
                  redirect: 'groups/all',
                },
                {
                  path: 'groups/all',
                  component: () => import(
                    /* webpackChunkName: "main-admin-groups" */ './views/main/admin/AdminGroups.vue'),
                },
                {
                  path: 'groups/create',
                  name: 'main-admin-groups-create',
                  component: () => import(
                    /* webpackChunkName: "main-admin-users-create" */ './views/main/admin/CreateGroup.vue'),
                },
                {
                  path: 'groups/edit/:id',
                  name: 'main-admin-groups-edit',
                  component: () => import(
                    /* webpackChunkName: "main-admin-groups-edit" */ './views/main/admin/EditGroup.vue'),
                },
              ],
            },
            {
              path: 'admin',
              component: () => import(/* webpackChunkName: "main-admin" */ './views/main/admin/Admin.vue'),
              redirect: 'admin/roles/all',
              children: [
                {
                  path: 'roles',
                  redirect: 'roles/all',
                },
                {
                  path: 'roles/all',
                  component: () => import(
                    /* webpackChunkName: "main-admin-roles" */ './views/main/admin/AdminRoles.vue'),
                },
                {
                  path: 'roles/create',
                  name: 'main-admin-roles-create',
                  component: () => import(
                    /* webpackChunkName: "main-admin-roles-create" */ './views/main/admin/CreateRole.vue'),
                },
                {
                  path: 'groups/edit/:id',
                  name: 'main-admin-roles-edit',
                  component: () => import(
                    /* webpackChunkName: "main-admin-roles-edit" */ './views/main/admin/EditRole.vue'),
                },
              ],
            },
            {
              path: 'admin',
              component: () => import(/* webpackChunkName: "main-admin" */ './views/main/admin/Admin.vue'),
              redirect: 'admin/apps/all',
              children: [
                {
                  path: 'apps',
                  redirect: 'apps/all',
                },
                {
                  path: 'apps/all',
                  component: () => import(
                    /* webpackChunkName: "main-admin-apps" */ './views/main/admin/AdminApps.vue'),
                },
                {
                  path: 'apps/create',
                  name: 'main-admin-apps-create',
                  component: () => import(
                    /* webpackChunkName: "main-admin-apps-create" */ './views/main/admin/CreateApp.vue'),
                },
                {
                  path: 'apps/edit/:id',
                  name: 'main-admin-apps-edit',
                  component: () => import(
                    /* webpackChunkName: "main-admin-apps-edit" */ './views/main/admin/EditApp.vue'),
                },
              ],
            },
          ],
        },
      ],
    },
    {
      path: '/*', redirect: '/',
    },
  ],
});
