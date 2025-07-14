print("for grade system")
marks=int(input("enter your marks:").strip())
if marks >= 90 and marks <= 100:
    print("grade A")
elif marks >=75 and marks<= 89:  
    print("grade B")
elif marks >=60 and marks <= 74:
    print("grade C")
else:
    print("fail")