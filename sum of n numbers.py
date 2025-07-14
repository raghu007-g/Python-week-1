print("sum of n numbers")
n=int(input("enter a number:").strip())
sum=0
for i in range(1,n+1):
    sum += i
    print(f"sum of first {n} numbers is {sum}")