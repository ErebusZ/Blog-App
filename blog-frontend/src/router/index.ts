import { createRouter, createWebHistory } from 'vue-router';
import type {RouteRecordRaw } from 'vue-router';
import Home from '@/views/HomeView.vue';


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  }
];

const router = createRouter({
  history: createWebHistory("/"),
  routes : routes,
});

export default router;