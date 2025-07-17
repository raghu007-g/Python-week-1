string=str(input("Enter your name: "))
print("Hello, " + string.capitalize() + "! Welcome to the regiser your biodata program.")
passion = str(input("Enter your passion: "))
print("Your passion is: " + passion.capitalize())
print("just make fun lets how many letters in your passion: " + str(len(passion)))
if  "developer" in passion:
 print("all the best for your journey in " + passion.capitalize() + "!")
 print("lets maake fun reverese your passion: " + passion[::-1])