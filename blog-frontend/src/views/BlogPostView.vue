<template>
<div v-if="currentPost" class="blog-post">
    <h1>{{ currentPost.title }}</h1>
    <p>By {{ currentPost.author.username }} on {{ formatDate(currentPost.created_at) }}</p>
    <div v-html="currentPost.content"></div>
    
    <div v-if="isAuthenticated && currentPost.author.id === user?.id">
    <router-link :to="{ name: 'EditPost', params: { id: currentPost.id } }">Edit Post</router-link>
    <button @click="deletePost">Delete Post</button>
    </div>

    <h2>Comments</h2>
    <div v-if="isAuthenticated">
    <textarea v-model="newComment" placeholder="Write a comment..."></textarea>
    <button @click="addComment">Add Comment</button>
    </div>
    
    <div v-for="comment in comments" :key="comment.id" class="comment">
    <p>{{ comment.content }}</p>
    <p>Created at {{ formatDate(comment.created_at) }} by {{ user?.username }}</p>
    <div v-if="isAuthenticated && comment.author_id === user?.id">
        <button @click="editComment(comment.id, comment)">Edit</button>
        <button @click="deleteComment(comment.id)">Delete</button>
    </div>
    </div>
    
    <div class="pagination">
    <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
    <span>Page {{ currentPage }} of {{ totalPages }}</span>
    <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>
</div>
</template>
  
<script lang="ts">
import { defineComponent, ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useBlogStore } from '@/stores/blog';
import { useCommentStore } from '@/stores/comment';
import { useAuthStore } from '@/stores/auth';
import { storeToRefs } from 'pinia';

export default defineComponent({
name: 'BlogPost',
setup() {
    const route = useRoute();
    const router = useRouter();
    const blogStore = useBlogStore();
    const commentStore = useCommentStore();
    const authStore = useAuthStore();

    const { currentPost } = storeToRefs(blogStore);
    const { comments, currentPage, totalPages } = storeToRefs(commentStore);
    const { user } = storeToRefs(authStore);

    const newComment = ref('');
    const isAuthenticated = computed(() => authStore.isAuthenticated());

    const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString();
    };

    const addComment = async () => {
    if (currentPost.value) {
        await commentStore.addComment({
        content: newComment.value,
        blog_id: currentPost.value.id,
        });
        newComment.value = '';
    }
    };

    const editComment = async (id: number, comment: any) => {
        await commentStore.editComment(id, comment);
    };

    const deleteComment = async (id: number) => {
        await commentStore.removeComment(id);
    };

    const deletePost = async () => {
    if (currentPost.value) {
        await blogStore.deletePost(currentPost.value.id);
        router.push('/');
    }
    };

    const prevPage = () => {
    if (currentPage.value > 1) {
        fetchComments(currentPage.value - 1);
    }
    };

    const nextPage = () => {
    if (currentPage.value < totalPages.value) {
        fetchComments(currentPage.value + 1);
    }
    };

    const fetchComments = (page: number) => {
    if (currentPost.value) {
        commentStore.fetchComments(currentPost.value.id, page);
    }
    };

    onMounted(async () => {
    const postId = Number(route.params.id);
    await blogStore.fetchPost(postId);
    fetchComments(1);
    });

    return {
    currentPost,
    comments,
    currentPage,
    totalPages,
    user,
    newComment,
    isAuthenticated,
    formatDate,
    addComment,
    editComment,
    deleteComment,
    deletePost,
    prevPage,
    nextPage,
    };
},
});
</script>
  