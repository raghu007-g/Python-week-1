print("square of a tuple generator")
number = int(input("Enter a number: "))
tuple_of_squares = tuple(i*i for i in range (number+1))
print("Tuple of squares:", tuple_of_squares)