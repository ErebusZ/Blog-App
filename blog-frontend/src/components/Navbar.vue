<template>
  <nav class="bg-blue-500 p-4 flex justify-between items-center">
    <div>
      <router-link to="/" class="text-white hover:underline">Home</router-link>
    </div>
    <div class="flex items-center space-x-4">
      <div class="relative">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search..."
          class="transition-all duration-300 border border-transparent bg-transparent text-white focus:bg-white focus:text-black focus:border-white focus:w-40 w-20 py-1 pl-2 rounded outline-none placeholder-transparent focus:placeholder-black"
          @focus="handleFocus"
          @blur="handleBlur"
          @keyup.enter="search"
        />
      </div>
      <template v-if="!isAuthenticated">
        <router-link to="/login" class="text-white hover:underline">Login</router-link>
        <router-link to="/register" class="text-white hover:underline">Register</router-link>
      </template>
      <template v-else>
        <button @click="logout" class="text-white hover:underline">Logout</button>
      </template>
    </div>
  </nav>
</template>

<script lang="ts">
import { computed, ref } from "vue";
import { useRouter } from 'vue-router';
import { useAuthStore } from "@/stores/auth";

export default {
  name: "NavbarComponent",
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    const searchQuery = ref('');

    const handleFocus = (event: FocusEvent) => {
      (event.target as HTMLInputElement).placeholder = "Search...";
    };

    const handleBlur = (event: FocusEvent) => {
      if (!(event.target as HTMLInputElement).value) {
        (event.target as HTMLInputElement).placeholder = "Search...";
      }
    };

    const search = () => {
      router.push({ 
        query: { 
          ...router.currentRoute.value.query, 
          search: searchQuery.value, 
          page: 1 
        } 
      });
    };

    const logout = () => {
      authStore.logout();
    };

    const isAuthenticated = computed(() => authStore.isAuthenticated);

    return {
      handleFocus,
      handleBlur,
      logout,
      isAuthenticated,
      searchQuery,
      search
    };
  },
};
</script>

<style scoped>
input {
  transition: width 0.3s ease;
  border: 1px solid white;
}
input:not(:focus) {
  background-color: transparent;
  color: white;
}
input::placeholder {
  color: white;
}
input:focus {
  border-color: white;
}
</style>