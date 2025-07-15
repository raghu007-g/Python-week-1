print("Count only even and odd numbers")
number = int(input("Enter a number: "))
count_even = 0
count_odd = 0
for i in range(1, number, 1):
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1        
print(f"Count of even numbers and odd number from 1 to {number}: {count_even} and {count_odd}")