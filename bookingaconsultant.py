#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector as mariadb
f = cgi.FieldStorage()
login_status = f.getvalue("msg")
msg3 = f.getvalue("msg3")
username = f.getvalue("username")
    
if login_status == "abc":
    login_status = "yes"
try:
    print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Book a Consultant</title>
    <!-- logo font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Zen+Tokyo+Zoo&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:wght@300&display=swap" rel="stylesheet">
    <!-- logo font -->
    <link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@100&family=Hina+Mincho&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="Home.css">
    <link rel="stylesheet" href="homeMedia.css">
    <style>
        * {
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
            font-family: 'Hina Mincho', serif;
        }

        #acting-like-body {
            margin-top: 15px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            /* height: 76vh; */

        }

        h3 {
            font-family: 'Hina Mincho', serif;
            font-size: 2rem;
            margin-left: 12px;
            color: black;
            margin-top: 12px;
        }

        p {
            font-family: 'Hina Mincho', serif;
            font-size: 21px;
            margin-left: 40px;
            margin-right: 12px;
            color: grey;
        }

        form {
            background: white;
            display: flex;
            padding: 3px 15px;
            flex-direction: column;
            margin: 20px auto;
            border: 1px solid black;
            border-radius: 13px;
        }

        h2 {
            margin: 6px;
            border-bottom: 1px solid;
            width: 277px;
            font-size: 2rem;
        }

        .text-box {
            margin: 4px 0;
            padding-left: 6px;
            height: 32px;
            border-color: #24a0ed;
            outline: none;
            border: 2px solid grey;
            border-radius: 3px;
            font-size: 16px;
        }

        #business-type {
            text-align: center;
            margin: 8px 0;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-around;
        }

        .radio {
            margin-left: 10px;
        }

        label {
            margin-left: 2px;
        }

        #submit {
            text-transform: capitalize;
            color: white;
            background: #24a0ed;
            outline: none;
            border: none;
            height: 28px;
            cursor: pointer;
            font-size: 18px;
        }


        .back {
            position: absolute;
            /* right: 135%; */
            left: 20px;
            top: 70px;
            height: 36px;
        }

        #span {
            margin: 3px;
            color: grey;
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
    </header>
    <div id="acting-like-body">""")
    print("""
    <a href="contactUs.py?msg=%s&username=%s"><img class="back" src="images/outline_arrow_back_black_24dp.png"></a>"""%(login_status,username))
        
    print("""
    
        <h3>What does booking a Consultant means?</h3>
        <p>Booking a consultant means you have appointed a person from our team to suggest you inetriors for your place.
            After booking you will recieve a call from our side and we will schedule the appointment as per mutual
            decison
            and we will visit your place and later if you wish we can take the contarct to build your place the way you
            like.</p>
    """)
except Exception as e:
    print(e)

db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
cur = db.cursor()
cur.execute("select * from user_registration where user_email = '%s'"%(username))
f = cur.fetchone()
if f == None:
    username = None

if username == "None" or username == None:
    print("""
    <form action="sendingmail.py">
        <h2>Book Your Consultant</h2>
    
    <input type="text" class="text-box" placeholder="Enter full your name.." name="fullname" pattern="[a-zA-Z ]+"
                title="Name must contain only alphabets." required>
    <input type="email" class="text-box" placeholder="Enter your email.." name="email" required>
    <input type="text" class="text-box" minlength="10" maxlength="10" name="phoneNumber" pattern="[0-9]{10}"
                title="Enter correct phone number." placeholder="Enter your phone number.." required>
    <input type="text" class="text-box" name="address" placeholder="Enter your address.." required>

    <div>
        <input type="text" class="text-box"  minlength="6" name="pincode" maxlength="6" pattern="[0-9]{6}"
                    title="Enter correct pincode." placeholder="Enter yourpin code.." required>
        <input type="text" class="text-box"  name="landmark" placeholder="Enter any landmark(xyz school)..">
    </div>
    <div id="business-type">
        <div><input type="radio" id="Residential" class="radio" value="Residential" name="business_type"
                        required><label for="Residential">Residential</label></div>
        <div><input type="radio" id="Office" class="radio" value="Office" name="business_type"><label
                        for="Office">Office</label></div>
        <div><input type="radio" id="Restaurant" class="radio" value="Restaurant" name="business_type"><label
                        for="Restaurant">Restaurant</label></div>
        <div><input type="radio" id="Lounge" class="radio" value="Lounge" name="business_type"><label
                        for="Lounge">Lounge</label></div>
        <div><input type="radio" id="Other" class="radio" value="Other" name="business_type"><label
                        for="Other">Other</label></div>
        </div>
        <input type="hidden" name="target" value='bookingaconsultant.py'>
        <button type="submit" id="submit">submit</button>
        <span id="span">*Note - Our service is currently available in Kolkata and nearby cities only.</span>
    </form>
    </div>""")
elif username != "None" or username != None:
    try:
        db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
        cur = db.cursor()
        cur.execute("select * from user_registration where user_email = '%s'"%(username))
        f = cur.fetchone()
        if f != None:
            print("""
        <form action="sendingmail.py">
            <h2>Book Your Consultant</h2>
        <input type="text" class="text-box" placeholder="Enter full your name.." name="fullname" pattern="[a-zA-Z ]+"
                title="Name must contain only alphabets." value="%s" required readonly>
        <input type="email" class="text-box" placeholder="Enter your email.." name="email" value="%s" required readonly>
        <input type="text" class="text-box" minlength="10" maxlength="10" name="phoneNumber" pattern="[0-9]{10}"
                title="Enter correct phone number." placeholder="Enter your phone number.." value="%s" required>
        <input type="text" class="text-box" name="address" placeholder="Enter your address.." required>
        <div>
            <input type="text" class="text-box"  minlength="6" name="pincode" maxlength="6" pattern="[0-9]{6}"
                    title="Enter correct pincode." placeholder="Enter your pincode.." required>
            <input type="text" class="text-box"  name="landmark" placeholder="Enter any landmark(xyz school)..">
            </div>
        <div id="business-type">
            <div><input type="radio" id="Residential" class="radio" value="Residential" name="business_type"
                        required><label for="Residential">Residential</label></div>
            <div><input type="radio" id="Office" class="radio" value="Office" name="business_type"><label
                        for="Office">Office</label></div>
            <div><input type="radio" id="Restaurant" class="radio" value="Restaurant" name="business_type"><label
                        for="Restaurant">Restaurant</label></div>
            <div><input type="radio" id="Lounge" class="radio" value="Lounge" name="business_type"><label
                        for="Lounge">Lounge</label></div>
            <div><input type="radio" id="Other" class="radio" value="Other" name="business_type"><label
                        for="Other">Other</label></div>
        </div>
        <input type="hidden" name="target" value='bookingaconsultant.py'>
            <button type="submit" id="submit">submit</button>
            <span id="span">*Note - Our service is currently available in Kolkata and nearby cities only.</span>
        </form>
        </div>"""%(f[1],f[2],f[3]))
    except Exception as e:
        print("Some error Occurred..")
print("""
</body>

</html>""")