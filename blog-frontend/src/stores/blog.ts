import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { BlogPost } from '@/types/index';
import { getBlogPosts } from '@/services/api';

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



  return { posts, currentPost, totalPages, currentPage, fetchPosts };
});
