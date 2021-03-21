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
    path: '/authorization',
    name: 'Authorization',
    component: () => import('../components/market/MarketAuthorization.vue'),
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
