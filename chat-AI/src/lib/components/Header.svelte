<script lang="ts">
	let open = false;
	let theme = "Sistem";

	function toggleDropdown() {
		open = !open;
	}

	function setTheme(t: string) : void {
		theme = t;
		open = false;
        if (typeof document !== "undefined") {
			document.documentElement.setAttribute("data-theme", t.toLowerCase());
		}
	}

</script>

<style>
    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        border-bottom: #ff0f0f 1px solid;
        height: 5vh;
    }

    .navbar-left{
        display: flex;
        margin-left:10px ;
        flex-direction: row;
        background-color: aqua;
        height: 100%;
        gap: 10px;
    }
    .navbar-right{
        display: flex;
        flex-direction: row;
        margin-right:15px ;
    }

    a{
        text-decoration: none;
    }

    a:visited{
        color: inherit;
    }

    .header a, 
    .header button {
	display: flex;
	align-items: center;
	justify-content: center;
	height: 100%;
    width: 50px;
    background-color: tomato;
    }

    a:hover{
        color: blue;
    }
    a{
        cursor: pointer;
    }   

	.dropdown {
        display: flex;
        align-items: center;
        justify-content: center;
		position: relative;
        width: 100%;
	}

    .dropdown button{
        background-color: #ff0f0f;
        border: none;
        color: white;
        font-size: 1rem;
        border-radius: 5px;
        height: 100%;
        width: 100%;
    }   
	.dropdown-btn {
		cursor: pointer;
	}
	.dropdown-menu {
		position: absolute;
		top: 100%;
		left: 0;
		background: white;
		box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
		border-radius: 8px;
		padding: 0.5rem;
		display: flex;
		flex-direction: column;
		z-index: 10;
	}
	.dropdown-menu button {
		padding: 0.3rem 0.7rem;
		text-decoration: none;
		color: black;
	}
	.dropdown-menu button:hover {
		background: #eee;
	}
</style>

<div class="header">
	<div class="navbar-left">
		<a href="/">CHAT-AI</a>
		<div class="dropdown">
			<button type="button"class="dropdown-btn" on:click={toggleDropdown}>Tema ▾</button>
            {#if open}
                <div class="dropdown-menu">
                    <button type="button" on:click={() => setTheme("Gelap")}>Gelap</button>
                    <button type="button" on:click={() => setTheme("Terang")}>Terang</button>
                    <button type="button" on:click={() => setTheme("Sistem")}>Sistem</button>
                </div>
            {/if}
		</div>
		<a href="/setting">Setting</a>
	</div>

	<div class="navbar-right">
		<a href="/login">Login</a>
	</div>
        
</div>