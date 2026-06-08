<script lang="ts">
import { jsPDF } from "jspdf";

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

function downloadPdf() {
    const doc = new jsPDF({
        orientation: "portrait",
        unit: "mm",
        format: "a4"
    });

    doc.setFont("times", "normal");
    doc.setFontSize(12);

    const content =
        capitalizeSentences(
            String(text ?? "")
        );

    const lines =
        doc.splitTextToSize(
            content,
            170
        );

    const pageHeight =
        doc.internal.pageSize.height;

    const marginTop = 20;
    const marginBottom = 20;
    const lineHeight = 7;

    let y = marginTop;

    for (const line of lines) {

        if (
            y >
            pageHeight -
            marginBottom
        ) {
            doc.addPage();
            y = marginTop;
        }

        doc.text(line, 20, y);

        y += lineHeight;
    }

    doc.save("story.pdf");
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
  margin-bottom: 1rem;
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
    margin-bottom: 30px;
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

</style>

<div class="bubble {role}">
    <div class="story">
        {#each capitalizeSentences(text).split('\n\n') as paragraph}
            <p>{paragraph}</p>
        {/each}
    </div>
</div>

{#if role === "assistant"}
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
{/if}
