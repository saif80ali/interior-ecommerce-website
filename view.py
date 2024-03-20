#!C:\Users\asus\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
f = cgi.FieldStorage()
myid = f.getvalue("myid")
p_id = f.getvalue("p_id") 
print("meraid=", myid)
print()
print("product ka id =",p_id)