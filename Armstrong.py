# take user input
number = int(input("Enter a number: "))
number_str = str(number)
number_digits = len(number_str)

# initialize 
sum = 0 
temp = number 

# addition of cubes of all digits
while temp > 0:
     digit = temp % 10
     sum += digit ** number_digits
     temp //= 10

# result display 
if number == sum:
     print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")


