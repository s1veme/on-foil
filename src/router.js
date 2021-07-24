import { createRouter, createWebHistory } from 'vue-router'
import store from "@/vuex/store";

const routes = [
    {
        path: '/',
        component: () => import('@/components/v-admin-panel'),
        name: 'admin-panel',
        meta: {
            accessTokenExpected: true
        },
    },
    {
        path: '/login',
        component: () => import('@/components/v-login'),
        name: 'login',
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});


router.beforeEach((to, from, next) => {
  const isTokenExpectedAndExist =
    (to.matched.some((r) => r.meta.accessTokenExpected) &&
      store.state.user.token) ||
    !to.matched.some((r) => r.meta.accessTokenExpected);
  if (isTokenExpectedAndExist) {
    return next();
  }
    router.push("/login");
});

export default router
