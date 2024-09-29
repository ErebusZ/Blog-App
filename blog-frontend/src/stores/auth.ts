import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { User } from '@/types/index';
import { login, register } from '@/services/api';
import * as jwt_decode from 'jwt-decode';


export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null);
  const token = ref<string | null>(null);


  const registerUser = async (username: string, email: string, password: string, firstName: string, lastName: string) => {
    try {
      await register(username, email, password, firstName, lastName);
      return true;
    } catch (error) {
      alert('Registration failed' + error);
      return false;
    }
  };

  const setToken = (newToken: string) => {
    token.value = newToken;
    localStorage.setItem('token', newToken);
    const decoded = jwt_decode.jwtDecode(newToken) as { user_id: number; username: string; email: string };
    user.value = {
      id: decoded.user_id,
      username: decoded.username,
      email: decoded.email,
    };
  };


  const loginUser = async (username: string, password: string) => {
    try {
      const response = await login(username, password);
      setToken(response.data.token);
      return true;
    } catch (error) {
      alert('Login failed' + error);
      return false;
    }
  };

  const clearToken = () => {
    token.value = null;
    user.value = null;
    localStorage.removeItem('token');
  };

  const logout = () => {
    clearToken();
  };

  const isAuthenticated = () => !!token.value;

  return { user, registerUser, loginUser, logout, isAuthenticated };
});
