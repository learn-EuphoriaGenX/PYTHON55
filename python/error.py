a = input("Enter a Number A: ")
b = input("Enter a Number B: ")
try:
    a = int(a)
    b = int(b)
    print(a/b)
# except ZeroDivisionError:
#     print("Are u Mad!")
# except ValueError:
#     print("Invalid Input")
except Exception as error:
    print(f"ERROR: {error}")
else:
    print("Wow! Error Free")
finally:
    print("Its me FInally!")