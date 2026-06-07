<script>
  export let role; // "user" atau "assistant"
  export let text ;
  
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
    background: var(--user-bubble);
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 0;
  }

.story {
  font-family: var(--app-font), sans-serif;
  font-size: 14pt;
  line-height: 1.7;
  text-align: justify;
  color: #f8fafc;
  max-width: 700px;
}

.story p {
  margin-bottom: 1rem;
}

  .assistant {
    background: var(--assistant-bubble);
    color: #f1f5f9;
    align-self: flex-start;
    border-bottom-left-radius: 0;
  }

</style>

<div class="bubble {role}">
<div class="story">
  {#each text.split('\n\n') as paragraph}
    <p>{paragraph}</p>
  {/each}
</div>
</div>
