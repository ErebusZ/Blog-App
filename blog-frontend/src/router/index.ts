import {
  createRouter,
  createWebHistory,
  RouteLocationNormalized,
  NavigationGuardNext,
} from "vue-router";
import Home from "../views/HomeView.vue";
import Login from "../views/LoginView.vue";
import Register from "../views/RegisterView.vue";
import BlogPostView from "@/views/BlogPostView.vue";
import NotFoundView from "@/views/NotFoundView.vue";
import EditBlogPostView from "@/views/EditBlogPostView.vue";
import { useAuthStore } from "@/stores/auth";

const routes = [
  { path: "/", component: Home, name: "Home" },
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/blog/:id", component: BlogPostView, name: "BlogPost" },
  {
    path: "/edit/:id",
    name: "EditBlogPost",
    component: EditBlogPostView,
    beforeEnter: (
      to: RouteLocationNormalized,
      from: RouteLocationNormalized,
      next: NavigationGuardNext
    ) => {
      const authStore = useAuthStore();
      if (authStore.isAuthenticated) {
        next();
      } else {
        next({ name: "Login" }); // Redirect to the login page
      }
    },
  },
  {
    path: "/create",
    name: "CreateBlogPost",
    component: EditBlogPostView,
    beforeEnter: (
      to: RouteLocationNormalized,
      from: RouteLocationNormalized,
      next: NavigationGuardNext
    ) => {
      const authStore = useAuthStore();
      if (authStore.isAuthenticated) {
        next();
      } else {
        next({ name: "Login" }); // Redirect to the login page
      }
    },
  },
  { path: "/:pathMatch(.*)*", component: NotFoundView, name: "NotFound" },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
