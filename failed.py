#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
f = cgi.FieldStorage()
msg = f.getvalue("msg")
msg2 = f.getvalue("msg2")
text = ""
if msg2 == "login":
    text = "Invalid Credentials"  
elif msg2 == "signup":
    text = "Email Already Registered Try Again With Another Email."
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
            height: 470px;
            width: 499px;
        }
h2 {
    margin: 0px 3px;
    text-align:center;
    color: rgb(19,9,124);
    font-size: 2rem;
}
a {
    text-decoration: none;
    background: rgb(75,77,247);
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
    <img src="images/help.jpg" alt="">
    <h2>%s</h2>
    <a href="Home.py?msg=%s&username=None">Try Again</a>   
</body>
</html>"""%(text,msg))