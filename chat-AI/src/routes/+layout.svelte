<script lang="ts">
import { onMount } from "svelte";
	import favicon from '$lib/assets/favicon.svg';
	import "../app.css"
	import Header from '$lib/components/Header.svelte';
	let loaded = false;
	let { children } = $props();

onMount(() => {
	const savedFont =
    localStorage.getItem("font");

if (savedFont) {
    document.documentElement.style.setProperty(
        "--app-font",
        `"${savedFont}"`
    );
}

    const savedUser =
        localStorage.getItem("userBubble");

    if (savedUser) {
        const rgb = JSON.parse(savedUser);

        document.documentElement.style.setProperty(
            "--user-bubble",
            `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`
        );
    }

    const savedAssistant =
        localStorage.getItem("assistantBubble");

    if (savedAssistant) {
        const rgb = JSON.parse(savedAssistant);

        document.documentElement.style.setProperty(
            "--assistant-bubble",
            `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`
        );
    }

	const savedBackground =
		localStorage.getItem("backgroundColor");

	if (savedBackground) {
		const rgb = JSON.parse(savedBackground);

		document.documentElement.style.setProperty(
			"--background",
			`rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`
		);
	}
});
</script>

<style>
main {
	background: var(--background);
}
</style>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>
<Header />
<main>
	{@render children?.()}
</main>

