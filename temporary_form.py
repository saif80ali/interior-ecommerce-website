#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")

import cgi
import mysql.connector as mariadb

f = cgi.FieldStorage()
category = f.getvalue("category")
poster_image = "images/" + f.getvalue("poster_image")
title = f.getvalue("title")
image_1 = "images/" + f.getvalue("image_1")
image_2 = "images/" + f.getvalue("image_2")
image_3 = "images/" + f.getvalue("image_3")
image_4 = "images/" + f.getvalue("image_4")
marked_price = int(f.getvalue("marked_price"))
offer_price = int(f.getvalue("offer_price"))
redirectURL = "temporary.html?msg=done"

try:
    db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
    cur = db.cursor()
    cur.execute("insert into my_shop (category, title, poster_image, image_1, image_2, image_3, image_4, marked_price, offer_price) values ('%s','%s','%s','%s','%s','%s','%s',%d,%d)"%(category,title,poster_image,image_1,image_2,image_3,image_4,marked_price,offer_price))
    db.commit()
    # print('<html>')
    # print('  <head>')
    # print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
    # print('  </head>')
    # print('</html>')
    print("record inserted")

except Exception as e:
    print(e)

