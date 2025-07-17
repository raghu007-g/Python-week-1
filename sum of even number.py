print("sum of even number")
numbers = int(input("Enter the number: "))
sum_of_even = sum(i for i in range(0, numbers + 1)  if i%2 == 0)
print(f"The sum of even numbers from 0 to", {numbers}, "is:", {sum_of_even})