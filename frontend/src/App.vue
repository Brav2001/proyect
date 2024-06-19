<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import Login from './views/Login.vue'
import Dashboard from './views/Dashboard.vue'
import { computed } from 'vue'
import { useStore } from 'vuex'

const store = useStore()

const isLoggedIn = computed(() => store.getters.isLoggedIn)

const toggleLogged = (token) => {
  store.dispatch('logged')
  store.dispatch('token', token)
}

const isToken = window.localStorage.getItem('token')

if (isToken) {
  toggleLogged(isToken)
}
</script>

<template>
  <template v-if="isLoggedIn">
    <Dashboard />
  </template>
  <template v-else>
    <Login />
  </template>
</template>
