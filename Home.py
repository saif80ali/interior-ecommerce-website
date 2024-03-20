#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
f = cgi.FieldStorage()
login_status = f.getvalue("msg")
msg3 = f.getvalue("msg3")
user = f.getvalue("user")
passwd = f.getvalue("passwd")
username = f.getvalue("username")
if login_status == "abc":
    login_status = "yes"

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MFurnitures And Decorators</title>
    <!-- <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> -->
    <!-- logo font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Zen+Tokyo+Zoo&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:wght@300&display=swap" rel="stylesheet">
    <!-- logo font -->
    <link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="Home.css">
    <link rel="stylesheet" href="homeMedia.css">

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
            <li><a href="" class="a active"> Home</a></li>
            <li><a href="#about" class="a navigation">Services</a> </li>
            <li><a href="" class="a navigation">Our Projects</a> </li>
            <li><a href="shop.py?msg=%s&username=%s" class="a navigation">Shop</a> </li>
            <li><a href="contactUs.py?msg=%s&username=%s" class="a navigation">Contact Us</a> </li>
            <li><a href="" class="a navigation">Help</a> </li>
        </ul>
    </nav>
    <div id="container">
        <h1 id="tag-line">YOU DREAM <span class="inner-tagline">WE Design</span></h1>
        <div id="caption">Indian Cabinet Works ,<span id="since">Since 1987</span>. We decorate interiors for Home, Restaurants, Corporate Offices , Commercial Places and Hospitality Designs. Our in interior  designs can transfrom your space into the home of your <span style="color: black;
    font-size: 26px;
    font-weight: bold;">dreams.</span><span id="span2"> We provide customised solution and designs to make your home a striking beautiful home.</span></div>
    </div>
    <h2 class="key" id="">What We Design</h2>
    <div id="aminities">
        <div class="each-aminities"><div class="image"><img src="images/furniture.webp"></div>
            <p>Furniture</p>
            <h3>A perfect home we have made it our goal to provide you with the best quality furnitures. After all every piece of furniture has a story.</h3>
        </div>
        <div class="each-aminities"><div class="image"><img src="images/furnishing.jpeg"></div>
            <p>Furnishing and Decor Accessories</p>
            <h3>What are you waiting for? upgrade your home by adding final decorative touch to your house and make beautiful, elegant and stylish.</h3>
        </div>
        <div class="each-aminities"><div class="image"><img src="images/modular-kitchen.jpeg"></div>
            <p>Modular Kitchens</p>
            <h3>The modular kitchens are not only eye catching but also efficient in saving space. Why to leave it where a lot of time and effort is spenthere daily! Organise your cooking space with the theme of your house.</h3>
        </div>
        <div class="each-aminities"><div class="image"><img src="images/wallpaper.jpeg"></div>
            <p>Painting and Wallpaper</p>
            <h3>Give your house a vibrant hue by adding spark and spice up the decor game. Cover them with richy patterned wallpapers and paintings.</h3>
        </div>
        <div class="each-aminities"><div class="image"><img src="images/wardrobe.jpeg"></div>
            <p>Modular Wardrobes</p>
            <h3>Isn't it you always dreamt to decorate your wardrobe as per movie and your dream? Take it easy! customise your wardrobe in line with the budget and requirement. Waste minimum space and save every inch of your home. </h3>
        </div>
        <div class="each-aminities"><div class="image"><img src="images/lighting.jpg"></div>
            <p>Lighting</p>
            <h3>Upgrade your view by creating great lighting and bring new energy to an interior. Draw attention to your most impressive area and change the mood of the living space. </h3>
        </div>
    </div>
    <div id="services">
        <h2 class="key" id="about"><span class="title">Sevices</span>  We Do</h2>
        <div id="each-service">
            <div class="each-aminities"><div class="image shape"><img src="images/corporate design.jpg"   alt="" srcset=""></div><p class="white"><span class="title">Corporate </span><span class="white">Design</span></p><h3 class="white">Successful business sped time ensuring their offices are well designed. Make your place more warm and welcoming for corporate clients by our interior designs for professional workplaces.</h3></div>
            <div class="each-aminities"><div class="image"><img src="images/restraunt-design.jpeg"   alt="" srcset=""></div><p class="white"><span class="title">Restaurant </span><span class="white">Design</span></p><h3 class="white">Don't you know?! Your restraunt's interior designs impacts customers psychology and prompts them to order more or less. Thus, it also impacts the duration of their stay. Hurry! with our interior design make all the decorations play an integral role in defining the look and feel of your restaurant.</h3></div>
            <div class="each-aminities"><div class="image"><img src="images/launge-design.jpeg"   alt="" srcset=""></div><p class="white"><span class="title">Lounge </span><span class="white">Design</span></p><h3 class="white">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolorum quod mollitia assumenda molestias fugiat qui facilis, temporibus nostrum praesentium recusandae sequi tempora cum similique excepturi dolore dolorem esse officia sint?</h3></div>
            <div class="each-aminities"><div class="image"><img src="images/hospital-design.jpeg"   alt="" srcset=""></div><p class="white"><span class="title">Hospitality </span><span class="white">Design</span></p><h3 class="white">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolorum quod mollitia assumenda molestias fugiat qui facilis, temporibus nostrum praesentium recusandae sequi tempora cum similique excepturi dolore dolorem esse officia sint?</h3></div>
            <div class="each-aminities"><div class="image"><img src="images/commercial-design.jpeg"   alt="" srcset=""></div><p class="white"><span class="title">Commercial </span><span class="white">Design</span></p><h3 class="white">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolorum quod mollitia assumenda molestias fugiat qui facilis, temporibus nostrum praesentium recusandae sequi tempora cum similique excepturi dolore dolorem esse officia sint?</h3></div>
            <div class="each-aminities"><div class="image"><img src="images/residential-design.jpeg"   alt="" srcset=""></div><p class="white"><span class="title">Residential </span><span class="white">Design</span></p><h3 class="white">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolorum quod mollitia assumenda molestias fugiat qui facilis, temporibus nostrum praesentium recusandae sequi tempora cum similique excepturi dolore dolorem esse officia sint?</h3></div>

        </div>

    </div>
    <div class=" hiding">
        <form action="sendingmail.py" class="form1">
            <img src="images/outline_close_black_24dp.png" id="cross" onclick="hiding()" alt="" srcset="">
            <h2 class="signup">SIGN UP</h2>
            <input type="text" placeholder="Enter Full Name.." name="fullname" class="input" pattern="[a-zA-Z ]+" title="Name must contain only alphabets." required>
            <input type="email" placeholder="Enter Your Email.." name="email" class="input" required>
            <input type="text" placeholder="Enter Phone Number.." name="number" maxlength="10" minlength="10" pattern="[0-9]{10}" class="input" title="Enter correct phone number" required >
            <input type="hidden" name="target" value='shop.py'>
            <input type="password" placeholder="Create Password.." pattern="^\S*$" title="Password Cannot Contain Whitespaces.." minlength="8" name="password" maxlength="15" id="password" class="input" required>
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
            <input type="hidden" name="target" value="Home.py">
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
            <input type="hidden" name="target" value="Home.py">
            <div id="bekaar-div"><input type="checkbox" name="" class="check" id="show-pass1"><label for="show-pass1">Show Password</label><span><a href="forgetpassword.py" class="forget-password">Forget Password?</a></span></div> 
            <input type="submit" value="LOG IN" class="button">
        </form>
    </div>""")
print("""
    <div id="covid-safety">
        <h2 class="covid-caption"><img src="images/coronavirus.png" class="corona-img">COVID-19 Safety Standards</h2>
        <div id="covid-protocols">
            <div class="each-protocol"><img src="images/mask.png"><span>MASKS FOR EMPLOYEES</span></div>
            <div class="each-protocol"><img src="images/sanitize.png"><span>SANITIZATION OF LABOURS</span></div>
            <div class="each-protocol"><img src="images/labour.png"><span>REDUCED MANPOWER</span></div>
            <div class="each-protocol"><img src="images/cleanliness.png"><span>FREQUENT HAND WASH</span></div>
            <div class="each-protocol"><img src="images/temperatureCheck.png"><span>TEMPERATURE SCANNING</span></div>
        </div>
    </div>
</body>
<!-- <script src="jquery-3.5.1.min.js"></script> -->
<script
  src="https://code.jquery.com/jquery-3.6.0.js"
  integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
  crossorigin="anonymous"></script>
  <script src="home1.js"></script>

</html>
""")