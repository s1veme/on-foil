import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import(/* webpackChunkName: "login" */ '../views/Dashboard.vue'),
    meta: {
      accessTokenExpected: true
    },
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const isTokenExpectedAndExist =
    (to.matched.some((r) => r.meta.accessTokenExpected) &&
      localStorage.getItem('token')) ||
    !to.matched.some((r) => r.meta.accessTokenExpected);
  if (isTokenExpectedAndExist) {
    return next();
  }
    router.push("/");
});

export default router
