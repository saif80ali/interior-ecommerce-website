#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
f = cgi.FieldStorage()
login_status = f.getvalue("msg")
msg3 = f.getvalue("msg3")
user = f.getvalue("user")
passwd = f.getvalue("passwd")
username = f.getvalue("username")
user_id = 0
if login_status == "abc":
    login_status = "yes"

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ContactUs</title>
    <script src="https://kit.fontawesome.com/a7f7913510.js" crossorigin="anonymous"></script>
    <!-- logo font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Zen+Tokyo+Zoo&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:wght@300&display=swap" rel="stylesheet">
    <!-- logo font -->
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:wght@300&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="Home.css">
    <link rel="stylesheet" href="homeMedia.css">
    <style>
        #contact-section::before {
            content: '';
            opacity: 0.9;
            position: absolute;
            height: 64vh;
            width: 100vw;
            background-image: url(images/contactus_background.jfif);
            background-position: center, center;
            background-size: cover;
            background-color: rgba(0, 0, 0, 0.7);
            background-blend-mode: darken;
        }

        #contact-section {
            height: 64vh;
            display: flex;
            flex-direction: column;
            z-index: 1;
            align-items: center;
            justify-content: center;

        }

        #contact-section h1 {
            text-transform: uppercase;
            z-index: 1;
            font-size: 4rem;
            max-width: 678px;
            text-align: center;
            color: whitesmoke;
        }

        p {
            color: white;
            font-family: 'Open Sans Condensed';
            margin-bottom: 8px;
            max-width: 56%;
            font-size: 20px;
            z-index: 1;
            text-align: center;
            margin-top: 17px;
            min-width: 403px;
        }

        #consultant {
            z-index: 1;
            height: 49px;
            width: 300px;
            cursor: pointer;
            outline: none;
            background: black;
            color: white;
            font-weight: bold;
            border: none;
            margin-bottom: 8px;
        }

        #contact-caption {
            z-index: 1;
            align-items: center;
            justify-content: center;
            display: flex;
            flex-direction: column;
        }

        #contact-details {
            background: black;
            align-items: center;
            display: flex;
            color: white;
            justify-content: space-between;
            flex-wrap: wrap;
            min-height: 21.5vh;
            font-family: sans-serif;
            cursor: pointer;
        }

        .contact-info {
            width: 38%;
            margin: 8px;
            margin-left: 12px;
        }

        .contact-info i {
            font-size: 1.5rem;
        }

        .contact-info span {
            margin-left: 12px;
            font-size: 19px;
            font-weight: bold;
        }

    </style>
</head>

<body>
    <header>
        <div id="logo">
            <span class="MF">I</span><span class="predicate">ndian</span>
            <span class="MF">C</span><span class="predicate">abinet</span>
            <span class="MF">W</span><span class="predicate">orks</span>
        </div>
        <div id="buttons">
        """)
if login_status != "yes":
    print("""
            <button class="btn signup" onclick="showing()">Sign Up</button>
            <button class="btn login" onclick="showing1()">Log In</button>""")
elif login_status == "yes":
    print("""<button  class="btn login" onclick="logout()" >Log Out</button>""")
    login_status = "abc"

print("""
        </div>
    </header>
    <nav>
        <div id="burger">
            <div class="burger-slice"></div>
            <div class="burger-slice"></div>
            <div class="burger-slice"></div>
        </div>
        <ul>
            <li><a href="Home.py?msg=%s&username=%s" class="a navigation"> Home</a></li>
            <li><a href="" class="a navigation">Our Projects</a> </li>
            <li><a href="shop.py?msg=%s&username=%s" class="a navigation">Shop</a> </li>
            <li><a href="" class="a active">Contact Us</a> </li>
            <li><a href="" class="a navigation">Help</a> </li>
        </ul>
    </nav>
    <div class=" hiding">
        <form action="sendingmail.py" class="form1">
            <img src="images/outline_close_black_24dp.png" id="cross" onclick="hiding()" alt="" srcset="">
            <h2 class="signup">SIGN UP</h2>
            <input type="text" placeholder="Enter Full Name.." name="fullname" class="input" pattern="[a-zA-Z ]+" title="Name must contain only alphabets." required>
            <input type="email" placeholder="Enter Your Email.." name="email" class="input" required>
            <input type="text" placeholder="Enter Phone Number.." name="number" maxlength="10" minlength="10" pattern="[0-9]{10}" class="input" title="Enter correct phone number" required >
            <input type="password" placeholder="Create Password.." pattern="^\S*$" title="Password Cannot Contain Whitespaces.." minlength="8" name="password" maxlength="15" id="password" class="input" required>
            <input type="hidden" name="target" value='shop.py'>
            <div id="bekaar-div"><input type="checkbox" name="" class="check" id="show-pass"><label for="show-pass">Show Password</label></div>
            <input type="submit" value="SUBMIT" class="button">
        </form>
    </div>"""%(login_status,username,login_status,username))

if msg3 == "failed":
    print("""
    <div class="signup-form1">
        <form action="user_login.py" class="form2">
            <img src="images/outline_close_black_24dp.png" id="cross" onclick="hiding1()" alt="" srcset="">
            <h2 class="signup">LOG IN</h2>
            <input type="email" placeholder="Enter Your Email.." value="%s" name="username" class="input red" required>
            <input type="password" placeholder="Enter Your Password.." name="password" pattern="^\S*$" title="Password Cannot Contain Whitespaces.." id="password1" value="%s" minlength="8" maxlength="15" class="input red" required>
            <input type="hidden" name="target" value="contactUs.py">
            <span id="nouser">Invalid Credentials.</span>
            <div id="bekaar-div"><input type="checkbox" name="" class="check" id="show-pass1"><label for="show-pass1">Show Password</label><span><a href="forgetpassword.py" class="forget-password">Forget Password?</a></span></div> 
            <input type="submit" value="LOG IN" class="button">
        </form>
    </div>
    """%(user,passwd))
else:
    print("""
    <div class="hiding1">
        <form action="user_login.py" class="form2">
            <img src="images/outline_close_black_24dp.png" id="cross" onclick="hiding1()" alt="" srcset="">
            <h2 class="signup">LOG IN</h2>
            <input type="email" placeholder="Enter Your Email.."  name="username" class="input" required>
            <input type="password" placeholder="Enter Your Password.." pattern="^\S*$" title="Password Cannot Contain Whitespaces.." name="password" id="password1" minlength="8" class="input" required>
            <input type="hidden" name="target" value="ContactUs.py">
            <div id="bekaar-div"><input type="checkbox" name="" class="check" id="show-pass1"><label for="show-pass1">Show Password</label><span><a href="forgetpassword.py" class="forget-password">Forget Password?</a></span></div> 
            <input type="submit" value="LOG IN" class="button">
        </form>
    </div>""")
print("""    
    <section id="contact-section">
        <div id="contact-caption">
            <h1>Good designs for good moments</h1>
            <p>Giving Your home a new style. We provide such interiors designs that compliments customers style,
                requirement
                and budget. being the emboidment of your choice, your home is the reflection of you and your identity.
            </p>
        </div>
        <button id="consultant">BOOK AN CONSULTANT</button>
    </section>
    <div id="contact-details">
        <div class="contact-info"><i class="fa fa-phone" aria-hidden="true" style="    transform: rotate(
            108deg
            );"></i><span> - 6291599480</span></div>
        <div class="contact-info"><i class="fa fa-whatsapp" aria-hidden="true"></i><span> - 8013051576</span></div>
        <div class="contact-info"><i class="fa fa-instagram" aria-hidden="true"></i><span> - saifali_fias</span></div>
        <div class="contact-info"><i class="fa fa-facebook-official" aria-hidden="true"></i><span> - saifali_fias</span>
        </div>
        <div class="contact-info"><i class="fa fa-map-marker" aria-hidden="true"></i><span> - 300 BIPIN BEHARI GANGULY
                STREET, KOLKATA - 700012</span></div>
    </div>

</body>
<script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
    crossorigin="anonymous"></script>
<script src="home1.js"></script>
<script>
$("#consultant").click(function(){
    window.open("bookingaconsultant.py?msg=%s&username=%s","_parent")
})
</script>

</html>"""%(login_status,username))