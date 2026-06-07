<script lang="ts">
    import { onMount } from "svelte";

    let open = false;
    let currentFont = "Special Elite";

    const fonts = [
        "Special Elite",
        "Arial",
        "Georgia",
        "Courier New",
        "Times New Roman",
        "Verdana",
        "Trebuchet MS"
    ];

    function toggleDropdown() {
        open = !open;
    }

    function setFont(font: string) {
        currentFont = font;
        open = false;

        localStorage.setItem("font", font);

        document.documentElement.style.setProperty(
            "--app-font",
            `"${font}"`
        );
    }

    onMount(() => {
        const saved =
            localStorage.getItem("font") ||
            "Special Elite";

        currentFont = saved;

        document.documentElement.style.setProperty(
            "--app-font",
            `"${saved}"`
        );
    });
</script>

<style>
    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        border-bottom: #ff0f0f 1px solid;
        height: 5vh;
    }

    .navbar-left {
        display: flex;
        margin-left: 10px;
        flex-direction: row;
        gap: 10px;
        height: 100%;
        align-items: center;
    }

    .navbar-right {
        display: flex;
        flex-direction: row;
        margin-right: 15px;
        height: 100%;
    }

    a {
        text-decoration: none;
        cursor: pointer;
    }

    a:visited {
        color: inherit;
    }

    a:hover {
        color: blue;
    }

    .dropdown {
        position: relative;
        height: 100%;
    }

    .dropdown button {
        border: none;
        font-size: 1rem;
        border-radius: 5px;
        height: 100%;
        min-width: 150px;
    }

    .header a {
        font-family: var(--app-font), sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: black;
        min-width: 100px;
        height: 100%;
    }

    .dropdown-btn {
        font-family: var(--app-font), sans-serif;
        cursor: pointer;
    }

    .dropdown-menu {
        position: absolute;
        top: 100%;
        left: 0;
        background: white;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        min-width: 220px;
        z-index: 10;
    }

    .dropdown-menu button {
        padding: 0.5rem;
        text-align: left;
        background: white;
        color: black;
        border: none;
        width: 100%;
    }

    .dropdown-menu button:hover {
        background: #eee;
    }
</style>

<div class="header">
    <div class="navbar-left">
        <a href="/">CHAT-AI</a>

        <div class="dropdown">
            <button
                type="button"
                class="dropdown-btn"
                on:click={toggleDropdown}
            >
                {currentFont} ▾
            </button>

            {#if open}
                <div class="dropdown-menu">
                    {#each fonts as font}
                        <button
                            type="button"
                            style="font-family:{font}"
                            on:click={() => setFont(font)}
                        >
                            Aa Bb Cc — {font}
                        </button>
                    {/each}
                </div>
            {/if}
        </div>

        <a href="/setting">Warna</a>
    </div>
</div>