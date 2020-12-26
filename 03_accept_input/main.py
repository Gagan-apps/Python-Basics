"""
accept user input with input() function
"""

# STEP 1 -> provide a prompt to user
# print("Enter your Name:")

# STEP 2 ->  accept the value in a variable
# name = input("Enter your Name:\n")

# STEP 3 ->  print the value
# print("Hello " + name)      # concatenation

# a = float(input("Enter Value 1:\n"))
# b = float(input("Enter Value 2:\n"))
#
# print("Sum is: " + str(a + b))

symbol = input("Provide a symbol for design\n")
fill = input("Provide a fill for design\n")
length = int(input("Provide the length\n"))

print(symbol * length)
print(symbol, end='')
print(fill * (length-2), end='')
print(symbol)
print(symbol * length)
