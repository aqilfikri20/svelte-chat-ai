<script lang="ts">
  export let role; // "user" atau "assistant"
  export let text ;
function capitalizeSentences(text: string): string {
    return text.replace(
        /(^\s*[a-zà-ÿ]|[.!?]\s+[a-zà-ÿ])/g,
        (match: string) => match.toUpperCase()
    );
}
  
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
    color: var(--font-color);
    align-self: flex-end;
    border-bottom-right-radius: 0;
  }

.story {
  font-family: var(--app-font), sans-serif;
  font-size: var(--app-font-size);
  line-height: 1.7;
  text-align: justify;
  max-width: 700px;
}

.story p {
  margin-bottom: 1rem;
}

  .assistant {
    background: var(--assistant-bubble);
    color: var(--font-color);
    align-self: flex-start;
    border-bottom-left-radius: 0;
  }

</style>

<div class="bubble {role}">
<div class="story">
{#each capitalizeSentences(text).split('\n\n') as paragraph}
  <p>{paragraph}</p>
{/each}
</div>
</div>
