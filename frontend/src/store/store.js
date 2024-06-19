import { createStore } from 'vuex'

const state = {
  logged: false,
  token: null
}

const mutations = {
  changeLogged(state) {
    state.logged = !state.logged
  },

  changeToken(state, newToken) {
    state.token = newToken
  }
}

const actions = {
  logged: ({ commit }) => commit('changeLogged'),
  token: ({ commit, token }) => commit('changeToken', token)
}
const getters = {
  isLoggedIn: (state) => state.logged,
  getToken: (state) => state.token
}

export default createStore({
  state,
  getters,
  actions,
  mutations
})
