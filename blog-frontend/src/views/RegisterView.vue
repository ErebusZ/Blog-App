<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <h1 class="text-3xl font-bold mb-4">Register Page</h1>
    <form
      @submit.prevent="registerUser"
      class="bg-white p-6 rounded shadow-md w-80"
    >
      <input
        type="text"
        v-model="firstName"
        placeholder="First Name"
        required
        class="border p-2 mb-4 w-full"
      />
      <input
        type="text"
        v-model="lastName"
        placeholder="Last Name"
        required
        class="border p-2 mb-4 w-full"
      />
      <input
        type="email"
        v-model="email"
        placeholder="Email"
        required
        class="border p-2 mb-4 w-full"
      />
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
        Register
      </button>
      <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
    </form>
  </div>
</template>

<script lang="ts">
import { ref } from "vue";
import axios, { AxiosError } from "axios";

export default {
  name: "RegisterView",
  setup() {
    const firstName = ref("");
    const lastName = ref("");
    const email = ref("");
    const username = ref("");
    const password = ref("");
    const error = ref("");

    const registerUser = async () => {
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_API_URL}/user_portal/signup/`,
          {
            first_name: firstName.value,
            last_name: lastName.value,
            email: email.value,
            username: username.value,
            password: password.value,
          }
        );

        console.log("Registration successful:", response.data);
      } catch (err) {
        const errorResponse = err as AxiosError;

        if (errorResponse.response && errorResponse.response.data) {
          error.value =
            (errorResponse.response.data as any).error ||
            "Registration failed. Please check your input.";
        } else {
          error.value = "Registration failed. Please check your input.";
        }

        console.error(errorResponse);
      }
    };

    return {
      firstName,
      lastName,
      email,
      username,
      password,
      registerUser,
      error,
    };
  },
};
</script>

<style scoped></style>
