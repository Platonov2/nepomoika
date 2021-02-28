import VueRouter, { RouteConfig } from 'vue-router'

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../components/Home.vue'),
  },
  {
    path: '/addCategory',
    name: 'AddCategory',
    component: () => import('../components/AddCategory.vue'),
  },
  {
    path: '/addProduct',
    name: 'AddProduct',
    component: () => import('../components/AddProduct.vue'),
  },
]

const router = new VueRouter({
  routes,
})

export default router;
