import { defineStore } from "pinia";
import { ref } from "vue";
import { User } from "@/types";

export const useAuthStore = defineStore("auth", () => {
  const user = ref<User | null>(null);
  const isAuthenticated = ref(false);
  const accessToken = ref<string | null>(null);
  const refreshToken = ref<string | null>(null);

  const loadState = () => {
    const savedUser = localStorage.getItem("user");
    const savedAccessToken = localStorage.getItem("accessToken");
    const savedRefreshToken = localStorage.getItem("refreshToken");

    if (savedUser) {
      user.value = JSON.parse(savedUser);
      isAuthenticated.value = true;
    }
    accessToken.value = savedAccessToken;
    refreshToken.value = savedRefreshToken;
  };

  const login = (userData: { user: User; access: string; refresh: string }) => {
    user.value = userData.user;
    accessToken.value = userData.access;
    refreshToken.value = userData.refresh;
    isAuthenticated.value = true;

    localStorage.setItem("user", JSON.stringify(userData.user));
    localStorage.setItem("accessToken", userData.access);
    localStorage.setItem("refreshToken", userData.refresh);
  };

  const logout = () => {
    user.value = null;
    accessToken.value = null;
    refreshToken.value = null;
    isAuthenticated.value = false;

    localStorage.removeItem("user");
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
  };

  loadState();

  return { user, isAuthenticated, accessToken, refreshToken, login, logout };
});
