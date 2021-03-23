import VueRouter, { RouteConfig } from 'vue-router'

const routes: Array<RouteConfig> = [
  {
    path: '/admin/login',
    name: 'AdminAuthorization',
    component: () => import('../components/admin/AdminAuthorization.vue'),
  },
  {
    path: '/admin',
    name: 'AdminMainPage',
    component: () => import('../components/admin/AdminMainPage.vue'),
  },
  {
    path: '/admin/addCategory',
    name: 'AddCategory',
    component: () => import('../components/AddCategory.vue'),
  },
  {
    path: '/admin/addProduct',
    name: 'AddProduct',
    component: () => import('../components/AddProduct.vue'),
  },
  {
    path: '/authorization',
    name: 'Authorization',
    component: () => import('../components/market/MarketAuthorization.vue'),
  },
  {
    path: '/registration',
    name: 'Registration',
    component: () => import('../components/market/MarketRegistration.vue'),
  },
  {
    path: '/',
    name: 'MarketMainPage',
    component: () => import('../components/market/MarketMainPage.vue'),
  },
]

const router = new VueRouter({
  routes,
})

export default router;
