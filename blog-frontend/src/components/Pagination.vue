<template>
  <div class="flex justify-center mt-4">
    <button
      class="px-4 py-2 mx-1 text-white bg-blue-500 rounded hover:bg-blue-600 disabled:opacity-50"
      @click="prevPage"
      :disabled="currentPage === 1"
    >
      Previous
    </button>
    <span class="text-lg"> Page {{ currentPage }} of {{ totalPages }} </span>
    <button
      class="px-4 py-2 mx-1 text-white bg-blue-500 rounded hover:bg-blue-600 disabled:opacity-50"
      @click="nextPage"
      :disabled="currentPage === totalPages"
    >
      Next
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "PaginationComponent",
  props: {
    currentPage: {
      type: Number,
      required: true,
    },
    totalPages: {
      type: Number,
      required: true,
    },
  },
  emits: ["update:currentPage"],
  methods: {
    prevPage() {
      if (this.currentPage > 1) {
        this.$emit("update:currentPage", this.currentPage - 1);
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.$emit("update:currentPage", this.currentPage + 1);
      }
    },
  },
});
</script>

<style scoped></style>
