#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector as mariadb
import datetime
import time
t = cgi.FieldStorage()
email = t.getvalue("email")
phoneNumber = t.getvalue("phoneNumber")
address = t.getvalue("address")
fullname  = t.getvalue("fullname")
landmark = t.getvalue("landmark")
pincode = t.getvalue("pincode")
business_type = t.getvalue("business_type")
date = datetime.date.today().strftime('%d/%m/%y')
t = time.localtime()
time1 = time.strftime("%H:%M:%S",t)

try:
    db = mariadb.connect(user="root", passwd = "Mustafa@9831" , db="mustafa_furnitures" , host="localhost", port="3307")
    cur = db.cursor()
    cur.execute("insert into consultant_booking (date,time,fullname,email,phoneNumber,address,pincode,landmark,business_type) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(date,time1,fullname,email,phoneNumber,address,pincode,landmark,business_type))
    db.commit()
    print("Booking confirmed!")
except Exception as e:
    print(e)