import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { BlogPost } from '@/types/index';
import { getBlogPosts, getBlogPost, createBlogPost, updateBlogPost, deleteBlogPost } from '@/services/api';

export const useBlogStore = defineStore('blog', () => {
  const posts = ref<BlogPost[]>([]);
  const currentPost = ref<BlogPost | null>(null);
  const totalPages = ref(1);
  const currentPage = ref(1);

  const fetchPosts = async (page = 1, search = '') => {
    try {
      const response = await getBlogPosts(page, search);
      posts.value = response.data.results;
      totalPages.value = Math.ceil(response.data.count / 10);
      currentPage.value = page;
      return posts
    } catch (error) {
        alert('Failed to fetch posts' + error);
    }
  };

  const fetchPost = async (id: number) => {
    try {
      const response = await getBlogPost(id);
      currentPost.value = response.data;
      return currentPost
    } catch (error) {
        alert('Failed to fetch post' + error);
    }
  };

  const createPost = async (data: Partial<BlogPost>) => {
    try {
      const response = await createBlogPost(data);
      posts.value.unshift(response.data);
      return response.data;
    } catch (error) {
        alert('Failed to create post' + error);
    }
  };

  const updatePost = async (id: number, data: Partial<BlogPost>) => {
    try {
      const response = await updateBlogPost(id, data);
      const index = posts.value.findIndex(post => post.id === id);
      if (index !== -1) {
        posts.value[index] = response.data;
      }
      return response.data;
    } catch (error) {
        alert('Failed to update post' + error);
    }
  };

  const deletePost = async (id: number) => {
    try {
      await deleteBlogPost(id);
      posts.value = posts.value.filter(post => post.id !== id);
    } catch (error) {
      alert('Failed to delete post' + error);
    }
  };

  return { posts, currentPost, totalPages, currentPage, fetchPosts, fetchPost, createPost, updatePost, deletePost };
});
