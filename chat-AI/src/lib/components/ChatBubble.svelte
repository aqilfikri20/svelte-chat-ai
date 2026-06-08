<script lang="ts">
import html2pdf from "html2pdf.js";
let storyElement: HTMLDivElement | null = null;

  export let role; // "user" atau "assistant"
  export let text:any;
import { createEventDispatcher } from "svelte";

const dispatch = createEventDispatcher();

function regenerate() {
    dispatch("regenerate");
}

  async function copyText() {
    await navigator.clipboard.writeText(
    capitalizeSentences(text)
);
}

function capitalizeSentences(text: string): string {
    return text.replace(
        /(^\s*[a-zà-ÿ]|[.!?]\s+[a-zà-ÿ])/g,
        (match: string) => match.toUpperCase()
    );
}
async function downloadPdf() {
    if (!storyElement) return;

    const opt = {
        margin: 10,
        filename: "story.pdf",
        image: {
            type: "jpeg",
            quality: 1
        },
        html2canvas: {
            scale: 2,
            useCORS: true
        },
        jsPDF: {
            unit: "mm",
            format: "a4",
            orientation: "portrait"
        },
        pagebreak: {
            mode: ["css", "legacy"]
        }
    };

    await html2pdf()
        .from(storyElement)
        .save();
}

const fontMap: Record<string, string> = {
    "Arial": "helvetica",
    "Times New Roman": "times",
    "Courier New": "courier"
};


</script>

<style>
  .bubble {
      position: relative;
      padding: 1.2rem 1.2rem;
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

  .assistant {
    background: var(--assistant-bubble);
    color: var(--font-color);
    align-self: flex-start;
    border-bottom-left-radius: 0;
   margin: 0;
  }

.message-actions {
    display: flex;
    gap: 2px;
    margin-left: 8px;
    opacity: 0.8;
}
.action-btn {
    width: 28px;
    height: 28px;

    display: flex;
    align-items: center;
    justify-content: center;

    border: none;
    border-radius: 10px;

    background: transparent;
    color: var(--font-color);

    cursor: pointer;

    transition: all 0.15s ease;
}
.action-btn:hover {
    background: rgba(255,255,255,0.1);
}

.assistant-wrapper {
  margin-top: 30px;
  margin-bottom: 30px;
  display: flex;
  flex-direction: column;
  align-self: flex-start; /* rata kiri */
  width: 100%;
}

.message-actions {
  display: flex;
  gap: 2px;
  margin-left: 4px;   /* sedikit indent dari tepi bubble */
  margin-top: 2px;    /* jarak dari bubble ke tombol */
  opacity: 0.8;
}
</style>


{#if role === "assistant"}
  <div class="assistant-wrapper" >
    <div class="bubble {role} "bind:this={storyElement}>
      <div class="story">
        {#each capitalizeSentences(text).split('\n\n') as paragraph}
          <p>{paragraph}</p>
        {/each}
      </div>
    </div>

    <div class="message-actions">
      <button class="action-btn" on:click={copyText} title="Salin">📋</button>
      <button class="action-btn" on:click={downloadPdf} title="Download PDF">📥</button>
      <button class="action-btn" on:click={regenerate} title="Ulangi">🔄</button>
    </div>
  </div>
{:else}
  <div class="bubble {role}">
    <div class="story">
      {#each capitalizeSentences(text).split('\n\n') as paragraph}
        <p>{paragraph}</p>
      {/each}
    </div>
  </div>
{/if}