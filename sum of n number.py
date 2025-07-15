print("Sum of n numbers")
method = input("Choose method (1: loop, 2: formula): ")
n = int(input("Enter a number: "))

if method == "1":
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"The sum of the first {n} numbers is: {total}")
elif method not in ("1", "2"):
    print("Invalid method selected. Please choose 1 or 2.")
else:
    total = n * (n + 1) // 2
    print(f"The sum of the first {n} numbers is: {total}")