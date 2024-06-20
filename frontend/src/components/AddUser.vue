<template>
  <el-form :model="form" label-width="auto" class="form">
    <el-form-item label="Nombre">
      <el-input v-model="form.nombre" />
    </el-form-item>
    <el-form-item label="Apellido">
      <el-input v-model="form.apellido" required />
    </el-form-item>
    <el-form-item label="Documento">
      <el-input v-model="form.documento" type="numeric" min="10" max="10" />
    </el-form-item>
    <el-form-item label="Edad">
      <el-input v-model="form.edad" type="numeric" required />
    </el-form-item>
    <el-form-item label="Contraseña">
      <el-input v-model="form.password" type="password" required />
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">Guardar</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import axios from 'axios'
import { reactive } from 'vue'
import { ElMessage } from 'element-plus'
import { useStore } from 'vuex'
import { URL } from '../api.js'

const store = useStore()

const getToken = window.localStorage.getItem('token')

const toggleLogged = (token: string) => {
  store.dispatch('logged')
  store.dispatch('token', token)
}

// do not use same name with ref
const form = reactive({
  documento: null,
  nombre: '',
  apellido: '',
  edad: null,
  password: ''
})

const validarEdad = () => {
  if (form.edad !== '' && form.edad !== null) {
    const edad = parseInt(form.edad)
    if (isNaN(edad)) {
      form.edad = null
    } else {
      form.edad = edad
    }
  } else {
    form.edad = null
  }
}

const validarDocumento = () => {
  if (form.documento !== '' && form.documento !== null) {
    const documento = parseInt(form.documento)
    if (isNaN(documento)) {
      form.documento = null
    } else {
      form.documento = documento
    }
  } else {
    form.documento = null
  }
}

const validateData = () => {
  validarEdad()
  validarDocumento()
  if (form.documento && form.nombre && form.apellido && form.edad && form.password) {
    return true
  }
  return false
}

const onSubmit = async () => {
  if (validateData()) {
    try {
      await axios.post(`${URL}/users`, form, {
        headers: { Authorization: `Bearer ${getToken}` }
      })
      form.documento = null
      form.nombre = ''
      form.apellido = ''
      form.edad = null
      form.password = ''
      ElMessage({
        message: 'Usuario Agregado con exito',
        type: 'success'
      })
    } catch (error) {
      console.log(error)
      ElMessage({
        message: 'Error al agregar el usuario',
        type: 'warning'
      })
      if (error.response.status === 401) {
        toggleLogged(null)
        window.localStorage.removeItem('token')
      }
    }
  } else {
    ElMessage({
      message: 'Campos invalidos',
      type: 'warning'
    })
  }
}
</script>

<style scoped>
.form {
  border: 1px black solid;
  border-radius: 10px;
  padding: 20px;
  width: 70%;
}
</style>
