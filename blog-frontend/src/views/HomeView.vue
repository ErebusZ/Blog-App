<template>
  <div class="flex flex-col items-center justify-center h-auto p-4">
    <div class="w-full max-w-4xl">
      <div
        v-for="blog in paginatedBlogs"
        :key="blog.id"
        class="flex bg-white rounded-lg shadow-md overflow-hidden mb-6"
      >
        <img
          class="w-64 h-40 object-cover"
          :src="blog.image"
          :alt="blog.title"
        />
        <div class="p-4 flex flex-col justify-between w-full">
          <h2 class="text-xl font-semibold mb-1">{{ blog.title }}</h2>
          <p class="text-gray-600 mb-1">by {{ blog.author }}</p>
          <p class="mt-2 text-gray-800">{{ blog.content }}</p>
          <router-link
            :to="{ name: 'BlogPost', params: { id: blog.id } }"
            class="mt-2 text-blue-500 hover:underline"
          >
            Read More
          </router-link>
        </div>
      </div>
      <Pagination
        :currentPage="currentPage"
        :totalPages="totalPages"
        @update:currentPage="currentPage = $event"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { computed, ref } from "vue";
import Pagination from "@/components/Pagination.vue";

export default {
  name: "HomeView",
  components: {
    Pagination,
  },
  setup() {
    const blogs = ref([
      {
        id: 1,
        title: "First Blog Post",
        author: "Author One",
        content: "This is a brief content of the first blog post.",
        image: "https://via.placeholder.com/400x250",
      },
      {
        id: 2,
        title: "Second Blog Post",
        author: "Author Two",
        content: "This is a brief content of the second blog post.",
        image: "https://via.placeholder.com/400x250",
      },
      {
        id: 3,
        title: "Third Blog Post",
        author: "Author Three",
        content: "This is a brief content of the third blog post.",
        image: "https://via.placeholder.com/400x250",
      },
      {
        id: 4,
        title: "Fourth Blog Post",
        author: "Author Four",
        content: "This is a brief content of the fourth blog post.",
        image: "https://via.placeholder.com/400x250",
      },
      {
        id: 5,
        title: "Fifth Blog Post",
        author: "Author Five",
        content: "This is a brief content of the fifth blog post.",
        image: "https://via.placeholder.com/400x250",
      },
    ]);

    const itemsPerPage = 2;
    const currentPage = ref(1);

    const totalPages = computed(() => {
      return Math.ceil(blogs.value.length / itemsPerPage);
    });

    const paginatedBlogs = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      return blogs.value.slice(start, end);
    });

    return { blogs, currentPage, totalPages, paginatedBlogs };
  },
};
</script>

<style scoped></style>
