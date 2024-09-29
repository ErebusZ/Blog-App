<template>
  <div class="register">
    <h2>Register</h2>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="firstName">Fist Name:</label>
        <input v-model="password" id="firstName" type="text" required />
      </div>
      <div>
        <label for="lastName">Last Name:</label>
        <input v-model="password" id="lastName" type="text" required />
      </div>
      <div>
        <label for="username">Username:</label>
        <input v-model="username" id="username" type="text" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input v-model="email" id="email" type="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <p v-if="error">{{ error }}</p>
    <p>Already have an account? <router-link to="/login">Log in here</router-link></p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

export default defineComponent({
  name: 'Register',
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();

    const firstName = ref('');
    const lastName = ref('');
    const username = ref('');
    const email = ref('');
    const password = ref('');
    const error = ref('');

    const handleSubmit = async () => {
      try {
        const success = await authStore.registerUser(username.value, email.value, password.value, firstName.value, lastName.value);
        if (success) {
          router.push('/');
        } else {
          error.value = 'Registration failed. Please try again.';
        }
      } catch (e) {
        error.value = 'An error occurred during registration.';
      }
    };

    return {
      username,
      email,
      password,
      error,
      handleSubmit,
    };
  },
});
</script>