<template>
  <div class="p-4 max-w-2xl mx-auto">
    <div v-if="isOwner" class="flex justify-between mb-4">
      <router-link
        :to="{ name: 'EditBlogPost', params: { id: blog.id } }"
        class="px-4 py-2 text-white bg-blue-500 rounded hover:bg-blue-600"
      >
        Edit
      </router-link>
      <button
        @click="deleteBlog"
        class="px-4 py-2 text-white bg-red-500 rounded hover:bg-red-600"
      >
        Delete
      </button>
    </div>
    <img
      class="w-full h-60 object-cover mb-4"
      :src="blog.image"
      :alt="blog.title"
    />
    <h1 class="text-3xl font-bold mb-2">{{ blog.title }}</h1>
    <p class="text-gray-600 mb-4">by {{ blog.author }}</p>
    <p class="text-gray-800">{{ blog.content }}</p>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { BlogPost } from "@/types";

export default {
  name: "BlogPost",
  setup() {
    const route = useRoute();
    const router = useRouter();
    const authStore = useAuthStore();

    const blog = ref<BlogPost>({
      id: 0,
      title: "",
      author: "",
      content: "",
      image: "",
      userId: 0,
    });
    const isOwner = ref(false);

    onMounted(() => {
      const blogId = route.params.id;
      const blogs: BlogPost[] = [
        {
          id: 1,
          title: "First Blog Post",
          author: "Author One",
          content: "content 1",
          image: "https://via.placeholder.com/400x250",
          userId: 1,
        },
        {
          id: 2,
          title: "Second Blog Post",
          author: "Author Two",
          content: "content 2",
          image: "https://via.placeholder.com/400x250",
          userId: 2,
        },
        {
          id: 3,
          title: "Third Blog Post",
          author: "Author Three",
          content: "contetn 3",
          image: "https://via.placeholder.com/400x250",
          userId: 3,
        },
      ];

      const selectedBlog = blogs.find((blog) => blog.id === Number(blogId));

      console.log("Logged-in user:", authStore.user);

      if (selectedBlog) {
        blog.value = selectedBlog;
        isOwner.value = authStore.user?.id === blog.value.userId;
      } else {
        router.replace({ name: "NotFound" });
      }
    });

    const deleteBlog = async () => {
      console.log("Deleting blog post with ID:", blog.value.id);
      await router.push({ name: "Home" });
    };

    return { blog, isOwner, deleteBlog };
  },
};
</script>

<style scoped></style>
