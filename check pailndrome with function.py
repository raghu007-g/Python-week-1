string_or_number = input("Enter a string or number: ")
def is_palindrome(string_or_number):
    string_or_number = string_or_number.lower().strip()
    if string_or_number == string_or_number[::-1]:
        return True
    else:
        return False
print(f"Is '{string_or_number}' a palindrome? {is_palindrome(string_or_number)}")