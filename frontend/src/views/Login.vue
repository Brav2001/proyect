<template class="container">
  <el-form :model="form" label-width="auto" style="max-width: 600px">
    <el-form-item label="documento">
      <el-input v-model="form.documento" />
    </el-form-item>
    <el-form-item label="password">
      <el-input v-model="form.password" type="password" />
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">Log In</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { reactive } from 'vue'

// do not use same name with ref
const form = reactive({
  documento: '',
  password: ''
})

const onSubmit = () => {
  console.log('submit!')
}
</script>

<style>
container {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
