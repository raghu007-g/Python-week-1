print("1 even number list generator")
print("2 odd number generator")
choice = int(input("Enter your choice: "))
numbers = int(input("final number: "))
if choice == 1:
        list_of_even_numbers = [ i for i in range(0, numbers) if i % 2 == 0]
        print("Even numbers:", list_of_even_numbers)
elif choice == 2:
         list_of_odd_numbers = [ i for i in range(0, numbers) if i % 2 != 0]
         print("Odd numbers:", list_of_odd_numbers)
else:
    print("Invalid choice. Please enter 1 or 2.")