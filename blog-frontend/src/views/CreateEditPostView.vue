<template>
    <div class="create-edit-post">
      <h2>{{ isEditing ? 'Edit Post' : 'Create New Post' }}</h2>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="title">Title:</label>
          <input v-model="title" id="title" type="text" required />
        </div>
        <div>
          <label for="content">Content:</label>
          <textarea v-model="content" id="content" required></textarea>
        </div>
        <button type="submit">{{ isEditing ? 'Update' : 'Create' }}</button>
      </form>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref, computed, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { useBlogStore } from '@/stores/blog';
  
  export default defineComponent({
    name: 'CreateEditPost',
    setup() {
      const route = useRoute();
      const router = useRouter();
      const blogStore = useBlogStore();
  
      const title = ref('');
      const content = ref('');
  
      const isEditing = computed(() => !!route.params.id);
  
      const handleSubmit = async () => {
        const postData = { title: title.value, content: content.value };
        
        if (isEditing.value) {
          const postId = Number(route.params.id);
          await blogStore.updatePost(postId, postData);
        } else {
          await blogStore.createPost(postData);
        }
  
        router.push('/');
      };
  
      onMounted(async () => {
        if (isEditing.value) {
          const postId = Number(route.params.id);
          const post = await blogStore.fetchPost(postId);
          if (post && post.value) {
            title.value = post.value.title;
            content.value = post.value.content;
          }
        }
      });
  
      return {
        title,
        content,
        isEditing,
        handleSubmit,
      };
    },
  });
  </script>