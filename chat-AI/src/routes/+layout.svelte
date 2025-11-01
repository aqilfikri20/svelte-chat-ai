<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import "../app.css"
	import Header from '$lib/components/Header.svelte';
	let { children } = $props();
</script>

<style>
</style>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>
<Header />
{@render children?.()}
