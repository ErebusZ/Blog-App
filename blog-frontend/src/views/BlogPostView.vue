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
      :src="blog.image || 'https://placehold.co/400x250'"
      :alt="blog.title"
    />
    <h1 class="text-3xl font-bold mb-2">{{ blog.title }}</h1>
    <p class="text-gray-600 mb-4">by {{ blog.author }}</p>
    <p class="text-gray-800">{{ blog.content }}</p>
    <Comments v-if="blogLoaded" :blogId="blog.id" />
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { BlogPost } from "@/types";
import axiosInstance from "@/axiosInstance";
import Comments from "@/components/Comments.vue";
import axios from "axios";

export default {
  name: "BlogPost",
  components: { Comments },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const authStore = useAuthStore();

    const blog = ref<BlogPost>({
      id: 0,
      title: "",
      content: "",
      image: "",
      userId: 0,
    });

    const isOwner = ref(false);
    const blogLoaded = ref(false);

    onMounted(async () => {
      const blogId = route.params.id;

      try {
        const response = await axios.get(
          `${process.env.VUE_APP_API_URL}/articles/blog/${blogId}`
        );

        blog.value = response.data.data;
        isOwner.value = !!(
          authStore.user && authStore.user.id === blog.value.userId
        );

        blogLoaded.value = true;
      } catch (error) {
        console.error("Error fetching blog post:", error);
        await router.replace({ name: "NotFound" });
      }
    });

    const deleteBlog = async () => {
      if (!blog.value.id) return;
      const blogId = route.params.id;
      try {
        await axiosInstance.delete(
          `${process.env.VUE_APP_API_URL}/articles/blog/${blogId}`
        );
        console.log("Blog deleted successfully.");
        await router.push({ name: "Home" });
      } catch (err) {
        console.error("Deletion failed:", err);
      }
    };

    return { blog, isOwner, deleteBlog, blogLoaded };
  },
};
</script>

<style scoped></style>
