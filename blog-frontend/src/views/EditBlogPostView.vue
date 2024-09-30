<template>
  <div class="p-4 max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold mb-4">
      {{ blog.id ? "Edit" : "Create" }} Blog Post
    </h1>
    <form @submit.prevent="blog.id ? updateBlog() : createBlog()">
      <div class="mb-4">
        <label for="title" class="block text-gray-700">Title</label>
        <input
          type="text"
          id="title"
          v-model="blog.title"
          class="mt-1 block w-full p-2 border rounded"
          required
        />
      </div>
      <div class="mb-4">
        <label for="description" class="block text-gray-700">Description</label>
        <textarea
          id="description"
          v-model="blog.content"
          class="mt-1 block w-full p-2 border rounded"
          required
        ></textarea>
      </div>
      <div class="flex justify-between">
        <button
          type="submit"
          class="px-4 py-2 text-white bg-blue-500 rounded hover:bg-blue-600"
        >
          {{ blog.id ? "Update" : "Create" }} Blog Post
        </button>
        <button
          @click="deleteBlog"
          type="button"
          class="px-4 py-2 text-white bg-red-500 rounded hover:bg-red-600"
          v-if="blog.id"
        >
          Delete
        </button>
      </div>
      <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
    </form>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { BlogPost } from "@/types";
import axiosInstance from "@/axiosInstance";

export default {
  name: "EditBlogPost",
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

    const error = ref("");

    onMounted(async () => {
      const blogId = route.params.id;
      if (blogId) {
        try {
          const response = await axiosInstance.get(
            `${process.env.VUE_APP_API_URL}/articles/blog/${blogId}`
          );
          blog.value = response.data.data;
        } catch (error) {
          console.error("Error fetching blog post:", error);
          router.replace({ name: "NotFound" });
        }
      }
    });

    const updateBlog = async () => {
      try {
        const response = await axiosInstance.patch(
          `${process.env.VUE_APP_API_URL}/articles/blog/${blog.value.id}`,
          {
            title: blog.value.title,
            content: blog.value.content,
          }
        );
        console.log("Blog updated successfully:", response.data);
        await router.push({ name: "BlogPost", params: { id: blog.value.id } });
      } catch (err) {
        console.error("Update failed:", err);
        error.value = "Failed to update the blog post.";
      }
    };

    const createBlog = async () => {
      try {
        const response = await axiosInstance.post(
          `${process.env.VUE_APP_API_URL}/articles/blog/`,
          {
            title: blog.value.title,
            content: blog.value.content,
          }
        );
        console.log("Blog created successfully:", response.data);
        await router.push({
          name: "BlogPost",
          params: { id: response.data.data.id },
        });
      } catch (err) {
        console.error("Creation failed:", err);
        error.value = "Failed to create the blog post.";
      }
    };

    const deleteBlog = async () => {
      if (!blog.value.id) return;
      try {
        await axiosInstance.delete(
          `${process.env.VUE_APP_API_URL}/articles/blog/${blog.value.id}`
        );
        console.log("Blog deleted successfully.");
        await router.push({ name: "Home" });
      } catch (err) {
        console.error("Deletion failed:", err);
        error.value = "Failed to delete the blog post.";
      }
    };

    return { blog, updateBlog, createBlog, deleteBlog, error };
  },
};
</script>

<style scoped></style>
