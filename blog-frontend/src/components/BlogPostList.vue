<template>
<div class="blog-post-list">
    <div v-for="post in posts" :key="post.id" class="blog-post-item">
    <h2>
        <router-link :to="{ name: 'BlogPost', params: { id: post.id } }">
        {{ post.title }}
        </router-link>
    </h2>
    <p>{{ post.content.substring(0, 200) }}...</p>
    <p>By {{ post.author.username }} on {{ formatDate(post.created_at) }}</p>
    </div>
    <div class="pagination">
    <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
    <span>Page {{ currentPage }} of {{ totalPages }}</span>
    <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>
</div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useBlogStore } from '@/stores/blog';
import { storeToRefs } from 'pinia';

export default defineComponent({
name: 'BlogPostList',
setup() {
    const blogStore = useBlogStore();
    const { posts, currentPage, totalPages } = storeToRefs(blogStore);
    const router = useRouter();
    const route = useRoute();

    const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString();
    };

    const prevPage = () => {
    if (currentPage.value > 1) {
        router.push({ query: { ...route.query, page: currentPage.value - 1 } });
    }
    };

    const nextPage = () => {
    if (currentPage.value < totalPages.value) {
        router.push({ query: { ...route.query, page: currentPage.value + 1 } });
    }
    };

    onMounted(() => {
    const page = Number(route.query.page) || 1;
    const search = route.query.search as string || '';
    blogStore.fetchPosts(page, search);
    });

    return {
    posts,
    currentPage,
    totalPages,
    formatDate,
    prevPage,
    nextPage,
    };
},
});
</script>
  