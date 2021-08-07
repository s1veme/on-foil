<template>
	<div>
		<form @submit.prevent="getToken">
			<p>Авторизация</p>
			<input type="login" name="login" autocomplete="off" placeholder="username" required
			v-model="username"
			>
			<input type="password" name="password" autocomplete="off" placeholder="password" required
			v-model="password"
			>
			<button id="login" type="submit"><span>Войти</span></button>
		</form>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			username: '',
			password: ''
		}
	},

	created() {
		if ('exit' in this.$route.query) {
			localStorage.removeItem('token')
			axios.defaults.headers[
				"Authorization"
			] = '';
		}
	},

	methods: {
		async getToken() {
			const userData = {
				username: this.username,
				password: this.password
			}

			const tokenData = await axios.post('/api/token/', userData)

			if (tokenData.data.access) {
				axios.defaults.headers[
					"Authorization"
				] = `Bearer ${tokenData.data.access}`;
				localStorage.setItem('token', tokenData.data.access)

				this.$router.push('/dashboard')
			}
		}
	}
}
</script>

<style>
	
</style>