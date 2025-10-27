name = "Realme"
age = 39
marks = 34.5
is_pass = False
a = None
c = 2 + 3j # complex
# conditon
num = int(input("Enter a Num: "))

if num > 500 :
    if num > 750:
        print("Grreater Than 500 and 750")
    else:
        print("only Grreater Than 500")
elif num > 100:
    if num > 250:
        print("Grreater Than 100 and 250")
    else:
        print("only Grreater Than 100")
else:
    print("Less than 100")

lic = True
hel = True
ins = True

fine = 0

if not lic: fine += 500
if not hel: fine += 500
if not ins: fine += 500

print("fine: ", fine)



