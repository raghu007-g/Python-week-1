print("find last 4 digits of credit card number")
credit_card_number = input("Enter your credit card number: ")
#only contain digits and less than 20 characters
if len(credit_card_number) < 20 and credit_card_number.isdigit():
#using slicing to get the last 4 digits    
    last_four_digits = credit_card_number[-4:]
    print(f"your last 4 digits are: {last_four_digits}")
    print("let's make fun with it")
    credit_card_number=credit_card_number[::-1]
    print(f"your credit card number in reverse is: {credit_card_number}") 
else:
    print(f"dont use spaces or letters, only digits and less than 20 characters then use {credit_card_number}")