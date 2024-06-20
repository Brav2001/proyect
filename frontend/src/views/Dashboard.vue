<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <el-menu
          active-text-color="#fff"
          background-color="#002130"
          class="el-menu-vertical-demo side"
          text-color="#d7d7d7"
        >
          <nav style="margin-top: 70px">
            <RouterLink to="/">
              <el-menu-item index="1">
                <span>Agregar Usuario</span>
              </el-menu-item>
            </RouterLink>
            <RouterLink to="/list">
              <el-menu-item index="2">
                <span>Lista de Usuarios</span>
              </el-menu-item>
            </RouterLink>
            <el-button type="plain" size="small" style="width: 100%" @click="LogOut"
              >Cerrar Sesión</el-button
            >
          </nav>
        </el-menu>
      </el-aside>
      <el-container>
        <el-header class="header">
          <span style="font-size: 20px; font-weight: bold"> TMsoft Usuario </span>
        </el-header>
        <el-main class="main">
          <RouterView />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.header {
  width: 100%;
  color: #fff;
  display: flex;
  align-items: center;
  background-color: #395e6f;
}
.main {
  width: 100%;
  min-height: calc(100vh - 60px);
  background-color: #ffffff;
  color: #000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.side {
  min-height: 100vh;
  border: none;
  display: flex;
  justify-content: center;
}
</style>

<script lang="ts" setup>
import { useStore } from 'vuex'
const store = useStore()

const toggleLogged = (token) => {
  store.dispatch('logged')
  store.dispatch('token', token)
}

const LogOut = () => {
  toggleLogged(null)
  window.localStorage.removeItem('token')
}
</script>
