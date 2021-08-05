<template>
	<div class="v-admin-header container mx-auto py-2 font-Montserrat flex">
		<button class="inline-flex items-center" @click="logout">
			<img src="@/assets/svg/exit.svg" alt="exit image" class="mr-2 w-4">
			<p class="text-2xl">Выйти из сессии</p>
		</button>
	</div>
</template>

<script>
export default {
	name: 'v-admin-header',

	methods: {
		logout() {
			this.$store.dispatch('logout');
			this.$router.push('/');
		}
	}
}
</script>