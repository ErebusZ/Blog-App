<template>
  <div class="flex flex-col items-center justify-center h-auto p-4">
    <template v-if="isAuthenticated">
      <router-link to="/create">
        <button class="bg-blue-500 text-white p-2 w-full rounded">
          Create New Blog
        </button>
      </router-link>
    </template>
    <div class="w-full max-w-4xl" v-if="blogs.length > 0">
      <div
        v-for="blog in paginatedBlogs"
        :key="blog.id"
        class="flex bg-white rounded-lg shadow-md overflow-hidden mb-6"
      >
        <router-link :to="`/blog/${blog.id}`" class="flex w-full">
          <img
            class="w-1/3 h-full object-cover"
            :src="blog.image || 'https://placehold.co/600x400'"
            :alt="blog.title"
          />
          <div class="p-4 flex flex-col justify-between w-2/3">
            <h2 class="text-xl font-semibold mb-0.5">{{ blog.title }}</h2>
            <p class="text-gray-600 mb-1">by {{ blog.author }}</p>
            <p class="mt-1 text-gray-800">
              {{ truncatedContent(blog.content) }}
            </p>
          </div>
        </router-link>
      </div>
      <Pagination
        :currentPage="currentPage"
        :totalPages="totalPages"
        @update:currentPage="currentPage = $event"
      />
    </div>
    <div v-else>
      <p class="text-gray-600">Loading blogs...</p>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, computed, onMounted } from "vue";
import axiosInstance from "@/axiosInstance";
import Pagination from "@/components/Pagination.vue";
import axios from "axios";
import { useAuthStore } from "@/stores/auth";

export default {
  name: "HomeView",
  components: {
    Pagination,
  },
  setup() {
    const blogs = ref([]);
    const itemsPerPage = 5;
    const currentPage = ref(1);
    const error = ref("");
    const isAuthenticated = computed(() => useAuthStore().isAuthenticated);

    const totalPages = computed(() => {
      return Math.ceil(blogs.value.length / itemsPerPage);
    });

    const paginatedBlogs = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      return blogs.value.slice(start, end);
    });

    const fetchBlogs = async () => {
      try {
        const response = await axios.get(
          `${process.env.VUE_APP_API_URL}/articles/blog/`
        );
        blogs.value = response.data.data;
      } catch (err) {
        console.error("Error fetching blogs:", err);
        error.value = "Failed to load blog posts.";
        blogs.value = [];
      }
    };

    onMounted(fetchBlogs);

    const truncatedContent = (content: string): string => {
      const maxLength = 250;
      return content.length > maxLength
        ? content.slice(0, maxLength) + "..."
        : content;
    };

    return {
      blogs,
      currentPage,
      totalPages,
      paginatedBlogs,
      error,
      isAuthenticated,
      truncatedContent,
    };
  },
};
</script>

<style scoped></style>
