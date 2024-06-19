<template>
  <el-table :data="tableData" style="width: 80%">
    <el-table-column fixed prop="id" label="Id" width="60px" />
    <el-table-column prop="nombre" label="Nombre" />
    <el-table-column prop="apellido" label="Apellido" />
    <el-table-column prop="documento" label="Documento" />
    <el-table-column prop="edad" label="Edad" />
    <el-table-column prop="fecha_creacion" label="Fecha creación" />
    <el-table-column fixed="right" label="Operaciones">
      <template #default="{ row }">
        <el-popconfirm
          title="¿Seguro quieres eliminar este usuario?"
          @confirm="handleDelete(row.id)"
        >
          <template #reference>
            <el-button link type="danger">Eliminar</el-button>
          </template>
        </el-popconfirm>
        <el-button link type="warning" size="small" @click="editUser(row)"> Editar</el-button>
      </template>
    </el-table-column>
  </el-table>

  <el-dialog v-model="dialogVisible" title="Editar Usuario" width="500" :before-close="handleClose">
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
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancelar</el-button>
        <el-button
          type="primary"
          @click="
            () => {
              dialogVisible = false
              onUpdate()
            }
          "
        >
          Confirmar
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script lang="ts" setup>
import axios from 'axios'
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { useStore } from 'vuex'
import { ElMessageBox } from 'element-plus'
import { reactive } from 'vue'

const dialogVisible = ref(false)

const store = useStore()

const getToken = window.localStorage.getItem('token')

const toggleLogged = (token: string) => {
  store.dispatch('logged')
  store.dispatch('token', token)
}
const form = reactive({
  id: '',
  documento: null,
  nombre: '',
  apellido: '',
  edad: null,
  password: ''
})

const handleClose = (done: () => void) => {
  ElMessageBox.confirm('¿Estas seguro que quieres salir?')
    .then(() => {
      done()
    })
    .catch((error) => {
      console.log(error)
    })
}

const tableData = ref([])

const getData = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/users', {
      headers: { Authorization: `Bearer ${getToken}` }
    })
    tableData.value = res.data
  } catch (error) {
    console.log(error)
    if (error.response.status === 401) {
      toggleLogged(null)
    }
  }
}

getData()

const editUser = (user: any) => {
  // Abrir el diálogo de edición
  dialogVisible.value = true

  // Cargar los datos del usuario en el formulario
  form.id = user.id
  form.nombre = user.nombre
  form.apellido = user.apellido
  form.documento = user.documento
  form.edad = user.edad
}

const handleDelete = async (id: string) => {
  try {
    await axios.delete(`http://127.0.0.1:8000/users/${id}`, {
      headers: { Authorization: `Bearer ${getToken}` }
    })

    tableData.value = tableData.value.filter((item) => item.id !== id)

    ElMessage({
      message: `Registro con id ${id} eliminado correctamente.`,
      type: 'success'
    })
  } catch (error) {
    ElMessage({
      message: 'Error al eliminar el registro',
      type: 'warning'
    })
    console.error('Error al eliminar el registro:', error)
    if (error.response.status === 401) {
      toggleLogged(null)
    }
  }
}

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

const clearForm = () => {
  form.id = null
  form.documento = null
  form.nombre = ''
  form.apellido = ''
  form.edad = null
  form.password = ''
}

const onUpdate = async () => {
  if (validateData()) {
    try {
      await axios.put(`http://127.0.0.1:8000/users/${form.id}`, form, {
        headers: { Authorization: `Bearer ${getToken}` }
      })
      clearForm()
      ElMessage({
        message: 'Usuario actualizado correctamente',
        type: 'success'
      })
      getData()
    } catch (error) {
      console.log(error)
      ElMessage({
        message: 'Error al actualizar el usuario',
        type: 'warning'
      })
      if (error.response.status === 401) {
        toggleLogged(null)
      }
    }
  } else {
    ElMessage({
      message: 'Por favor, complete todos los campos correctamente',
      type: 'warning'
    })
  }
}
</script>
