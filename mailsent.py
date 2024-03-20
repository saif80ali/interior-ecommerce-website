#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
f = cgi.FieldStorage()

target = f.getvalue("target")
session = f.getvalue("session")

if target == "shop.py":
    fullname = f.getvalue("fullname")
    fullname = fullname.replace(" ","+")
    email = f.getvalue("email")
    name = fullname
    name = name.replace("+"," ") 
    receiver = email
    number = f.getvalue("number")
    password = f.getvalue("password")
    
elif target == "bookingaconsultant.py":
    fullname = f.getvalue("fullname")
    fullname = fullname.replace(" ","+")
    name = fullname
    name = name.replace("+"," ")
    email = f.getvalue("email")
    receiver = email
    phoneNumber = f.getvalue("phoneNumber")
    address = f.getvalue("address")
    address = address.replace(" ","+")
    pincode = f.getvalue("pincode")
    landmark = f.getvalue("landmark")
    landmark = landmark.replace(" ","+")
    business_type = f.getvalue("business_type")
else:
    receiver = f.getvalue("receiver")
    name = f.getvalue("name")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap" rel="stylesheet">
    <title>Mail Sent</title>
    <script type="text/javascript">
        function movetoNext(current, nextFieldID) {
            if (current.value.length >= current.maxLength) {
                document.getElementById(nextFieldID).focus();
            }
        }
        function preventBack() { window.history.forward(); }
        setTimeout("preventBack()", 0);
        window.onunload = function () { null };
    </script>
    <style>
        * {
            padding: 0px;
            margin: 0px;
            box-sizing: border-box;
        }

        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

        }

        #mail {
            margin-top: 18px;
        }

        h2 {
            font-family: roboto;
            margin: 12px auto;
            text-align: center;
            font-size: 2rem;
        }

        p {
            font-family: system-ui;
            color: grey;
            width: 400px;
            text-align: center;
            margin: auto;
            font-size: 16px;
        }

        form {
            text-align: center;
        }

        img {
            margin: auto;
            height: 302px;
            width: 500px;
        }

        span {
            color: rgb(255, 79, 90);
            margin: auto;
            font-size: 20px;
            font-family: sans-serif;
        }

        #input-boxes {
            display: flex;
            justify-content: center;
        }

        .input {
            color: gray;
            border: none;
            border-bottom: 4px solid #24a0ed;
            margin: 12px 5px;
            text-align: center;
            width: 42px;
            font-size: 3rem;
            outline: none;
        }

        #buttons {
            width: 347px;
            display: flex;
            justify-content: space-between;
            margin-top: 15px;
        }

        a {
            text-decoration: none;
            background: yellow;
            color: black;
            padding: 4px 8px;
        }

        button {
            background: #24a0ed;
            outline: none;
            cursor: pointer;
            color: white;
            border: none;
            width: 69px;
            font-weight: bold;
        }

        button:hover {
            background: #98c4df;
        }
    </style>
</head>

<body>
    <div id="mail">
        <h2>Email sent</h2>
        <p>An email containing your One Time password has been sent to your Email - %s .</p>
        <img src="images/mailsent.jpg">
    </div>
    <form action="passwordchange.py">
        <span>Enter your 4-digit OTP</span>
        <div id="input-boxes">
            <input type="text" id="first" class="input" name="first-number" onkeyup="movetoNext(this, 'second')"
                maxlength="1" minlength="1" pattern="[0-9]" title="Enter only number" required>
            <input type="text" id="second" class="input" name="second-number" onkeyup="movetoNext(this, 'third')"
                maxlength="1" minlength="1" pattern="[0-9]" title="Enter only number" required>
            <input type="text" id="third" class="input" name="third-number" onkeyup="movetoNext(this, 'fourth')"
                maxlength="1" minlength="1" pattern="[0-9]" title="Enter only number" required>
            <input type="text" id="fourth" class="input" name="fourth-number" maxlength="1" minlength="1"
                pattern="[0-9]" title="Enter only number" required>
            <input type="hidden" name="receiver" value="%s">
            <input type="hidden" name="session" value="%s">"""%(receiver,receiver,session))
if target == "shop.py":
    print("""
    <input type="hidden" name="target" value="%s">
    <input type="hidden" name="fullname" value="%s">
    <input type="hidden" name="email" value="%s">
    <input type="hidden" name="number" value="%s">
    <input type="hidden" name="password" value="%s">
    </div>
        <div id="buttons">
            <a href="sendingmail.py?target=%s&fullname=%s&email=%s&number=%s&password=%s">Resend OTP</a>
            <button type="submit">Next</button>
        </div>"""%(target,fullname,email,number,password,target,fullname,email,number,password))

elif target == "bookingaconsultant.py":
    print("""
    <input type="hidden" name="target" value="%s">
    <input type="hidden" name="fullname" value="%s">
    <input type="hidden" name="email" value="%s">
    <input type="hidden" name="phoneNumber" value="%s">
    <input type="hidden" name="address" value="%s">
    <input type="hidden" name="pincode" value="%s">
    <input type="hidden" name="landmark" value="%s">
    <input type="hidden" name="business_type" value="%s">
    </div>
        <div id="buttons">
            <a href="sendingmail.py?target=%s&fullname=%s&email=%s&phoneNumber=%s&address=%s&pincode=%s&landmak=%s&business_type=%s">Resend OTP</a>
            <button type="submit">Next</button>
        </div>"""%(target,fullname,email,phoneNumber,address,pincode,landmark,business_type,target,fullname,email,phoneNumber,address,pincode,landmark,business_type))

else:
    print("""
        </div>
        <div id="buttons">
            <a href="sendingmail.py?receiver=%s&name=%s">Resend OTP</a>
            <button type="submit">Next</button>
        </div>"""%(receiver,name))
        
print("""
    </form>
</body>
</html>""")