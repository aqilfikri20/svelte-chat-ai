<script lang="ts">
 import ChatBubble from "$lib/components/ChatBubble.svelte";
import { onMount, tick } from "svelte";

let textarea: HTMLTextAreaElement;
let messages = [
  { role: "assistant", text: "Halo! Selamat Datang 😄" },
  { role: "assistant", text: `dunia cerita mulai berubah. Di dalamnya hidup seseorang bernama Dian Saputra yang dikenal sebagai pedagang naga dan penjaga keamanan hutan. Ia memiliki kendali atas semua hal dengan hati-hati melalui perjalanan panjang menuju tempat itu untuk mengumpulkan para pengembara dari wilayah lain. Banyak orang menyadari pentingnya menjalankan misi mereka sendiri demi mempertahankan kebenaran terhadap sistem lama tersebut. Setiap hari diadakan pertemuan besar antar tokoh agar dapat membantu menemukan jalan keluar bagi anggota keluarga atau masyarakat kecil.

Beberapa tahun kemudian, sistem lama yang dibangun secara diam-diam berubah. Para pengembara muda berkumpul untuk mencari jalan keluar dari dunia fantasi mereka sendiri dan memperbaiki keadaan agar tidak terjadi konflik besar antar wilayah kecil atau masyarakat biasa. Dian memiliki kemampuan menjaga keseimbangan alam dengan mengikuti perintahnya sebagai penjaga jalur energi Naga Terbang yang selama ini dikendalikan para pedagang naga tersebut. Ia juga memahami pentingnya memastikan semua orang hidup dalam harmoni bersama demi menyelamatkan masa depan keluarga mereka. Ketika proses itu hampir mencapai puncaknya, banyak tokoh lain menyadari bahwa keberanian adalah cara terbaik bagi manusia menentukan arah keputusan melalui keberhasilan individu masing-masing.

sistem lama yang dibangun oleh para pedagang naga berhasil diperbaiki. Para pengembara muda dari wilayah lain mengambil keputusan untuk mencari jalan keluar dengan cara mereka sendiri dan menciptakan keseimbangan baru dalam dunia fantasi tersebut. Dian memutuskan tidak lagi menjalankan misinya sebagai penjaga jalur energi Naga Terbang atau memberikan bantuan kepada keluarga kecil terdekat agar bisa menyelamatkan masa depan bersama. Ia juga mempertimbangkan pentingnya keberanian individu demi memastikan keharmonisan antar masyarakat dapat terjalin harmonis secara bertahap.

para pengembara muda dari wilayah lain memutuskan untuk mengambil keputusan bersama. Mereka memilih menjalankan misinya dengan cara yang sama dan menciptakan keseimbangan baru dalam dunia fantasi mereka sendiri. Dian berhasil membantu keluarga kecilnya menyelamatkan Naga Terbang di masa depan melalui bantuan pribadi atau memperbaiki jalur energi naga secara diam-diam demi keselamatan hidup masyarakat tersebut. Ia juga menemukan banyak orang terluka saat proses perbaikan itu tidak dapat dihindari lagi. Beberapa tokoh lainnya menyadari pentingnya keberanian individu sebagai simbol kebersamaan antar manusia agar harmoni bisa terjaga kembali selama ini.

seluruh masyarakat yang terlibat dalam proses perbaikan memutuskan untuk mengambil keputusan bersama. Para pengembara muda berkumpul di desa-desa kecil dan memperbaiki jalur energi Naga Terbang dengan cara mereka sendiri agar tidak ada konflik besar lagi antar wilayah tersebut. Beberapa orang mencoba membantu Dian menjaga sistem lama sebagai penjaga atau menemukan jalan keluar dari masalah itu secara diam-diam demi menyelamatkan masa depan keluarganya. Ketika para pedagang naga kembali bekerja sama pada awal tahun ini, banyak anggota kelompok lain menyadari pentingnya keberanian individu bagi memahami realitas dunia fantasi melalui metode baru yang dapat membuka keseimbangan hidup manusia selama generasi berikutnya.

seluruh kelompok pengembara muda kembali bekerja sama dengan cara yang mereka pilih. Dian berhasil memperbaiki jalur energi Naga Terbang dan mengembalikan kestabilan sistem lama kepada masyarakatnya melalui metode baru di mana setiap orang dapat menjaga keseimbangan dunia fantasi bersama dalam situasi darurat. Ia juga memutuskan untuk meninggalkan tempat itu demi menyelamatkan keluarga kecil dari tragedi besar tersebut. Keputusan ini membuka jalan bagi banyak pihak agar tidak ada lagi konflik antar wilayah lain terjadi. Para pedagang naga kini memahami pentingnya keberanian individu sebagai simbol kebersamaan manusia selama generasi berikutnya.

seluruh kelompok pengembara muda berkumpul kembali untuk memahami realitas dunia fantasi. Para pedagang naga memutuskan bekerja sama dengan Dian dan mengambil keputusan bersama dalam menghadapi situasi darurat yang terjadi di wilayah lain melalui metode baru mereka sendiri. Sistem tersebut tidak lagi berada pada kondisi lama atau konflik besar antar masyarakat secara diam-diam. Ketika sistem Naga Terbang benar-benar stabil, para anggota keluarganya bisa meninggalkan tempat itu demi menyelamatkan masa depan generasinya. Banyak orang menyadari pentingnya keberanian individu sebagai simbol kebersamaan manusia selama ini.

Setelah kejadian itu, sistem Naga Terbang kembali stabil dan tidak lagi terjadi konflik besar antar wilayah. Para pedagang naga berkumpul untuk mempelajari cara kerja mereka sendiri dalam menghadapi situasi darurat yang sebelumnya dianggap sebagai masalah kecil bagi masyarakatnya. Dian mencoba membantu keluarganya menjaga jalur energi tersebut dengan memperbaikinya secara diam-diam agar semua orang dapat menerima kebaikan bersama melalui metode baru ini. Ia juga mengambil keputusan penting demi menyelamatkan masa depan generasinya dari tragedi besar tersebut. Ketika para anggota kelompok pengembara muda menyadari bahwa keberanian adalah fondasi kebenaran selama banyak tahun.

Setelah kejadian itu, sistem Naga Terbang kembali stabil dan masyarakat tidak lagi memiliki masalah besar. Para pedagang naga berkumpul untuk mempelajari cara kerja mereka sendiri dengan mempertimbangkan bahwa keberanian adalah fondasi kebenaran yang selama ini dianggap sebagai simbol kebersamaan manusia dalam dunia fantasi. Dian menyadari pentingnya menjaga jalur energi agar semua orang bisa hidup bersama melalui kebaikan masing-masing secara kolektif. Ia juga menemukan jalan keluar bagi para anggota keluarganya dari situasi darurat tersebut demi menyelamatkan masa depan generasinya.

Beberapa tahun kemudian, sistem Naga Terbang kembali stabil dan masyarakat tidak lagi dianggap sebagai simbol ketidakadilan. Para pedagang naga yang sebelumnya mengalami masalah besar kini memiliki cara baru untuk menjaga jalur energi mereka sendiri dengan memperbaiki kerusakan kecil dalam wilayah tersebut. Dian mencoba membantu keluarganya agar dapat bertahan hidup bersama melalui metode ini demi menyelamatkan masa depan generasi berikutnya. Ia menyadari bahwa keberanian adalah fondasi kebenaran bagi semua orang selama banyak tahun. Ketika situasi darurat terjadi, para anggota kelompok pengembara muda memahami pentingnya kebaikan dari setiap individu.
  ` }
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

  const context = messages.slice(-8); 

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
        background: var(--background);
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

    button{
        margin: 0;
        border-radius: 0px 10px 10px 0px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        background-color: rgb(55, 55, 55);
        color: white;
        border: white 3px solid;
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