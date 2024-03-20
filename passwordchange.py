#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")

import cgi

f = cgi.FieldStorage()
receiver = str(f.getvalue("receiver"))
encription = str(f.getvalue("session"))
fisrtNumber = str(f.getvalue("first-number"))
secondNumber = str(f.getvalue("second-number"))
thirdNumber = str(f.getvalue("third-number"))
fourthNumber = str(f.getvalue("fourth-number"))

OTPforValidation = fisrtNumber + secondNumber + thirdNumber + fourthNumber

j = 0
encription1 = encription.replace("aql","")
encription2 = ""
while j < len(encription1):
    if encription1[j] == "g":
        encription2 = encription2 + "0"

    elif encription1[j] == "j":
        encription2 = encription2 + "1"
        
    elif encription1[j] == "r":
        encription2 = encription2 + "2"
        
    elif encription1[j] == "w":
        encription2 = encription2 + "3"
        
    elif encription1[j] == "z":
        encription2 = encription2 + "4"
        
    elif encription1[j] == "b":
        encription2 = encription2 + "5"
        
    elif encription1[j] == "m":
        encription2 = encription2 + "6"
        
    elif encription1[j] == "p":
        encription2 = encription2 + "7"
        
    elif encription1[j] == "t":
        encription2 = encription2 + "8"
        
    elif encription1[j] == "f":
        encription2 = encription2 + "9"
        
    j += 1

if OTPforValidation == encription2:
    target = f.getvalue("target")

    if target == "shop.py":
        fullname = f.getvalue("fullname")
        fullname = fullname.replace(" ","+")
        email = f.getvalue("email")
        number = f.getvalue("number")
        password = f.getvalue("password")
        print('<html>')
        print('  <head>')
        print(' <meta http-equiv="refresh" content=0;url="registration.py?fullname=%s&email=%s&number=%s&password=%s"/>'%(fullname,email,number,password)) 
        print('  </head>')
        print('</html>')


    elif target == "bookingaconsultant.py":
        fullname = f.getvalue("fullname")
        fullname = fullname.replace(" ","+")
        email = f.getvalue("email")
        phoneNumber = f.getvalue("phoneNumber")
        address = f.getvalue("address")
        address = address.replace(" ","+")
        pincode = f.getvalue("pincode")
        landmark = f.getvalue("landmark")
        landmark = landmark.replace(" ","+")
        business_type = f.getvalue("business_type")

        print('<html>')
        print('  <head>')
        print('  <meta http-equiv="refresh" content=0;url="validate_user.py?target=%s&fullname=%s&email=%s&phoneNumber=%s&address=%s&pincode=%s&landmark=%s&business_type=%s"/>'%(target,fullname,email,phoneNumber,address,pincode,landmark,business_type)) 
        print('  </head>')
        print('</html>')

    else:
        try:
            print("""
    <!DOCTYPE html>
    <html lang="en" >

    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forget Password</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap" rel="stylesheet">
    <script type="text/javascript">
        function preventBack() { window.history.forward(); }
        setTimeout("preventBack()", 0);
        window.onunload = function () { null };
    </script>
    <style>
        * {
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }

        #user-credentials {
            margin: 102px auto;
            width: 400px;
            display: flex;
            flex-direction: column;
        }


        h3 {
            font-size: 2rem;
            font-family: 'Roboto';
            font-weight: bold;
            margin: 17px auto;
        }

        p {
            margin: auto;
            width: 349px;
            text-align: center;
            font-size: 18px;
            color: grey;
            font-family: emoji;
        }

        form {
            display: flex;
            flex-direction: column;
            width: 75%;
            margin: 31px auto;
        }

        .input {
            margin: 5px 0px;
            padding: 8px;
            outline: none;
            border: 2px solid #24a0ed;
        }

        span {
            display: none;
            color: red;
            font-family: monospace;
            font-size: 15px;
            font-weight: bold;
        }

        button {
            width: 75%;
            margin: -6px auto;
            height: 36px;
            font-weight: bold;
            color: white;
            background: #24a0ed;
            border: none;
            outline: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #7db4e3;
        }

        .red {
            border-color: red;
        }

        .hide {
            display: inline;
        }
    </style>

    </head>

    <body >
    <div id="user-credentials">
        <h3>Create new password</h3>
        <p>Your password must have atleast 8 characters</p>
        <form action="updatepassword.py">

            <input type="password" placeholder="Create new password" id="password" pattern="^\S*$" title="Password Cannot Contain Whitespaces.." minlength="8" maxlength="15" value="" class="input "
                name="password" required>

            <input type="password" placeholder="Re-enter your password" id="confirm-password" pattern="^\S*$" title="Password Cannot Contain Whitespaces.." value="" maxlength="15" class="input" name="user_input"
                required>
            <input type="hidden" name="receiver" value="""""+receiver+""">
            <input type="submit" id="submit" style="display: none;" value="submit">
            <span id="nouser">Password did not match.</span>

            <!-- <button>Save password</button> -->
        </form>
        <button>Save password</button>
    </div>
    </body>
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
    crossorigin="anonymous"></script>
    <script>
    $("button").click(function(){
        if ($("#password").val() == $("#confirm-password").val()){
            $("#submit").click()
        }
        else{
            $("#nouser").addClass("hide")
            $("#confirm-password").addClass("red")
        }
    })
    $("#confirm-password").focus(function(){
        $("#confirm-password").removeClass("red")
    })

    $(".input").click(function () {
        $(".input").removeClass("red")
        $("#nouser").removeClass("hide")
    })
    </script>

    </html>""")
        except Exception as e:
            print(e)
elif OTPforValidation != encription2:
    target = f.getvalue("target")
    email = f.getvalue("email")
    if target == None or target == "None":
        target = "forgetpassword.py"
    if target != "shop.py":
        if email == "None" or email == None:
            email = receiver

    print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Failed</title>
    <style>
        *{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }
        body{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        img {
    height: 435px;
    
}
h2 {
    text-align:center;
    color: rgb(255,114,92);
    font-size: 2rem;
}
a {
    text-decoration: none;
    background: rgb(255,114,92);
    height: 34px;
    width: 112px;
    margin-top: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    cursor: pointer;
    border-radius: 4px;
    font-weight: bold;
    text-transform: uppercase;
}
    </style>
</head>
<body>
    <img src="images/help.jpg" alt="">
    <h2>Invalid OTP</h2>
    <a href="%s?username=%s">Try Again</a>   
</body>
</html>"""%(target,email))