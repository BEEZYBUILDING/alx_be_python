#week 4.2 project
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
num = number * i
print(number, "*", i, "=", num, "\n")
