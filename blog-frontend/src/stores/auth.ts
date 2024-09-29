import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { User } from '@/types/index';
import { login, register } from '@/services/api';
import * as jwt_decode from 'jwt-decode';


export const useAuthStore = defineStore('auth', () => {

  const registerUser = async (username: string, email: string, password: string, firstName: string, lastName: string) => {
    try {
      await register(username, email, password, firstName, lastName);
      return true;
    } catch (error) {
      alert('Registration failed' + error);
      return false;
    }
  };

  return { registerUser };
});
