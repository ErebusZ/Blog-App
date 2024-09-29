<template>
    <div class="search-bar">
      <input 
        v-model="searchQuery" 
        @input="search" 
        placeholder="Search ... "
      />
    </div>
  </template>
  
  <script lang="ts">

  import { defineComponent, ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default defineComponent({
    name: 'SearchBar',
    setup() {
      const router = useRouter();
      const searchQuery = ref('');
  
      const search = () => {
        router.push({ query: { ...router.currentRoute.value.query, search: searchQuery.value, page: 1 } });
      };
  
      return {
        searchQuery,
        search,
      };
    },
  });
  </script>