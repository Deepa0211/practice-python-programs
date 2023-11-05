# Write a program to print the following pattern.
# *
# **
# ***
# ****
# *****

rows = 5

# rows
for i in range(1, rows + 1):
    # columns
    for j in range(1, i + 1):
        # print *
        print("*" , end="")
    print()
    