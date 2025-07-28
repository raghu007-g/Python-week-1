print("valid checker to password")
name = str(input("Enter your name: "))
if len(name) < 9 and name.isalnum():
   print("Valid name")
elif name.find(" "):
    print("Invalid name, it should not contain spaces")
  