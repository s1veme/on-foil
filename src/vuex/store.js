import { createStore } from 'vuex'
import axios from 'axios'


let store = createStore({
	state() {
		return {
			user: {
				token: localStorage.getItem('token') || '',
			}
		}
	},
	mutations: {
		setUser(state, userData) {
			if (state.user) {
				state.user = { ...state.user, ...userData }
			} else {
				state.user = userData
			}
		},
	},
	actions: {
		async createToken({commit}, user) {
			const tokenData = await axios.post('/api/token/', user)
			if (tokenData.data.access) {
				axios.defaults.headers[
					"Authorization"
				] = `Bearer ${tokenData.data.access}`;
				localStorage.setItem('token', tokenData.data.access)

				commit('setUser', tokenData.data.access)
			}
		}
	},
	getters: {}
})

export default store;