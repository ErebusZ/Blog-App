<template>
    <div class="login">
      <h2>Login</h2>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="username">Username:</label>
          <input v-model="username" id="username" type="text" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input v-model="password" id="password" type="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
      <p v-if="error">{{ error }}</p>
      <p>Don't have an account? <router-link to="/register">Register here</router-link></p>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { useAuthStore } from '@/stores/auth';
  
  export default defineComponent({
    name: 'Login',
    setup() {
      const router = useRouter();
      const authStore = useAuthStore();
  
      const username = ref('');
      const password = ref('');
      const error = ref('');
  
      const handleSubmit = async () => {
        try {
          const success = await authStore.loginUser(username.value, password.value);
          if (success) {
            router.push('/');
          } else {
            error.value = 'Login failed. Please check your credentials and try again.';
          }
        } catch (e) {
          error.value = 'An error occurred during login. Please try again later.';
        }
      };
  
      return {
        username,
        password,
        error,
        handleSubmit,
      };
    },
  });
  </script>