#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")

import smtplib
import cgi
from email.message import EmailMessage
import random
import mysql.connector as mariadb
# import imghdr

msg = EmailMessage()

f = cgi.FieldStorage()

target = f.getvalue("target")

msg['From'] = "mdsaif80ali@gmail.com"

if target == "shop.py":
    msg['Subject'] = "Your verification OTP!"
    fullname = f.getvalue("fullname")
    fullname.replace(" ","+")
    fullname = fullname.replace(" ","+")
    name = fullname
    name = name.replace("+"," ")
    email = f.getvalue("email")
    msg['To'] = email
    number = f.getvalue("number")
    password = f.getvalue("password")
    db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
    cur = db.cursor()
    cur.execute("SELECT * FROM user_registration WHERE user_email = '%s' "%(email))
    t = cur.fetchall()
    if t !=[]:
        msg1 = "def"
        print('<html>')
        print('  <head>')
        print('    <meta http-equiv="refresh" content=0;url="failed.py?msg=%s&msg2=signup"/>'%msg1) 
        print('  </head>')
        print('</html>')
        exit()

elif target == "bookingaconsultant.py":
    msg["Subject"] = "OTP for consultant booking confirmation!"
    fullname = f.getvalue("fullname")
    fullname = fullname.replace(" ","+")
    name = fullname
    name = name.replace("+"," ")
    email = f.getvalue("email")
    msg['To'] = email
    phoneNumber = f.getvalue("phoneNumber")
    address = f.getvalue("address")
    address = address.replace(" ","+")
    pincode = f.getvalue("pincode")
    landmark = f.getvalue("landmark")
    landmark = landmark.replace(" ","+")
    business_type = f.getvalue("business_type") 
else:
    name = f.getvalue("name")
    msg['Subject'] = "Your OTP to change password!"
    msg['To'] = f.getvalue("receiver")


# for sending photo
# msg.set_content("image attached")
# with open('images/bathroom1.jfif','rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name
# msg.add_attachment(file_data, maintype = "image" , subtype = file_type, filename = file_name)

#sending html
otp = random.randint(1001,5000)
otp = str(otp)
i = 0
encription = ""
while i < len(otp):

    if otp[i] == "0":
        encription = encription + "g"

    elif otp[i] == "1":
        encription = encription + "j"
        
    elif otp[i] == "2":
        encription = encription + "r"
        
    elif otp[i] == "3":
        encription = encription + "w"
        
    elif otp[i] == "4":
        encription = encription + "z"
        
    elif otp[i] == "5":
        encription = encription + "b"
        
    elif otp[i] == "6":
        encription = encription + "m"
        
    elif otp[i] == "7":
        encription = encription + "p"
        
    elif otp[i] == "8":
        encription = encription + "t"
        
    elif otp[i] == "9":
        encription = encription + "f"
        
    i += 1
encription = encription + "aql"

msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
    <head><title>Some Error Occurred</title>
    <style>
        #otp{
            font-size:2rem;
        }
        #name{
            text-transform: capitalize;
        }

    </style>
    </head>
    <body>
        <h3>Dear <span id="name">%s</span> ,</h3>
        <h1> Your one time password is <span id="otp">%s</span>.</h1>
    </body>
    </html>"""%(name,otp), subtype = 'html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     #  smtp.ehlo()
#     #  smtp.starttls()
#     #  smtp.ehlo()
     smtp.login(msg['From'],"zgwowzagdpogmfpn")
     smtp.send_message(msg)

if target == "shop.py":
    print('<html>')
    print('  <head>')
    print(' <meta http-equiv="refresh" content=0;url="mailsent.py?session=%s&email=%s&number=%s&password=%s&target=%s&fullname=%s"/>'%(encription,email,number,password,target,fullname)) 
    print('  </head>')
    print('</html>')
    
elif target == "bookingaconsultant.py":
    print('<html>')
    print('  <head>')
    print(' <meta http-equiv="refresh" content=0;url="mailsent.py?session=%s&email=%s&phoneNumber=%s&address=%s&target=%s&fullname=%s&landmark=%s&business_type=%s&pincode=%s"/>'%(encription,email,phoneNumber,address,target,fullname,landmark,business_type,pincode)) 
    print('  </head>')
    print('</html>')

else:
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url=mailsent.py?receiver=%s&session=%s&name=%s" />'%(msg['To'],encription,name)) 
    print('  </head>')
    print('</html>')


