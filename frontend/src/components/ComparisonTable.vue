<template>
  <div class="card my-8">
    <h3 v-if="title" class="text-2xl font-bold text-gray-800 mb-6">{{ title }}</h3>
    <div class="overflow-x-auto">
      <table class="w-full">
        <thead>
          <tr class="border-b-2 border-gray-300">
            <th class="py-3 px-4 text-left font-bold text-gray-700">{{ headers[0] }}</th>
            <th 
              v-for="(header, index) in headers.slice(1)" 
              :key="index"
              class="py-3 px-4 text-left font-bold"
              :class="index === 0 ? 'text-blue-600' : 'text-purple-600'"
            >
              {{ header }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="(row, rowIndex) in rows" 
            :key="rowIndex"
            class="border-b border-gray-200 hover:bg-gray-50 transition-colors"
          >
            <td class="py-4 px-4 font-semibold text-gray-700">{{ row.label }}</td>
            <td 
              v-for="(value, colIndex) in row.values" 
              :key="colIndex"
              class="py-4 px-4"
            >
              <component 
                :is="getValueComponent(value)" 
                :value="value"
                :index="colIndex"
              />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { h } from 'vue'

defineProps({
  title: String,
  headers: {
    type: Array,
    required: true
  },
  rows: {
    type: Array,
    required: true
  }
})

const getValueComponent = (value) => {
  return (props) => {
    const colorClass = props.index === 0 ? 'text-blue-700' : 'text-purple-700'
    
    if (typeof value === 'object' && value.highlight) {
      return h('span', { 
        class: `font-bold ${colorClass} px-2 py-1 bg-opacity-20 rounded`,
        style: props.index === 0 ? 'background-color: rgba(59, 130, 246, 0.1)' : 'background-color: rgba(168, 85, 247, 0.1)'
      }, value.text)
    }
    
    return h('span', { class: 'text-gray-700' }, value)
  }
}
</script>

