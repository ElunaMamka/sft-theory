<template>
  <div id="app" class="min-h-screen">
    <!-- 顶部导航栏 -->
    <nav class="bg-white shadow-md sticky top-0 z-50">
      <div class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-500 rounded-lg flex items-center justify-center">
              <span class="text-white font-bold text-xl">S</span>
            </div>
            <h1 class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              SFT原理教学系统
            </h1>
          </div>
          
          <!-- 导航菜单 -->
          <div class="hidden md:flex space-x-6">
            <router-link 
              v-for="route in navRoutes" 
              :key="route.path"
              :to="route.path"
              class="nav-link"
              :class="{ 'active': $route.path === route.path }"
            >
              {{ route.name }}
            </router-link>
          </div>
          
          <!-- 移动端菜单按钮 -->
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
        
        <!-- 移动端菜单 -->
        <div v-if="mobileMenuOpen" class="md:hidden mt-4 space-y-2">
          <router-link 
            v-for="route in navRoutes" 
            :key="route.path"
            :to="route.path"
            @click="mobileMenuOpen = false"
            class="block py-2 px-4 hover:bg-blue-50 rounded-lg transition-colors"
            :class="{ 'bg-blue-100': $route.path === route.path }"
          >
            {{ route.name }}
          </router-link>
        </div>
      </div>
    </nav>

    <!-- 主内容区域 -->
    <main class="container mx-auto px-4 py-8">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- 页脚 -->
    <footer class="bg-white border-t mt-16 py-8">
      <div class="container mx-auto px-4 text-center text-gray-600">
        <p>SFT原理交互式教学系统 © 2025</p>
        <p class="mt-2 text-sm">为基础薄弱的学生精心设计，图文并茂，形象生动</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const mobileMenuOpen = ref(false)

const navRoutes = [
  { path: '/', name: '首页' },
  { path: '/part1', name: '预训练vs SFT' },
  { path: '/part2', name: 'LoRA' },
  { path: '/part3', name: '数据集' },
  { path: '/part4', name: '实践工作流' }
]
</script>

<style scoped>
.nav-link {
  @apply px-4 py-2 rounded-lg transition-all duration-300 font-medium;
  @apply hover:bg-blue-50 hover:text-blue-600;
}

.nav-link.active {
  @apply bg-gradient-to-r from-blue-500 to-purple-500 text-white;
}
</style>

