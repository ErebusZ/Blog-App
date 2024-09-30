import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/HomeView.vue";
import Login from "../views/LoginView.vue";
import NotFoundView from "@/views/NotFoundView.vue";

const routes = [
  { path: "/", component: Home, name: "Home" },
  { path: "/login", component: Login },
  { path: "/:pathMatch(.*)*", component: NotFoundView },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
