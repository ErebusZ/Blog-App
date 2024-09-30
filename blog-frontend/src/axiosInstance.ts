import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const axiosInstance = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
});

axiosInstance.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore();
    if (authStore.accessToken) {
      config.headers.Authorization = `Bearer ${authStore.accessToken}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    const authStore = useAuthStore();

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const newTokens = await refreshToken(authStore.refreshToken!);
        authStore.accessToken = newTokens.access;
        authStore.refreshToken = newTokens.refresh;

        originalRequest.headers.Authorization = `Bearer ${newTokens.access}`;
        return axiosInstance(originalRequest);
      } catch (err) {
        console.error("Token refresh failed:", err);
        return Promise.reject(err);
      }
    }
    return Promise.reject(error);
  }
);

const refreshToken = async (refreshToken: string) => {
  const response = await axios.post("/user_portal/refresh/", {
    token: refreshToken,
  });
  return response.data.data;
};

export default axiosInstance;
