<script lang="ts">
    import {onMount} from "svelte";

    let message = "";
    let textarea: HTMLTextAreaElement;

    let messages = [
    { role: "assistant", text: "Halo! Aku ChatGPT mini buatan Aqil 😄" },
    { role: "assistant", text: "Silahkan Tanyakan Apapun yg anda mau" }
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
        background-color: aqua;
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 95vh;
    }
    .chat-output{ 
        display: flex;
        align-items: center;
        background-color: rgb(25, 2, 159);
        height: 90%;
        width: 80%;
    }

    .chat-input{
        bottom: 5vh;
        background-color: rgb(225, 127, 255);
        display: flex;
        flex-direction: row;
        width: 80%;
        height: 5vh;
        align-items: flex-end;
    }

    .text-input{
        flex: 1;
        background-color: antiquewhite;
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