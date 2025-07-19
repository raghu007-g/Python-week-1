print("vowels counter")
vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
text = input("Enter a string: ")
count = sum(1 for char in text if char in vowels)
print("Number of vowels in the string:", count)
