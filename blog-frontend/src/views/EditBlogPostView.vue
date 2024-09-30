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
        <label for="author" class="block text-gray-700">Author</label>
        <input
          type="text"
          id="author"
          v-model="blog.author"
          class="mt-1 block w-full p-2 border rounded"
          required
        />
      </div>
      <div class="mb-4">
        <label for="content" class="block text-gray-700">content</label>
        <textarea
          id="content"
          v-model="blog.content"
          class="mt-1 block w-full p-2 border rounded"
          required
        ></textarea>
      </div>
      <div class="mb-4">
        <label for="image" class="block text-gray-700">Image URL</label>
        <input
          type="text"
          id="image"
          v-model="blog.image"
          class="mt-1 block w-full p-2 border rounded"
          required
        />
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
    </form>
  </div>
</template>

<script lang="ts">
import { ref, onMounted, computed } from "vue";
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
      author: "",
      content: "",
      image: "",
      userId: 0,
    });

    const isOwner = computed(() => {
      return authStore.user?.id === blog.value.userId;
    });

    onMounted(async () => {
      const blogId = route.params.id;
      if (blogId) {
        const response = await axiosInstance.get(
          `/your_api_endpoint_to_get_blog/${blogId}/`
        );
        blog.value = response.data;
      }
    });

    const updateBlog = async () => {
      try {
        const response = await axiosInstance.put(
          `/your_api_endpoint_to_update/${blog.value.id}/`,
          {
            title: blog.value.title,
            author: blog.value.author,
            content: blog.value.content,
            image: blog.value.image,
          }
        );
        console.log("Blog updated successfully:", response.data);
        await router.push({ name: "BlogPost", params: { id: blog.value.id } });
      } catch (err) {
        console.error("Update failed:", err);
      }
    };

    const createBlog = async () => {
      try {
        const response = await axiosInstance.post(
          "${process.env.VUE_APP_API_URL}/user_portal/login/",
          {
            title: blog.value.title,
            author: blog.value.author,
            content: blog.value.content,
            image: blog.value.image,
            userId: authStore.user?.id,
          }
        );
        console.log("Blog created successfully:", response.data);
        await router.push({
          name: "BlogPost",
          params: { id: response.data.id },
        });
      } catch (err) {
        console.error("Creation failed:", err);
      }
    };

    const deleteBlog = async () => {
      if (!blog.value.id) return;
      try {
        await axiosInstance.delete(
          `/your_api_endpoint_to_delete/${blog.value.id}/`
        );
        console.log("Blog deleted successfully.");
        await router.push({ name: "Home" });
      } catch (err) {
        console.error("Deletion failed:", err);
      }
    };

    return { blog, isOwner, updateBlog, createBlog, deleteBlog };
  },
};
</script>

<style scoped></style>
