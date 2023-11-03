# Write a program to find if the given number is prime or not.
number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, int(number / 2)):
        if (number % i) == 0:
            print(number, "is not prime")
            break
    else:
        print(number, "is prime") 
    
else: 
    print("Not a prime number")
          
         
    