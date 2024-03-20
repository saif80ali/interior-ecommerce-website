#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
from os import umask
import mysql.connector as mariadb

t = cgi.FieldStorage()
username = t.getvalue("username")
password = t.getvalue("password")
target = t.getvalue("target")
try:
    db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
    cur = db.cursor()
    cur.execute("select * from user_registration where user_email = '%s' and password = '%s'"%(username,password))
    f = cur.fetchone()
    if f != None:
        msg = "abc"
        print('<html>')
        print('  <head>')
        print('    <meta http-equiv="refresh" content=0;url="shop.py?msg=%s&username=%s"/>'%(msg,username)) 
        print('  </head>')
        print('</html>')
    else:
        msg = "def"
        print('<html>')
        print('  <head>')
        print('    <meta http-equiv="refresh" content=0;url="%s?msg=%s&msg3=failed&user=%s&passwd=%s"/>'%(target,msg,username,password)) 
        print('  </head>')
        print('</html>')

except Exception as e:
    print(e)