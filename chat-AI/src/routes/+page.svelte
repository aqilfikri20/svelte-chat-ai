<script lang="ts">
 import ChatBubble from "$lib/components/ChatBubble.svelte";
import { onMount, tick } from "svelte";

let textarea: HTMLTextAreaElement;
let messages = [
  { role: "assistant", text: "Halo! Aku ChatGPT mini buatan Aqil 😄" },
  { role: "assistant", text: "Silahkan Tanyakan Apapun..." }
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

  // siapkan payload (kirim ringkasan / beberapa pesan terakhir untuk konteks)
  // kirim hanya beberapa pesan terakhir supaya payload tidak terlalu besar
  const context = messages.slice(-8); // kirim 8 pesan terakhir sebagai konteks

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
      // auto-scroll: scroll chat-output to bottom
      // kecil: execute after dom updates
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
        background-color: rgb(55, 55, 55);
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

    button[disabled] { opacity: 0.6; cursor: not-allowed; }
</style>

<div class="chat-container">
    <div class="chat-output">
        {#each messages as m}
             <ChatBubble role={m.role} text={m.text} />
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
                    Mengirim...
                {:else}
                    Send
                {/if}
        </button>
    </div>
</div>