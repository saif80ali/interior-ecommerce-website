#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
f = cgi.FieldStorage()
try:
    fullname = f.getvalue("fullname")
    email = f.getvalue("email")
    phoneNumber = f.getvalue("phoneNumber")
    address = f.getvalue("address")
    pincode = f.getvalue("pincode")
    landmark = f.getvalue("landmark")
    business_type = f.getvalue("business_type")
    target = f.getvalue("target")
    print(fullname,email,phoneNumber,address,pincode,landmark,business_type,target)
    # print('<html>')
    # print('  <head>')
    # print('    <meta http-equiv="refresh" content="0;url=sendingmail.py?receiver=%s&msg=0&name=%s" />'%(email,fullname))
    # print('  </head>')
    # print('</html>')
except Exception as e:
    print(e)



