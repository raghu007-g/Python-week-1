import getpass
           
correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin= getpass.getpass("Enter your ATM PIN: ")
    if len(pin) != 4 and not pin.isdigit():
        print("Incorrect PIN. Please try again.")
        continue
    if pin == correct_pin:
        print("PIN accepted. Access granted.")
        break
    else:
         attempts -= 1
    if attempts==0:
        print("Too many attempts.  card blocked.")
    else:
       
        print(f"you have {attempts} attempts left out of 3.")