# Write a program to find a fibonacci of a number.
n = int(input("What's n? "))

first_number =  0
second_number =  1
next_number = second_number
count = 1

print(first_number, second_number, end=" ")

# creating sequence
while count <= n:
    print(next_number, end=" ")
    first_number, second_number = second_number, next_number
    count += 1
    next_number = first_number + second_number
    
    
    

    