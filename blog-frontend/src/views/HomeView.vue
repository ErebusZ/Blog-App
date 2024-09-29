<template>
  <div class="home">
    <h1>Blog Posts</h1>
    <SearchBar />
    <BlogPostList />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import BlogPostList from '@/components/BlogPostList.vue';
import SearchBar from '@/components/SearchBar.vue';

export default defineComponent({
  name: 'Home',
  components: {
    BlogPostList,
    SearchBar,
  },
});
</script>