<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <h1 class="text-3xl font-bold mb-4">Login Page</h1>
    <form
      @submit.prevent="loginUser"
      class="bg-white p-6 rounded shadow-md w-80"
    >
      <input
        type="text"
        v-model="username"
        placeholder="Username"
        required
        class="border p-2 mb-4 w-full"
      />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        required
        class="border p-2 mb-4 w-full"
      />
      <button type="submit" class="bg-blue-500 text-white p-2 w-full rounded">
        Login
      </button>
      <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
    </form>
  </div>
</template>

<script lang="ts">
import { ref } from "vue";
import axios from "axios";
import { useAuthStore } from "@/stores/auth";
import { User } from "@/types";
import { useRouter } from "vue-router";

export default {
  name: "LoginView",
  setup() {
    const username = ref("");
    const password = ref("");
    const error = ref("");
    const authStore = useAuthStore();
    const router = useRouter();

    const loginUser = async () => {
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_API_URL}/user_portal/login/`,
          {
            username: username.value,
            password: password.value,
          }
        );

        const { access, refresh, userId } = response.data.data;
        const user: User = {
          id: userId,
          name: username.value,
        };

        authStore.login({ user, access, refresh });
        console.log("Login successful:", response.data);

        await router.push({ name: "Home" });
      } catch (err) {
        error.value = "Login failed. Please check your credentials.";
        console.error(err);
      }
    };

    return { username, password, loginUser, error };
  },
};
</script>

<style scoped></style>
