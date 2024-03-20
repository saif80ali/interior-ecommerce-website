otp = 8562
otp = str(otp)
i = 0
encription = ""
while i < len(otp):

    if otp[i] == "0":
        encription = encription + "g"

    elif otp[i] == "1":
        encription = encription + "j"
        
    elif otp[i] == "2":
        encription = encription + "r"
        
    elif otp[i] == "3":
        encription = encription + "w"
        
    elif otp[i] == "4":
        encription = encription + "z"
        
    elif otp[i] == "5":
        encription = encription + "b"
        
    elif otp[i] == "6":
        encription = encription + "m"
        
    elif otp[i] == "7":
        encription = encription + "p"
        
    elif otp[i] == "8":
        encription = encription + "t"
        
    elif otp[i] == "9":
        encription = encription + "f"
        
    i += 1
encription = encription + "aql"
print("encripted otp=",encription)

#decriptor


j = 0

encription1 = encription.replace("aql","")

print(encription1)
encription2 = ""
while j < len(encription1):
    if encription1[j] == "g":
        encription2 = encription2 + "0"

    elif encription1[j] == "j":
        encription2 = encription2 + "1"
        
    elif encription1[j] == "r":
        encription2 = encription2 + "2"
        
    elif encription1[j] == "w":
        encription2 = encription2 + "3"
        
    elif encription1[j] == "z":
        encription2 = encription2 + "4"
        
    elif encription1[j] == "b":
        encription2 = encription2 + "5"
        
    elif encription1[j] == "m":
        encription2 = encription2 + "6"
        
    elif encription1[j] == "p":
        encription2 = encription2 + "7"
        
    elif encription1[j] == "t":
        encription2 = encription2 + "8"
        
    elif encription1[j] == "f":
        encription2 = encription2 + "9"
        
    j += 1

print("decripted otp=",encription2)