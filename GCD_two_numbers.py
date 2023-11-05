# Write a program to find GCD of two numbers.
number_1 = int(input("Enter first number "))
number_2 = int(input("Enter second number "))

# calculate minimum of two numbers
result = min(number_1, number_2)

# find common factor
while result > 0:
    if number_1 % result == 0 and number_2 % result == 0:
        break
    result -= 1

# print result
print(f"GCD of {number_1} and {number_2} is", result)