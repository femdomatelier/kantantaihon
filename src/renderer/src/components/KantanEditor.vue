<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from 'vue'
import * as monaco from 'monaco-editor';
import {
  init,
  classModule,
  propsModule,
  styleModule,
  eventListenersModule,
  h,
} from "snabbdom";
import { ipcRenderer } from 'electron';

const kantan = ref(null)
const previewer = ref(null)
const source = ref('Test1\n  Test2')
const isPreview = ref(false)
const compiledLines = ref<string[]>([])

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const compile = (input: string, _1: number, _2: string[]): string => {
  return `<p>${input}</p>`;
};

const patch = init([
  classModule,
  propsModule,
  styleModule,
  eventListenersModule,
]);

compiledLines.value = source.value.split('\n').map(compile)

onMounted(() => {
  if (kantan.value === null || previewer.value === null) {
    return;
  }

  const editor = monaco.editor.create(kantan.value, {
    value: source.value,
    language: 'plaintext',
    theme: 'vs-dark',
    automaticLayout: true,
  });

  editor.getModel()?.onDidChangeContent((e: monaco.editor.IModelContentChangedEvent) => {
    source.value = editor.getValue();
    e.changes.forEach((change: monaco.editor.IModelContentChange) => {
      const editorModel = editor.getModel();
      if (editorModel === null) {
        return;
      }
      const { range, text } = change;
      const startLine = range.startLineNumber - 1;
      let endLine = range.endLineNumber - 1;
      if (text === '') {
        // Delete
        const line = editorModel.getLineContent(startLine + 1);
        compiledLines.value.splice(startLine, endLine - startLine + 1, compile(line, startLine, []));
      }
      else {
        // Insert or Replace
        const lines = [];
        endLine += text.split('\n').length;
        const editorModel = editor.getModel();
        for (let i = startLine; i <= endLine; i++) {
          if (i + 1 > editorModel.getLineCount())
            continue;
          const line = editorModel.getLineContent(i + 1);
          if (line === undefined) {
            continue;
          }
          lines.push(line);
        }
        const compiled = lines.map((line, index) => compile(line, startLine + index, lines));
        compiledLines.value.splice(startLine, endLine - startLine + 1, ...compiled);
      }
    });
  });
});

</script>

<template>
  <div class="editor-container">
    <div class="flex flex-row h-full">
      <div class="editor" ref="kantan"></div>
      <div class="preview" ref="previewer">
        <div v-for="(line, index) in compiledLines" :key="index"
          class="flex items-start space-x-4 py-1 border-b border-gray-300">
          <div class="text-gray-500 font-mono text-sm w-10 text-right">{{ index }}</div>
          <div class="flex-1 text-gray-900">
            <span v-html="line" class="whitespace-pre"></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.editor {
  width: 50%;
  height: 95%;
}

.preview {
  width: 50%;
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