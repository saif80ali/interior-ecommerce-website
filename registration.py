#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")

import cgi
import mysql.connector as mariadb

t = cgi.FieldStorage()

fullname = t.getvalue("fullname")
email = t.getvalue("email")
number = t.getvalue("number")
password = t.getvalue("password")

try:
    db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
    cur = db.cursor()
    cur.execute("INSERT INTO user_registration (fullname,user_email,phone_number,password) VALUES ('%s','%s','%s','%s');"%(fullname,email,number,password))
    db.commit()
    msg = "abc"
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content=0;url="shop.py?msg=%s&username=%s"/>'%(msg,email)) 
    print('  </head>')
    print('</html>')


except Exception as e:
    msg = "def"
    print(e)