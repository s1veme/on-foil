<template>
<div class="v-login w-screen h-screen flex justify-center items-center bg-gray-200">
		<form class="p-10 bg-white rounded flex justify-center items-center flex-col shadow-md" @submit.prevent="getLogin">
			<p class="mb-5 text-3xl uppercase text-gray-600">Авторизация</p>
			<input type="login" name="login" class="mb-5 p-3 w-80 focus:border-green-400 rounded border-2 outline-none" autocomplete="off" placeholder="username" required
			v-model="username"
			>
			<input type="password" name="password" class="mb-5 p-3 w-80 focus:border-green-400 rounded border-2 outline-none" autocomplete="off" placeholder="password" required
			v-model="password"
			>
			<button class="bg-green-400 hover:bg-green-500 text-white font-bold p-2 rounded w-80" id="login" type="submit"><span>Войти</span></button>
		</form>
	</div>
</template>

<script>
import { mapActions } from "vuex";
export default {
	name: 'v-login',
	data() {
		return {
			username: "",
			password: ""
		}
	},
	methods: {
		...mapActions(["createToken"]),

		getLogin() {
			const userData = {
				username: this.username,
				password: this.password,
			};

			this.createToken(userData)
			.then(() => this.$router.push('/'))
			.catch(err => console.log(err))
		},
	}
}
</script>