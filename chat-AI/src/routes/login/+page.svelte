<style>
    .login-container{
        background-color:rgb(55, 55, 55);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 95vh;
        width: 100%;
    }

    .login{
        padding-top: 5%;
        background-color: rgb(255, 255, 255);
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 40%;
        height: 60vh;
        border-radius: 20px;
    }

    .form-login{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 80%;
    }

    .form-login ::placeholder{
        color: rgb(219, 205, 234);
    }

    input{
        margin: 10px;
        padding: 10px;
        width: 100%;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        background-color: rgb(55, 55, 55);
        color: white;
    }
    button{
        margin: 10px;
        padding: 10px;
        width: 50%;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        background-color: rgb(55, 55, 55);
        color: white;
    }

    .login-alternatif{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
</style>

<div class="login-container">
    <div class="login">
        <h2>Login</h2>
        <form class="form-login" action="/login" method="post">
            <input placeholder="Masukkan Username"/>
            <input placeholder="Masukkan Password"/>
        </form>
        <button>Login</button>
        <div class="login-alternatif">
            <p>Belum Punya Akun? <a href="/register">Register</a></p>
            <button>Masuk langsung dengan Gmail</button>
        </div>
    </div>
</div>