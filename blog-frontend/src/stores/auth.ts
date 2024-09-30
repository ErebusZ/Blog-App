import { defineStore } from "pinia";
import { ref } from "vue";
import { User } from "@/types";

export const useAuthStore = defineStore("auth", () => {
  const user = ref<User | null>(null);
  const isAuthenticated = ref(false);
  const accessToken = ref<string | null>(null);
  const refreshToken = ref<string | null>(null);

  const login = (userData: { user: User; access: string; refresh: string }) => {
    user.value = userData.user;
    accessToken.value = userData.access;
    refreshToken.value = userData.refresh;
    isAuthenticated.value = true;
  };

  const logout = () => {
    user.value = null;
    accessToken.value = null;
    refreshToken.value = null;
    isAuthenticated.value = false;
  };

  return { user, isAuthenticated, accessToken, refreshToken, login, logout };
});
