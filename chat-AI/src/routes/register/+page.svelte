<style>
    .register-container{
        background-color:rgb(55, 55, 55);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 95vh;
        width: 100%;
    }

    .register{
        padding-top: 3%;
        background-color: rgb(255, 255, 255);
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 40%;
        height: 80vh;
        border-radius: 20px;
    }

    .form-register{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 80%;
    }

    .verifikasi{
        display: flex;
        flex-direction: column;
        width: 100%;
    }


    .verifikasi button{
        margin-top: 5px;
        padding: 5px;
        border-radius: 10px;
        border: none;
        font-size: 14px;
        cursor: pointer;
        background-color: rgb(55, 55, 55);
        color: white;
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

    .button-submit{
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

        input::placeholder{
            color: rgb(219, 205, 234);
        }

        .radio-register{
            display: flex;
            align-items: center;
            gap: 30px;
        }

        .radio-register label{
            font-size: 18px;
            display: flex;
            align-items: center;
            cursor: pointer;
            line-height: 1.2;
            
        }

        .radio-register input[type="radio"] {
            vertical-align: middle;
            accent-color: rgb(55, 55, 55); 
            margin-right: 5px;
        }
</style>

<div class="register-container">
    <div class="register">
        <h2>Register</h2>`
        <form class="form-register">
            <input type="text" placeholder="Masukkan username"/>
            <input type="password" placeholder="Masukkan Password"/>
            <input type="password" placeholder="Konfirmasi Password"/>
            <div class="verifikasi">
                <p>Verifikasi dengan:</p>
                <div class="radio-register">
                    <label><input type="radio" name="verifikasi" value="email" checked/> Email</label>
                    <label><input type="radio" name="verifikasi" value="sms"/> SMS</label>
                </div>
                <button>Kirim Kode</button>
            </div>
            <input placeholder="Masukkan Kode verifikasi"/>

        </form>
        <button class="button-submit">Register</button>
        <p>Sudah Punya Akun? <a href="/login">Login</a></p>
    </div>
</div>