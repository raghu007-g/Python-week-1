print("reverse a number")
number = int(input("Enter a number: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number//= 10
    print(f" Reversed number is : {reversed_number} with palindrome check")
    if str(reversed_number) == str(number):
        print(f"{reversed_number} is a palindrome")
    else:
        print(f"{reversed_number} is not a palindrome")
        