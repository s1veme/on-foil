import { createStore } from 'vuex'
import axios from 'axios'


let store = createStore({
	state() {
		return {
			user: {
				token: localStorage.getItem('token') || '',
			},
			reservation: null
		}
	},
	mutations: {
		setUser(state, userData) {
			console.log(userData)
			if (state.user) {
				state.user = { ...state.user, ...userData }
			} else {
				state.user = userData
			}
			console.log(this.state.user)
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

				commit('setUser', {'token': tokenData.data.access})

				return true
			}
		},

		logout() {
			this.token = ''
			localStorage.removeItem('token')
		}
	},
	getters: {}
})

export default store;