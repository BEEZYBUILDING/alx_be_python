#week 4.3 project
size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
     
    for i in range(size): # Use a for loop to print asterisks in a row
        print("*", end="")  # Stay on the same line
    print()  # Move to the next line after each row
    row += 1





