#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")

import cgi
import mysql.connector as mariadb
t = cgi.FieldStorage() 
searched_product = t.getvalue("searched-query")
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
    <link rel="stylesheet" href="home.css">
    <link rel="stylesheet" href="shop.css">""")
if searched_product == "dressing table" or searched_product == "wardrobe":
    print("""<link rel="stylesheet" href="shop1.css">""")
print("""
    <link rel="stylesheet" href="homeMedia.css">
    <!-- logo font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Zen+Tokyo+Zoo&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:wght@300&display=swap" rel="stylesheet">
    <!-- logo font -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div id="logo">
            <span class="MF">I</span><span class="predicate">ndian</span>
            <span class="MF">C</span><span class="predicate">abinet</span>
            <span class="MF">W</span><span class="predicate">orks</span>
        </div>
        <div id="buttons">""")
if login_status != "yes":
    print("""
            <button class="btn signup" onclick="showing()">Sign Up</button>
            <button class="btn login" onclick="showing1()">Log In</button>""")
elif login_status == "yes":
    print("""<button class="btn login" onclick="logout()"">Log Out</button>""")
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
            <li><a href="" class="a active">Shop</a> </li>
            <li><a href="contactUs.py?msg=%s&username=%s" class="a navigation">Contact Us</a> </li>
            <li><a href="" class="a navigation">Help</a> </li>
        </ul>
    </nav>
    <div class=" hiding">
        <form action="sendingmail.py" class="form1">
            <img src="images/outline_close_black_24dp.png" id="cross" onclick="hiding()" alt="" srcset="">
            <h2 class="signup">SIGN UP</h2>
            <input type="text" placeholder="Enter Full Name.." name="fullname" class="input" required>
            <input type="email" placeholder="Enter Your Email.." name="email" class="input" required>
            <input type="text" placeholder="Enter Phone Number.." pattern="[0-9]{10}" name="number" maxlength="10" minlength="10" class="input" required >
            <input type="hidden" name="target" value='shop.py'>
            <input type="password" placeholder="Create Password.." name="password" pattern="^\S*$" title="Password Cannot Contain Whitespaces.." id="password" maxlength="15" class="input" required>
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
            <input type="hidden" name="target" value="shop.py">
            <span id="nouser">Invalid Credentials.</span>
            <div id="bekaar-div"><input type="checkbox" name="" class="check" id="show-pass1"><label for="show-pass1">Show Password</label><span><a href="forgetpassword.py" class="forget-password">Forget Password?</a></span></div> 
            <input type="submit" value="LOG IN" class="button">
        </form>
    </div>"""%(user,passwd))
else:
    print("""
    <div class="hiding1">
        <form action="user_login.py" class="form2">
            <img src="images/outline_close_black_24dp.png" id="cross" onclick="hiding1()" alt="" srcset="">
            <h2 class="signup">LOG IN</h2>
            <input type="email" placeholder="Enter Your Email.."  name="username" class="input" required>
            <input type="password" placeholder="Enter Your Password.." name="password" pattern="^\S*$" title="Password Cannot Contain Whitespaces.." id="password1" minlength="8" class="input" required>
            <input type="hidden" name="target" value="shop.py">
            <div id="bekaar-div"><input type="checkbox" name="" class="check" id="show-pass1"><label for="show-pass1">Show Password</label><span><a href="forgetpassword.py" class="forget-password">Forget Password?</a></span></div> 
            <input type="submit" value="LOG IN" class="button">
        </form>
    </div>""")

print("""
    <section id="seacrh-conatiner">
        <div class="seacrh-boxes" onclick="searched_item('beds')"><img src="images/beds.png" alt="failed to download image" srcset=""><span class="text">BEDS</span></div>
        <div class="seacrh-boxes" onclick="searched_item('tables')"><img src="images/chairs.png" alt="failed to download image" srcset=""><span class="text">TABLES/CHAIRS</span></div>
        <div class="seacrh-boxes" onclick="searched_item('drawers')"><img src="images/chest-of-drawers.png" alt="failed to download image" srcset=""><span class="text">CHEST OF DRAWERS</span></div>
        <div class="seacrh-boxes" onclick="searched_item('dining sets')"><img src="images/dining_table.png" alt="failed to download image" srcset=""><span class="text">DINING SETS</span></div>
        <div class="seacrh-boxes" onclick="searched_item('dressing table')"><img src="images/dressing-table.png" alt="failed to download image" srcset=""><span class="text">DRESSING TABLE</span></div>
        <div class="seacrh-boxes" onclick="searched_item('false ceiling')"><img src="images/false-ceiling.png" alt="failed to download image" srcset=""><span class="text">FALSE CEILING</span></div>
        <div class="seacrh-boxes" onclick="searched_item('kitchen')"><img src="images/kitchen-set.png" alt="failed to download image" srcset=""><span class="text">KICTHEN SETS</span></div>
        <div class="seacrh-boxes" onclick="searched_item('wardrobe')"><img src="images/wardrobe.png" alt="failed to download image" srcset=""><span class="text">Wardrobes</span></div>
        <div class="seacrh-boxes" onclick="searched_item('shoe rack')"><img src="images/shoerack.png" alt="failed to download image" srcset=""><span class="text">SHOE RACKS</span></div>
        <div class="seacrh-boxes" onclick="searched_item('sofa')"><img src="images/sofa.png" alt="failed to download image" srcset=""><span class="text">SOFA</span></div>
        <div class="seacrh-boxes" onclick="searched_item('tv unit')"><img src="images/TV-unit.png" alt="failed to download image" srcset=""><span class="text">TV UNITS</span></div>
        <div class="seacrh-boxes" onclick="searched_item('study table')"><img src="images/study-table.png" alt="failed to download image" srcset=""><span class="text">STUDY TABLE</span></div>
        <div class="seacrh-boxes" onclick="searched_item('bathroom')"><img src="images/bathroom.png" alt="failed to download image" srcset=""><span class="text">BATHROOM</span></div>
        <div class="seacrh-boxes" onclick="searched_item('prayer room')"><img src="images/prayerroom.png" alt="failed to download image" srcset=""><span class="text">PRAYER ROOM</span></div>
    </section>
    <form action="shop.py">
        <input type="hidden" name="searched-query" id="searched-query">
        <input type="hidden" name="msg" value='%s'>
        <input type="hidden" name="username" value='%s'>
        <button id="form-button" style="display: none;">submit</button>
    </form>"""%(login_status,username))

if searched_product == None :
        print("""
    <h1 class="searched-item-name">ALL</h1>
        """)
        try:
            db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
            cur = db.cursor()
            cur.execute("SELECT * FROM my_shop where p_id = 18 or p_id = 67 or p_id = 68 or p_id = 3 or p_id = 28  or p_id = 39  or p_id = 50  or p_id = 10  or p_id = 45  or p_id = 64 or p_id = 95 or p_id = 86")
            # cur.execute("select * from my_shop")
            f = cur.fetchall()
        except Exception as e:
            print(e)
elif searched_product != None:
    print("""
    <h1 class="searched-item-name">%s</h1>"""%searched_product)

    try:
        db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
        cur = db.cursor()
        cur.execute("SELECT * FROM my_shop where category = '%s'"%searched_product)
        f = cur.fetchall()
    except Exception as e:
        print(e)
print("""
<div id="my-shop">
    <div id="custom-design"><a href=""><h2><span>C</span><span>U</span><span>S</span><span>T</span><span>O</span><span>M</span><br><span>D</span><span>E</span><span>S</span><span>I</span><span>G</span><span>N</span></h2></a></div>
    <div id="shop-items">
""")
if f != []:
    for item in f:
        print("""<div class="each-shop-item"><img src="%s" alt="" srcset=""><div class="text-description"><h3 class="product-name">%s</h3><p class="price-p">MRP:Rs.<span class="price">%s</span></p><p class="offer-p">Offer Price:Rs.<sapn class="offer-price">%s</sapn></p></div><button class="view-button" onclick="showimage('%s','P%s','%s','%s','%s')">View</button></div>"""%(item[3],item[2],item[8],item[9],item[3],item[0],item[1],item[2],item[9]))
elif f == []:
    print("""<img src="images/under-construction.jpg" alt="" srcset="">""")
print("""
    </div>
</div>
""")
# <a href="view.py?p_id=%s&myid=5" class="view-button" onclick="showimage("%s")">View</a>
print("""
<div id="image" class="image-show">
    <b id="cross" onclick="document.getElementById('image').style.display = 'none';">x</b>
    <img id="image-view" src="" alt="Some Image of furniture">
    <div id="explanation">
        <table>
            <tr>
                <td style="font-weight: bold;">Product ID</td>
                <td style="font-weight: bold;">Category</td>
                <td style="font-weight: bold;">Description</td>
                <td style="font-weight: bold;">Estimated Price</td>
            </tr>
            <tr>
                <td id="p_id"></td>
                <td id="p_name"></td>
                <td id="p_des"></td>
                <td id="p_price"></td>
            </tr>

        </table>
    </div>
</div>""")


        

# print("""
#     <div id="my-shop">
#         <div id="custom-design"><a href=""><h2><span>C</span><span>U</span><span>S</span><span>T</span><span>O</span><span>M</span><br><span>D</span><span>E</span><span>S</span><span>I</span><span>G</span><span>N</span></h2></a></div>
#         <div id="shop-items">
#             <!-- <div class="each-shop-item"><img src="images/dining-set1.jpeg" alt="" srcset=""><div class="text-description"><h3 class="product-name">rose 7 piece dining set</h3><p class="price-p">MRP:Rs.<span class="price">45,000</span></p><p class="offer-p">Offer Price:Rs.<sapn class="offer-price">40,000</sapn></p></div>
#         <button class="view-button">View</button></div> -->
#         </div>
#     </div>
    
print("""    
</body>
<script
  src="https://code.jquery.com/jquery-3.6.0.js"
  integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
  crossorigin="anonymous"></script>
  <script src="home1.js"></script>
  <script>

    function searched_item(query){
        $("#searched-query").val(query)
        console.log($("#searched-query").text())
        $(".searched-item-name").text($("#searched-query").text())
        $("#form-button").click()

    }
    function showimage(imagepath, p_id, name, des, price) {
        document.getElementById('image-view').src = imagepath
        document.getElementById('image').style.display = "flex";
        document.getElementById('p_id').innerHTML = p_id
        document.getElementById('p_name').innerHTML = name
        document.getElementById('p_des').innerHTML = des
        document.getElementById('p_price').innerHTML = price


    }

  </script>
</html>
""")