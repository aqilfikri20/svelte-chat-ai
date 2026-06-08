<script lang="ts">


import ChatBubble from "$lib/components/ChatBubble.svelte";
import { onMount, tick } from "svelte";

async function regenerateMessage(index: number) {
    if (messages[index].role !== "assistant")
        return;

    let userMessage = null;

    for (let i = index - 1; i >= 0; i--) {
        if (messages[i].role === "user") {
            userMessage = messages[i];
            break;
        }
    }

    if (!userMessage) return;

messages = [
    ...messages,
    {
        role: "assistant",
        text: "Menghasilkan ulang..."
    }
];

const loadingIndex =
    messages.length - 1;

messages = [...messages];

try {
    const resp = await fetch(
        "http://localhost:8000/chat",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                messages: [userMessage]
            })
        }
    );

    if (!resp.ok) {
        throw new Error(
            `Server error ${resp.status}`
        );
    }

    const data = await resp.json();

    messages[loadingIndex] = {
        role: "assistant",
        text: data.reply
    };
}
catch (err) {
    messages[loadingIndex] = {
        role: "assistant",
        text: "Gagal menghasilkan ulang."
    };
}
finally {
    messages = [...messages];
}

await tick();

const container =
    document.querySelector(
        ".chat-output"
    ) as HTMLElement;

if (container) {
    container.scrollTop =
        container.scrollHeight;
}
}

let textarea: HTMLTextAreaElement;
let messages = [
  { role: "assistant", text: "Halo! Selamat Datang.\n\n Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄" },
  { role: "assistant", text: `Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄Silakan Ketik Kata Kunci untuk Membuat Cerita Anda 😄` },
];
let input = "";
let loading = false;

const adjustHeight = () => {
  if (textarea) {
    textarea.style.height = "auto";
    textarea.style.height = `${textarea.scrollHeight}px`;
  }
};

onMount(() => {
  adjustHeight();
});

const handleInput = () => {
  adjustHeight();
  // optional: limit input length
  if (input.length > 4000) input = input.slice(0, 4000);
};

async function sendMessage() {
  const trimmed = input.trim();
  if (!trimmed || loading) return;

  // tambah pesan user dulu ke UI
  messages = [...messages, { role: "user", text: trimmed }];
  input = "";
  adjustHeight();
  loading = true;

  const context = messages.slice(-8); 

  try {
    const resp = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: context })
    });

    if (!resp.ok) {
      const txt = await resp.text();
      throw new Error(`Server error: ${resp.status} ${txt}`);
    }

    const data = await resp.json();
    // backend mengembalikan { reply: "..." }
    if (data && data.reply) {
      messages = [...messages, { role: "assistant", text: data.reply }];
   
      await tick();
      const container = document.querySelector('.chat-output') as HTMLElement;
      if (container) container.scrollTop = container.scrollHeight;
    } else {
      throw new Error("Invalid response from server");
    }
  } catch (err) {
    console.error(err);
    messages = [...messages, { role: "assistant", text: "Terjadi kesalahan saat menghubungi server." }];
  } finally {
    loading = false;
  }
}

</script>
<style>
    .chat-container{
        background: var(--background);
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 95vh;
    }
    .chat-output{ 
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 90%;
        width: 80%;
        overflow-y:auto;
    }

    .chat-input{
        bottom: 5vh;
        display: flex;
        flex-direction: row;
        width: 80%;
        height: 5vh;
        align-items: flex-end;
    }

    .chat-output::-webkit-scrollbar {
        display: none; /* Chrome, Safari */
    }

    .chat-output {
        -ms-overflow-style: none;  /* Internet Explorer dan Edge lama */
        scrollbar-width: none;     /* Firefox */
    }

    .text-input{
        flex: 1;
        width: 90%;
        height: 100%;
        display: flex;
        align-items: flex-end;
    }

    textarea{
        min-height: 5vh;
        margin: 0;
        padding-top: 1vh;
        padding-bottom: 1vh;
        padding-left: 10px;
        width: 100%;
        border-bottom-left-radius: 10px;
        border-top-left-radius: 10px;
        font-size: 16px;
        resize: none;
        overflow: hidden;
        transform-origin: bottom;
        transition: height 0.1s;
        box-sizing: border-box;
    }

    .chat-input button{
        width: 10%;
        height: 100%;
        align-self: flex-end;
    }

    button{
        margin: 0;
        border-radius: 0px 10px 10px 0px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        background-color: rgb(25, 25, 25);
        color: white;
        border: white 3px solid;
        font-family:var(--app-font), sans-serif;
         transition: background-color 0.2s, color 0.2s;
    }

    button[disabled] { opacity: 0.6; cursor: not-allowed; }
</style>

<div class="chat-container">
    <div class="chat-output">
        {#each messages as m, index}
             <ChatBubble role={m.role} text={m.text} on:regenerate={() => regenerateMessage(index)}
 />
        {/each}
    </div>

    <div class="chat-input">
        <div class="text-input">
            <textarea
            id="chatInput"
            bind:this={textarea}
            bind:value={input}
            on:input={handleInput}
            rows="1"
            placeholder="Tulis Pesan Anda Disini.."></textarea>
        </div>
        <button on:click={sendMessage} disabled={loading}>
                {#if loading}
                    Sending...
                {:else}
                    Send
                {/if}
        </button>
    </div>
</div>