print("palidrome checker")
number_or_string = input("Enter a number or string to check for palindrome: ")
reversed_number_or_string = number_or_string[::-1]
print("Reversed:", reversed_number_or_string)
if number_or_string == number_or_string[::-1]:
    print(f"{number_or_string} is a palindrome.")
else:
    print(f"{number_or_string} is not a palindrome.")