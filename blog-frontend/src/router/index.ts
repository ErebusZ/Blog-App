import { createRouter, createWebHistory } from 'vue-router';
import type {RouteRecordRaw } from 'vue-router';
import Home from '@/views/HomeView.vue';
import Register from '@/views/RegisterView.vue';
import Login from '@/views/LoginView.vue';
import BlogPost from '@/views/BlogPostView.vue';
import CreateEditPost from '@/views/CreateEditPostView.vue';
import { useAuthStore } from '@/stores/auth';


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/post/:id',
    name: 'BlogPost',
    component: BlogPost,
  },
  {
    path: '/create',
    name: 'CreatePost',
    component: CreateEditPost,
    meta: { requiresAuth: true },
  },
  {
    path: '/edit/:id',
    name: 'EditPost',
    component: CreateEditPost,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes : routes,
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.matched.some(record => record.meta.requiresAuth) && !authStore.isAuthenticated()) {
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;