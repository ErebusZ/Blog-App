import { createRouter, createWebHistory } from 'vue-router';
import type {RouteRecordRaw } from 'vue-router';
import Home from '@/views/HomeView.vue';
import Register from '@/views/RegisterView.vue';
import Login from '@/views/LoginView.vue';
import BlogPost from '@/views/BlogPostView.vue';
import CreateEditPost from '@/views/CreateEditPostView.vue';


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


export default router;