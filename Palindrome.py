# Write a program to check if the given number is palindrome or not.
text = input("Enter a text to check palindrome: ").lower()

for i in text:
    if text[0] == text[-1]:
        print("Text is palindrome")
        break
else:
    print("Text is not palindrome")
    
    