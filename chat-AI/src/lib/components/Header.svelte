<script lang="ts">
import logo from "$lib/assets/logo.png";
    import { onMount } from "svelte";
let sizeOpen = false;
let currentSize = "14px";
    let open = false;
    let currentFont = "Special Elite";

const fontSizes = [
    "12px",
    "14px",
    "16px",
    "18px",
    "20px",
    "24px",
    "28px"
];

function toggleSizeDropdown() {
    sizeOpen = !sizeOpen;
}

function setFontSize(size: string) {
    currentSize = size;
    sizeOpen = false;

    localStorage.setItem("fontSize", size);

    document.documentElement.style.setProperty(
        "--app-font-size",
        size
    );
}


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
        const savedSize =
    localStorage.getItem("fontSize") ||
    "16px";

currentSize = savedSize;

document.documentElement.style.setProperty(
    "--app-font-size",
    savedSize
);
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
        background-color: rgb(25, 25, 25);
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        height: 6vh;
         position: relative;
    }
    .header::after {
    content: "";

    position: absolute;
    left: 0;
    bottom: 0;

    width: 100%;
    height: 2px;

    background: linear-gradient(
        90deg,
        #ff8c1a,
        #0069d2,
        #0e08d1,
        #ff8c1a
    );

    background-size: 300% 100%;

    animation: borderFlow 4s linear infinite;
}

@keyframes borderFlow {
    0% {
        background-position: 0% 50%;
    }

    100% {
        background-position: 300% 50%;
    }
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

    .dropdown {
        position: relative;
        height: 70%;
    }

    .dropdown button {
        border: none;
        font-size: 17px;
        border-radius: 5px;
        height:100%;
        width: 140px;
    }

    .header a {
        font-family: var(--app-font), sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        min-width: 100px;
        height: 100%;
        
        
    }



    .color-link {
    position: relative;
    z-index: 1;

    display: flex;
    align-items: center;
    justify-content: center;

    height: 100%;
    width: 140px;

    background: rgb(25,25,25);

    border-radius: 8px;
    text-decoration: none;
}

.dropdown-btn {
    background:
        linear-gradient(
            90deg,
            #1d8fff,
            #ff8c1a
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color:
        transparent;

    font-weight: 600;
}

    .dropdown-menu {
        position: absolute;
        top: 100%;
        left: 0;
        background: rgb(25, 25, 25);
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
        background: rgb(25, 25, 25);
        color: rgb(255, 255, 255);
        border: none;
        width: 100%;
    }

    .dropdown-menu button:hover {
        background: #eee;
        color:black;
    }

    .logo-link {
    display: flex;
    align-items: center;
    height: 100%;
}

.logo {
    height: 100%;
    width: auto;
    object-fit: contain;
}

.animated-border {
    position: relative;
    padding: 2px;
    border-radius: 12px;
    overflow: hidden;
}

.animated-border::before {
    content: "";

    position: absolute;
    inset: -50%;

    background:
        conic-gradient(
            from 0deg,
            #ff8c1a,
            #0069d2,
            #0e08d1
        );

    animation:
        spin 3s linear infinite;
}

.animated-border button {
    position: relative;
    z-index: 1;

    border: none;

    background:
        rgb(25,25,25);

    color: white;

    border-radius: 8px;

}
.animated-border::before {
    filter:
        blur(8px);

    opacity: .8;
}

.gradient-text {
    background:white ;

    -webkit-background-clip: text;
    background-clip: text;

    -webkit-text-fill-color: transparent;

    font-weight: 700;
}

@keyframes spin {
    from {
        transform:
            rotate(0deg);
    }

    to {
        transform:
            rotate(360deg);
    }
}
</style>

<div class="header">
    <div class="navbar-left">
        <a href="/" class="logo-link">
    <img src={logo} alt="CHAT-AI Logo" class="logo" />
</a>

        <div class="dropdown">
        <div class="animated-border">
            <button
                type="button"
                class="dropdown-btn"
                on:click={toggleDropdown}
            >
                <span class="gradient-text">
                    Font ▾
                </span>
            </button>
        </div>

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
        <div class="dropdown">
        <div class="animated-border">
            <button
                type="button"
                class="dropdown-btn"
                on:click={toggleSizeDropdown}
            >
                <span class="gradient-text">
                    Size ▾
                </span>
            </button>
        </div>

    {#if sizeOpen}
        <div class="dropdown-menu">
            {#each fontSizes as size}
                <button
                    type="button"
                    on:click={() => setFontSize(size)}
                >
                    {size}
                </button>
            {/each}
        </div>
    {/if}

</div>
    <div class="animated-border">
        <a href="/color" class="color-link">
            <span class="gradient-text">
                Color
            </span>
        </a>
    </div>
        
    </div>
</div>