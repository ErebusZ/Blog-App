import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { Comment } from '@/types/index';
import { getCommentsByPost, createComment, updateComment, deleteComment } from '@/services/api';

export const useCommentStore = defineStore('comment', () => {
  const comments = ref<Comment[]>([]);
  const totalPages = ref(1);
  const currentPage = ref(1);

  const fetchComments = async (postId: number, page = 1) => {
    try {
      const response = await getCommentsByPost(postId, page);
      comments.value = response.data.results;
      totalPages.value = Math.ceil(response.data.count / 10);
      currentPage.value = page;
    } catch (error) {
      alert('Failed to fetch comments:' + error);
    }
  };

  const addComment = async (data: Partial<Comment>) => {
    try {
      const response = await createComment(data);
      comments.value.unshift(response.data);
      return response.data;
    } catch (error) {
      alert('Failed to add comment:' + error);
    }
  };

  const editComment = async (id: number, data: Partial<Comment>) => {
    try {
      const response = await updateComment(id, data);
      const index = comments.value.findIndex(comment => comment.id === id);
      if (index !== -1) {
        comments.value[index] = response.data;
      }
      return response.data;
    } catch (error) {
      alert('Failed to edit comment:' + error);
    }
  };

  const removeComment = async (id: number) => {
    try {
      await deleteComment(id);
      comments.value = comments.value.filter(comment => comment.id !== id);
    } catch (error) {
      alert('Failed to delete comment:' + error);
    }
  };

  return { comments, totalPages, currentPage, fetchComments, addComment, editComment, removeComment };
});

