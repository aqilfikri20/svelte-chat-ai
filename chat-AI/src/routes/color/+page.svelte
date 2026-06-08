<script lang="ts">
let loaded = false;
import { onMount } from "svelte";
import { goto } from "$app/navigation";

function backToChat() {
    goto("/");
}

let userR = 0;
let userG = 201;
let userB = 111;

let assistantR = 37;
let assistantG = 99;
let assistantB = 235;

let backgroundR = 25;
let backgroundG = 25;
let backgroundB = 25;

let fontR = 255;
let fontG = 255;
let fontB = 255;

$: userColor =
    `rgb(${userR}, ${userG}, ${userB})`;

$: assistantColor =
    `rgb(${assistantR}, ${assistantG}, ${assistantB})`;

$: backgroundColor =
    `rgb(${backgroundR}, ${backgroundG}, ${backgroundB})`;
    

$: fontColor =
    `rgb(${fontR}, ${fontG}, ${fontB})`;

$: if (loaded) {
    document.documentElement.style.setProperty(
        "--user-bubble",
        userColor
    );

    localStorage.setItem(
        "userBubble",
        JSON.stringify({
            r: userR,
            g: userG,
            b: userB
        })
    );
}

$: if (loaded) {
    document.documentElement.style.setProperty(
        "--assistant-bubble",
        assistantColor
    );

    localStorage.setItem(
        "assistantBubble",
        JSON.stringify({
            r: assistantR,
            g: assistantG,
            b: assistantB
        })
    );
}

$: if (loaded) {
    document.documentElement.style.setProperty(
        "--background",
        backgroundColor
    );

    localStorage.setItem(
        "backgroundColor",
        JSON.stringify({
            r: backgroundR,
            g: backgroundG,
            b: backgroundB
        })
    );
}

$: if (loaded) {
    document.documentElement.style.setProperty(
        "--font-color",
        fontColor
    );

    localStorage.setItem(
        "fontColor",
        JSON.stringify({
            r: fontR,
            g: fontG,
            b: fontB
        })
    );
}

onMount(() => {
    const savedUser =
        localStorage.getItem("userBubble");

    if (savedUser) {
        const rgb = JSON.parse(savedUser);

        userR = rgb.r;
        userG = rgb.g;
        userB = rgb.b;
    }

    const savedAssistant =
        localStorage.getItem("assistantBubble");

    if (savedAssistant) {
        const rgb = JSON.parse(savedAssistant);

        assistantR = rgb.r;
        assistantG = rgb.g;
        assistantB = rgb.b;
    }

    const savedBackground =
        localStorage.getItem("backgroundColor");

    if (savedBackground) {
        const rgb = JSON.parse(savedBackground);

        backgroundR = rgb.r;
        backgroundG = rgb.g;
        backgroundB = rgb.b;
    }
    
    const savedFontColor =
        localStorage.getItem("fontColor");

    if (savedFontColor) {
        const rgb = JSON.parse(savedFontColor);

        fontR = rgb.r;
        fontG = rgb.g;
        fontB = rgb.b;
    }

    loaded = true;
});
</script>
<div class="container">
    <h2>Warna Bubble User</h2>

    <div class="preview" style="background:{userColor}">
        Contoh Pesan User
    </div>

    <label for="user-red">
        Merah ({userR})
    </label>
    <input
        id="user-red"
        type="range"
        min="0"
        max="255"
        bind:value={userR}
    />

    <label for="user-green">
        Hijau ({userG})
    </label>
    <input
        id="user-green"
        type="range"
        min="0"
        max="255"
        bind:value={userG}
    />

    <label for="user-blue">
        Biru ({userB})
    </label>
    <input
        id="user-blue"
        type="range"
        min="0"
        max="255"
        bind:value={userB}
    />

    <p>{userColor}</p>

    <h2>Warna Bubble Assistant</h2>

    <div
        class="preview"
        style="background:{assistantColor}"
    >
        Contoh Pesan Assistant
    </div>

    <label for="assistant-red">
        Merah ({assistantR})
    </label>
    <input
        id="assistant-red"
        type="range"
        min="0"
        max="255"
        bind:value={assistantR}
    />

    <label for="assistant-green">
        Hijau ({assistantG})
    </label>
    <input
        id="assistant-green"
        type="range"
        min="0"
        max="255"
        bind:value={assistantG}
    />

    <label for="assistant-blue">
        Biru ({assistantB})
    </label>
    <input
        id="assistant-blue"
        type="range"
        min="0"
        max="255"
        bind:value={assistantB}
    />

    <p>{assistantColor}</p>


        <h2>Warna Font</h2>


    <label for="font-red">
        Merah ({fontR})
    </label>
    <input
        id="font-red"
        type="range"
        min="0"
        max="255"
        bind:value={fontR}
    />

    <label for="font-green">
        Hijau ({fontG})
    </label>
    <input
        id="font-green"
        type="range"
        min="0"
        max="255"
        bind:value={fontG}
    />

    <label for="font-blue">
        Biru ({fontB})
    </label>
    <input
        id="font-blue"
        type="range"
        min="0"
        max="255"
        bind:value={fontB}
    />

    <p>{fontColor}</p>

        <h2>Warna Background</h2>


    <label for="background-red">
        Merah ({backgroundR})
    </label>
    <input
        id="background-red"
        type="range"
        min="0"
        max="255"
        bind:value={backgroundR}
    />

    <label for="background-green">
        Hijau ({backgroundG})
    </label>
    <input
        id="background-green"
        type="range"
        min="0"
        max="255"
        bind:value={backgroundG}
    />

    <label for="background-blue">
        Biru ({backgroundB})
    </label>
    <input
        id="background-blue"
        type="range"
        min="0"
        max="255"
        bind:value={backgroundB}
    />

    <p>{backgroundColor}</p>

    <button on:click={backToChat}>
        Simpan & Kembali
    </button>
</div>


<style>
    .container {
    max-width: 700px;
    margin: auto;
    padding: 25px;
    border-radius: 20px;
    background: #1e1e1e;
    color: #f5f5f5;
    box-shadow:
        0 10px 30px rgba(0,0,0,0.3),
        0 0 0 1px rgba(255,255,255,0.05);

    display: flex;
    flex-direction: column;
    gap: 15px;
}

.section-title {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 10px;
}

.preview {
    padding: 16px 20px;
    border-radius: 18px;
    color: var(--font-color);
    font-size: 1rem;
    font-weight: 500;
    width: fit-content;
    min-width: 220px;
    width: 100%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    transition: all 0.15s ease;
}

.preview:hover {
    transform: translateY(-2px);
}

label {
    font-weight: 600;
    font-size: 0.95rem;
}

input[type="range"] {
    width: 100%;
    height: 8px;
    border-radius: 999px;
    appearance: none;
    background: #444;
    outline: none;
}

/* Slider merah */
    
#user-red,
#assistant-red,
#background-red,
#font-red {
    accent-color: rgb(255, 60, 60);
}

/* Slider hijau */
#background-green,
#font-green,
#user-green,
#assistant-green {
    accent-color: rgb(0, 220, 120);
}

/* Slider biru */
#background-blue,
#font-blue,
#user-blue,
#assistant-blue {
    accent-color: rgb(70, 130, 255);
}

.color-value {
    font-family: monospace;
    background: #2a2a2a;
    padding: 8px 12px;
    border-radius: 8px;
    width: fit-content;
}

button {
    margin-top: 20px;
    padding: 12px 20px;
    border: none;
    border-radius: 12px;
    background: #2563eb;
    color: white;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition:
        background 0.2s ease,
        transform 0.2s ease;
}

button:hover {
    background: #1d4ed8;
    transform: translateY(-2px);
}

button:active {
    transform: translateY(0);
}

.page-wrapper {
    min-height: 100vh;
    background: #121212;
    padding: 30px;
}

.divider {
    margin: 20px 0;
    height: 1px;
    background: rgba(255,255,255,0.1);
}
</style>