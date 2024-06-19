import { createRouter, createWebHistory } from 'vue-router'
import Adduser from '../components/AddUser.vue'
import ListUsers from '../components/ListUsers.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'AddUser',
      component: Adduser
    },
    {
      path: '/list',
      name: 'ListUser',
      component: ListUsers
    }
  ]
})

export default router
