<script setup>
import { ref, watch, onMounted } from 'vue'
import * as monaco from 'monaco-editor';

const kantan = ref(null)
const source = ref('Test')
const isPreview = ref(false)

onMounted(() => {
  const editor = monaco.editor.create(kantan.value, {
    value: source.value,
    language: 'plaintext',
    theme: 'vs-dark'
  });
});

const toggleSwitch = () => {
  isPreview.value = !isPreview.value
};

</script>

<template>
  <div class="editor-container">
    <div v-show="!isPreview" class="editor" ref="kantan"></div>
    <div v-show="isPreview" class="preview">XXXXXXXXXXXXXXX</div>
    <div class="switch-container">
      <div class="flex justify-end">
        <div class="w-16 h-8 rounded-full flex items-center cursor-pointer transition-all duration-300"
          :class="isPreview ? 'bg-gray-400' : 'bg-white border border-gray-300'" @click="toggleSwitch">
          <div class="w-6 h-6 bg-white rounded-full shadow-md transform transition-all duration-300"
            :class="isPreview ? 'translate-x-8 bg-gray-600' : 'translate-x-1 bg-gray-300'"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.editor {
  width: 100%;
  height: 95%;
}

.preview {
  width: 100%;
  height: 95%;
}

.switch-container {
  height: 5%;
}

.editor-container {
  width: 95vw;
  height: 95vh;
}
</style>