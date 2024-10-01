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

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      if (authStore.refreshToken) {
        try {
          const newTokens = await refreshToken(authStore.refreshToken);
          console.log(newTokens);
          authStore.accessToken = newTokens.access;

          originalRequest.headers.Authorization = `Bearer ${newTokens.access}`;
          return axiosInstance(originalRequest);
        } catch (err) {
          console.error("Token refresh failed:", err);
          return Promise.reject(err);
        }
      } else {
        return Promise.reject(error);
      }
    }
    return Promise.reject(error);
  }
);

const refreshToken = async (refreshToken: string) => {
  const response = await axios.post(
    `${process.env.VUE_APP_API_URL}/user_portal/refresh/`,
    {
      refresh: refreshToken,
    }
  );
  return response.data; // Ensure this matches your actual API response structure
};

export default axiosInstance;
