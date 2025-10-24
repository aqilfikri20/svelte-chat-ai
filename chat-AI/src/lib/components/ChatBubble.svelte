<script>
  export let role; // "user" atau "assistant"
  export let text;
  
</script>

<style>
  .bubble {
    margin: 0.5rem 0;
    padding: 0.75rem 1rem;
    border-radius: 12px;
    max-width: 80%;
    word-wrap: break-word;
    line-height: 1.5;
    font-size: 0.95rem;
  }

  .user {
    background: #2563eb;
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 0;
  }

  .assistant {
    background: #444;
    color: #f1f5f9;
    align-self: flex-start;
    border-bottom-left-radius: 0;
  }

</style>

<div class="bubble {role}">
  {text}
</div>
