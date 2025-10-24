<script>
  // State pesan dan input
  let messages = [
    { role: "assistant", text: "Halo! Aku ChatGPT mini buatan Aqil 😄" },
    { role: "assistant", text: "Silahkan Tanyakan Apapun yg anda mau" }
  ];
  let input = "";

  function sendMessage() {
    if (!input.trim()) return;
    messages = [...messages, { role: "user", text: input }];
    input = "";
    // nanti di sini kita hubungkan ke FastAPI
  }
</script>

<style>
  .chat-container {
    max-width: 600px;
    margin: 2rem auto;
    border: 1px solid #444;
    border-radius: 12px;
    padding: 1rem;
    background: #111;
    color: #eee;
    font-family: system-ui;
    height: 80vh;
    display: flex;
    flex-direction: column;
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
    background: #444;
    align-self: flex-start;
  }

  .input-box {
    display: flex;
    gap: 0.5rem;
  }

  input {
    flex: 1;
    padding: 0.75rem;
    border-radius: 8px;
    border: none;
  }

  button {
    padding: 0.75rem 1rem;
    background: #16a34a;
    border: none;
    border-radius: 8px;
    color: white;
    cursor: pointer;
  }
</style>

<div class="chat-container">
  <div class="messages">
    {#each messages as m}
      <div class="message {m.role}">
        <strong>{m.role === "user" ? "Kamu" : "Asisten"}:</strong> 
        {m.text}
      </div>
    {/each}
  </div>

  <div class="input-box">
    <input
      placeholder="Tulis pesan Anda Disini..."
      bind:value={input}
      on:keydown={(e) => e.key === "Enter" && sendMessage()}
    />
    <button on:click={sendMessage}>Kirim Pesan</button>
  </div>
</div>
