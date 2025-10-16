import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

// 导入页面组件
import Home from './pages/Home.vue'
import Part1 from './pages/Part1.vue'
import Part2 from './pages/Part2.vue'
import Part3 from './pages/Part3.vue'
import Part4 from './pages/Part4.vue'

const routes = [
  { path: '/', component: Home, meta: { title: '课程首页' } },
  { path: '/part1', component: Part1, meta: { title: '第一部分：预训练 vs SFT' } },
  { path: '/part2', component: Part2, meta: { title: '第二部分：LoRA高效微调' } },
  { path: '/part3', component: Part3, meta: { title: '第三部分：SFT数据集' } },
  { path: '/part4', component: Part4, meta: { title: '第四部分：SFT实践工作流' } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')

