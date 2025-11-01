<script>

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
    gap:10px;
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

a:hover{
    color: blue;
}
a{
    cursor: pointer;
}   
</style>

<div class="header">
	<div class="navbar-left">
		<a href="/"><h4>CHAT-AI</h4></a>
		<a href="/tema">Tema</a>
		<a href="/setting">Setting</a>
	</div>

	<div class="navbar-right">
		<a href="/login">Login</a>
	</div>
        
</div>