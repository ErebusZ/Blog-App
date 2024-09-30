import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/HomeView.vue";
import Login from "../views/LoginView.vue";
import Register from "../views/RegisterView.vue";
import NotFoundView from "@/views/NotFoundView.vue";
import BlogPostView from "@/views/BlogPostView.vue";
import EditBlogPostView from "@/views/EditBlogPostView.vue";

const routes = [
  { path: "/", component: Home, name: "Home" },
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/blog/:id", component: BlogPostView, name: "BlogPost" },
  { path: "/edit/:id", component: EditBlogPostView, name: "EditBlogPost" },
  { path: "/create", component: EditBlogPostView, name: "CreateBlogPost" },
  { path: "/:pathMatch(.*)*", component: NotFoundView },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
