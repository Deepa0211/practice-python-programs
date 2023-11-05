# Write a program to find a factorial of a number.
number = int(input("Enter a number "))

# Initialize
fact = 1

for i in range(1, number + 1):
    fact = fact * i
    
print(f"Factorial of {number} is", fact)
    