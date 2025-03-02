<script setup lang="ts">
import { ref, onMounted, watchEffect } from 'vue'
import {
  init,
  classModule,
  propsModule,
  styleModule,
  eventListenersModule,
  h
} from "snabbdom";
import KantanEditor from './components/KantanEditor.vue'

const patch = init([
  classModule,
  propsModule,
  styleModule,
  eventListenersModule,
])


const ipcHandle = (): void => window.electron.ipcRenderer.send('ping')
</script>

<template>
  <kantan-editor/>
</template>

<style>
html, body, #app {
  margin: 0;
  height: 100%;
}

</style>