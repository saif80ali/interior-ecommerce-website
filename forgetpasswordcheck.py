#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")

import cgi
import mysql.connector as mariadb

f = cgi.FieldStorage()
user_input = f.getvalue("user_input")
try:
    db = mariadb.connect(host="localhost",db="mustafa_furnitures", user="root", passwd = "Mustafa@9831" ,port="3307")
    cur = db.cursor()
    cur.execute("select * from user_registration where user_email = '%s' or phone_number = '%s'"%(user_input,user_input))
    t = cur.fetchall()
    if t == []:
        print('<html>')
        print('  <head>')
        print('    <meta http-equiv="refresh" content="0;url=forgetpassword.py?user_input=%s&msg=0" />'%user_input) 
        print('  </head>')
        print('</html>')
    else:
        if len(t) == 1:
            for item in t:
                email = item[2]
                name = item[1]
            print('<html>')
            print('  <head>')
            print('    <meta http-equiv="refresh" content="0;url=sendingmail.py?receiver=%s&msg=0&name=%s" />'%(email,name))
            print('  </head>')
            print('</html>')
        elif len(t) > 1:
            print("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forget Password</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap" rel="stylesheet">
    <script type="text/javascript">
        function preventBack() { window.history.forward(); }
        setTimeout("preventBack()", 0);
        window.onunload = function () { null };
    </script>
    <style>
        *{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }
        div {
    border: 2px solid gray;
    border-radius: 12px;
    margin: 121px auto;
    width: 400px;
    display: flex;
    flex-direction: column;
    height: 350px;
}
h3 {
    font-family: 'Roboto';
    margin: 20px 0px;
    text-align: center;
    font-size: 2rem;
}
.a {
    min-width: 215px;
    /* max-width: 250px; */
    margin-right: 8px;
    height: 40px;
    display: flex;
    justify-content: space-between;
    text-decoration: none;
    align-items: center;
    border: 2px solid #24a0ed;
    margin-left: 24px;
    margin-top: 8px;
    color: black;
    border-radius: 9px;
    font-family: sans-serif;
}
.text {
    padding-left: 9px;
}
span.icon {
    color: #24a0ed;
    text-align: center;
    border-left: 2px solid;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    width: 30px;
}
p {
    font-family: emoji;
    margin: 6px auto;
    color: gray;
    font-size: 18px;
}
.b {
    text-decoration: none;
    color: grey;
    margin-left: 9px;
    margin-top: 22px;
    font-weight: bold;
}
    </style>
</head>
<body oncontextmenu="return false">
    <div>
        <h3>Select your account</h3>
        <p>An OTP will be sent to your email</p>""")
            for item in t:
                print("""<a href="sendingmail.py?receiver=%s&name=%s" class="a"><span class="text">%s</span><span class="icon">></span></a>"""%(item[2],item[1],item[2]))
            print("""
        <a href="forgetpassword.py" class="b">Cannot find my account</a>
    </div>

</body>
</html>
        """)

except Exception as e:
    print(e)

