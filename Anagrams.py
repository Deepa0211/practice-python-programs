# take user input
word1 = input("Enter first string: ").lower()
word2 = input("Enter second string: ").lower()


if sorted(word1) == sorted(word2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")