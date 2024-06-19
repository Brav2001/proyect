<template>
  <div class="container">
    <el-form
      :model="form"
      label-width="auto"
      style="max-width: 600px; border: 1px black solid; border-radius: 10px; padding: 20px"
    >
      <el-form-item label="document">
        <el-input v-model="form.documento" />
      </el-form-item>
      <el-form-item label="password">
        <el-input v-model="form.password" type="password" />
      </el-form-item>

      <div class="submit">
        <el-button type="primary" @click="onSubmit" style="width: 70%">Log In</el-button>
      </div>
    </el-form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import axios from 'axios'
import { useStore } from 'vuex'

const store = useStore()

const form = reactive({
  documento: '',
  password: ''
})

const toggleLogged = (token) => {
  store.dispatch('logged')
  store.dispatch('token', token)
}

const onSubmit = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/login', form)
    const token = response.data.token
    window.localStorage.setItem('token', token)
    toggleLogged(token)
  } catch (error) {
    console.error('Error durante el inicio de sesión:', error)
  }
}
</script>

<style>
.container {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.submit {
  display: flex;
  justify-content: center;
}
</style>
