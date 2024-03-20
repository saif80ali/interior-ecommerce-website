#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")

import cgi
f = cgi.FieldStorage()
user_input = f.getvalue("user_input")
msg = f.getvalue("msg")

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
        header {
    margin: 22px 9px;
}
header a {
    display: flex;
    width: 45px;
    height: 28px;
    align-items: center;
    border-radius: 10px;
    justify-content: center;
    cursor: pointer;
    background: #24a0ed;
    color: white;
}
a:hover{
    background-color: #53a8dd;
    border: 2px solid #53a8dd;
}
#user-credentials {
    margin: 102px auto;
    width: 400px;
    display: flex;
    flex-direction: column;
}
img {
    filter: invert(1);
    height: 26px;
}
h3 {
    font-size: 2rem;
    font-family: 'Roboto';
    font-weight: bold;
    margin: 17px auto;
}
p {
    margin: auto;
    width: 349px;
    text-align: center;
    font-size: 18px;
    color: grey;
    font-family: emoji;
}
form {
    display: flex;
    flex-direction: column;
    width: 75%;
    margin: 31px auto;
}
.input {
    padding: 8px;
    outline: none;
    border: 2px solid #24a0ed;
}
span {
    color: red;
    font-family: monospace;
    font-size: 15px;
    font-weight: bold;
}
button {
    margin: 18px 0px;
    height: 36px;
    font-weight: bold;
    color: white;
    background: #24a0ed;
    border: none;
    outline: none;
    cursor: pointer;
}
button:hover{
    background-color: #7db4e3;
}
.red{
    border-color:red ;
}
.hide{
    display: none;
}
    </style>

</head>
<body>
    <header><a href="Home.py?msg=no&username=None"><img src="images/outline_arrow_back_black_24dp.png" alt=""></a></header>
    <!-- <h1>Forget Password</h1> -->
    <div id="user-credentials">
        <h3>Find your account</h3>
        <p>Enter your email or phone number linked to your account.</p>
        <form action="forgetpasswordcheck.py">""")
if user_input != None:
    print("""<input type="text" placeholder="xyz@gmail.com" value="%s" class="input red" name="user_input" required>"""%user_input)

else:
    print("""<input type="text" placeholder="xyz@gmail.com" value="" class="input" name="user_input" required>""")
if msg == "0":
    print("""<span id="nouser">No users found.</span>""")

print("""                   
            <button type="submit">Find Account</button>
        </form>
    </div>
</body>
<script
  src="https://code.jquery.com/jquery-3.6.0.js"
  integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
  crossorigin="anonymous"></script>
<script>
    $(".input").click(function(){
        $(".input").removeClass("red")
        $("#nouser").addClass("hide")
    
    })
</script>
</html>""")