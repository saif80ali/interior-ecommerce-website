#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector as mariadb
f = cgi.FieldStorage()
username = str(f.getvalue("receiver"))
password = str(f.getvalue("password"))

try:
    db = mariadb.connect(user="root",passwd="Mustafa@9831",db="mustafa_furnitures" , host="localhost", port="3307")
    cur = db.cursor()
    cur.execute("UPDATE user_registration SET password='%s' WHERE user_email='%s'"%(password,username))
    db.commit()
    print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Failed</title>
    <style>
        *{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }
        body{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        img {
    height: 435px;
    
}
h2 {
    text-align:center;
    color: rgb(255,114,92);
    font-size: 2rem;
}
a {
    text-decoration: none;
    background: rgb(255,114,92);
    height: 34px;
    width: 112px;
    margin-top: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    cursor: pointer;
    border-radius: 4px;
    font-weight: bold;
    text-transform: uppercase;
}
    </style>
</head>
<body>
    <img src="images/passwordupdated.jpg" alt="">
    <h2>Password changed successfully!</h2>
    <a href="Home.py">Home</a>   
</body>
</html>""")
except Exception as e:
    print(e)