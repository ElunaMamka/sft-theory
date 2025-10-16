<template>
  <div class="card my-8 bg-gradient-to-br from-blue-50 to-purple-50">
    <h3 v-if="title" class="text-2xl font-bold text-gray-800 mb-6 text-center">{{ title }}</h3>
    <div class="flex justify-center items-center min-h-[300px] relative">
      <slot></slot>
    </div>
    <p v-if="description" class="text-center text-gray-600 mt-6 text-lg">{{ description }}</p>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  description: String
})
</script>

