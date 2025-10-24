<script lang="ts">
    import {onMount} from "svelte";
    export let data;
    let textarea: HTMLTextAreaElement;

    let messages = [
    { role: "assistant", text: "Halo! Aku ChatGPT mini buatan Aqil 😄" },
    { role: "assistant", text: "Silahkan Tanyakan Apapun yg anda mau Silahkan Tanyakan Apapun yg anda mau Silahkan Tanyakan Apapun yg anda mau Silahkan Tanyakan Apapun yg anda mau Silahkan Tanyakan Apapun yg anda mau Silahkan Tanyakan Apapun yg anda mau Silahkan Tanyakan Apapun yg anda mau Silahkan Tanyakan Apapun yg anda mau" }
     ];

    let input = "";

    const adjustHeight = () => {
        if(textarea) {
            textarea.style.height = "auto";
            textarea.style.height = `${textarea.scrollHeight}px`;
        }
    }

    onMount(() => {
        adjustHeight()
    })

    const handleInput = () => {
        adjustHeight()
    }

    function sendMessage() {
        if (!input.trim()) return;
        messages = [...messages, { role: "user", text: input }];
        input = "";
        adjustHeight()
        // nanti di sini kita hubungkan ke FastAPI
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
    }

    .messages {
        flex: 1;
        overflow-y: auto;
        margin-bottom: 1rem;
    }

    .message {
        margin: 0.5rem 0;
        padding: 0.75rem;
        border-radius: 8px;
        max-width: 80%;
        word-wrap: break-word;
    }

    .user {
        background: #2563eb;
        align-self: flex-end;
    }

    .assistant {
        background: #ff7b7b;
        align-self: flex-start;
    }

    .chat-input{
        bottom: 5vh;
        display: flex;
        flex-direction: row;
        width: 80%;
        height: 5vh;
        align-items: flex-end;
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
</style>

<div class="chat-container">
    <div class="chat-output">
        {#each messages as m}
        <div class="message {m.role}">
            <strong>{m.role === "user" ? "Kamu" : "Asisten"}:</strong> 
            {m.text}
        </div>
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
        <button on:click={sendMessage}>Send</button>
    </div>
</div>