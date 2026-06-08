<script lang="ts">
let pdfElement: HTMLDivElement | null = null;

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
    if (!pdfElement) return;
    const html2pdf =
        (await import("html2pdf.js")).default;


    await html2pdf()
        .set({
            margin: 0,
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
            }
        })
        .from(pdfElement)
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

.pdf-hidden {
    position: fixed;
    left: -99999px;
    top: 0;
}

.pdf-container {
    width: 210mm;
    min-height: 296.8mm;

    box-sizing: border-box;

    background: var(--assistant-bubble);
    color: var(--font-color);

    padding: 20mm;

    border-radius: 0;
}

.pdf-story {
    font-family: var(--app-font), sans-serif;

    font-size: var(--app-font-size);

    line-height: 1.8;

    text-align: justify;

    word-break: break-word;
}

.pdf-story p {
    margin-bottom: 1em;
}
</style>

{#if role === "assistant"}
<div class="assistant-wrapper">

    <!-- Bubble chat normal -->
    <div class="bubble assistant">
        <div class="story">
            {#each capitalizeSentences(text).split('\n\n') as paragraph}
                <p>{paragraph}</p>
            {/each}
        </div>
    </div>

    <div class="message-actions">
        <button
            class="action-btn"
            on:click={copyText}
            title="Salin"
        >
            📋
        </button>

        <button
            class="action-btn"
            on:click={downloadPdf}
            title="Download PDF"
        >
            📥
        </button>

        <button
            class="action-btn"
            on:click={regenerate}
            title="Ulangi"
        >
            🔄
        </button>
    </div>

</div>

<!-- Template khusus PDF -->
<div class="pdf-hidden">
    <div
        bind:this={pdfElement}
        class="pdf-container"
    >
        <div class="pdf-story">
            {#each capitalizeSentences(text).split('\n\n') as paragraph}
                <p>{paragraph}</p>
            {/each}
        </div>
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