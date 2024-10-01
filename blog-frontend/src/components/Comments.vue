<template>
  <div class="mt-6">
    <h2 class="text-2xl font-bold mb-4">Comments</h2>

    <div
      v-for="comment in comments"
      :key="comment.id"
      class="bg-white border rounded-lg shadow p-4 mb-4 relative"
    >
      <div class="flex justify-between items-start">
        <p class="font-semibold text-gray-800">{{ comment.author }}</p>

        <div v-if="isOwner(comment.user_id)" class="relative">
          <button @click="toggleMenu(comment.id)" class="focus:outline-none">
            <span class="material-icons"
              ><svg
                width="24"
                height="24"
                viewBox="0 0 16 16"
                xmlns="http://www.w3.org/2000/svg"
                fill="#000000"
                class="bi bi-three-dots-vertical"
              >
                <path
                  d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"
                /></svg
            ></span>
          </button>
          <div
            v-if="activeCommentId === comment.id"
            class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg z-10"
          >
            <div class="py-1">
              <button
                @click="editComment(comment)"
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 w-full text-left"
              >
                Edit
              </button>
              <button
                @click="deleteComment(comment.id)"
                class="block px-4 py-2 text-sm text-red-600 hover:bg-gray-100 w-full text-left"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>

      <p class="text-gray-700 mt-2">{{ comment.content }}</p>
    </div>

    <form
      @submit.prevent="addComment"
      class="mt-4 bg-gray-100 p-4 rounded-lg shadow"
    >
      <textarea
        v-model="newComment"
        class="border p-2 w-full rounded-md"
        placeholder="Add a comment..."
        required
      ></textarea>
      <button
        type="submit"
        class="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        Submit Comment
      </button>
    </form>

    <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent, onMounted } from "vue";
import axiosInstance from "@/axiosInstance"; // Import your axios instance
import { useAuthStore } from "@/stores/auth";
import axios from "axios";
import AxiosInstance from "@/axiosInstance"; // Import the auth store

interface Comment {
  id: number;
  content: string;
  user_id: number;
}

export default defineComponent({
  name: "CommentsComponent",
  props: {
    blogId: {
      type: Number,
      required: true,
    },
  },
  setup(props) {
    const authStore = useAuthStore();
    const comments = ref<Comment[]>([]);
    const newComment = ref<string>("");
    const error = ref<string>("");
    const activeCommentId = ref<number | null>(null); // Track the active comment ID for the menu

    // Fetch comments for the specific blog post
    const fetchComments = async () => {
      try {
        const response = await axios.get(
          `${process.env.VUE_APP_COMMENT_API_URL}/comments/post/${props.blogId}`
        );
        console.log(response.data); // Log the response data
        comments.value = response.data; // Adjust according to your response structure
      } catch (err) {
        console.error("Failed to fetch comments:", err);
        error.value = "Failed to load comments.";
      }
    };

    // Use onMounted to ensure fetchComments runs after the component is mounted
    onMounted(() => {
      fetchComments();
    });

    const addComment = async () => {
      if (!newComment.value.trim()) return;
      try {
        const response = await AxiosInstance.post(
          `${process.env.VUE_APP_COMMENT_API_URL}/comment/`,
          {
            content: newComment.value,
            post_id: props.blogId,
          }
        );
        comments.value.push(response.data); // Assuming response.data.data contains the new comment
        newComment.value = ""; // Clear the input field
      } catch (err) {
        console.error("Failed to add comment:", err);
        error.value = "Failed to add comment.";
      }
    };

    const deleteComment = async (commentId: number) => {
      try {
        await axiosInstance.delete(
          `${process.env.VUE_APP_COMMENT_API_URL}/comments/${commentId}`
        );
        comments.value = comments.value.filter(
          (comment) => comment.id !== commentId
        );
      } catch (err) {
        console.error("Failed to delete comment:", err);
        error.value = "Failed to delete comment.";
      }
      activeCommentId.value = null; // Close the menu after action
    };

    const editComment = (comment: Comment) => {
      // Logic to handle editing comments can be added here.
      // You might want to show an input to edit the existing comment.
    };

    const toggleMenu = (commentId: number) => {
      // Toggle the visibility of the menu
      activeCommentId.value =
        activeCommentId.value === commentId ? null : commentId;
    };

    const isOwner = (commentAuthorId: number) => {
      return authStore.user?.id === commentAuthorId; // Check if the logged-in user is the owner of the comment
    };

    fetchComments(); // Fetch comments when the component is mounted

    return {
      comments,
      newComment,
      addComment,
      deleteComment,
      editComment,
      error,
      isOwner,
      toggleMenu,
      activeCommentId,
    };
  },
});
</script>

<style scoped></style>
