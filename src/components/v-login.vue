<template>
	<div class="v-login">
		<form @submit.prevent="getLogin">
			<input type="text" v-model="username" required>
			<input type="password" v-model="password" required>
			<button type="submit">
				Login
			</button>
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