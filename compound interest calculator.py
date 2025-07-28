principal=0
rate=0
interest=0

while principal <= 0:
    try:
        principal = float(input("Enter the principal amount (greater than 0): "))
        if principal <= 0:
            print("Principal must be greater than 0. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        
while rate <= 0:
    rate = int(input("Enter the rate of interest (greater than 0): "))
    if rate <= 0:
        print("Rate must be greater than 0. Please try again.")
        
while interest <= 0:
    try:
        interest = float(input("Enter the the interest (greater than 0): "))
        if interest <= 0:
            print("interest must be greater than 0. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        
    total_amount = principal * pow((1 + interest / 100) , rate)
    print(f"The total amount after {interest} years is: {total_amount:.2f}")

        

        
        
