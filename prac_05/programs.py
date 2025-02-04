"""
CP1401 - Coding Checkpoint 1
https://github.com/CP1401/Practicals/blob/master/checkpoints/checkpoint_01.md
Suggested Solutions
Please do not use/view these solutions until you have attempted the checkpoint challenges yourself!
"""

# String formatting demos
product = "fish"
price = 12.3
# No real formatting
print("You want ", product, ". It costs $", price, sep="")

# .format method
print("You want {}. It costs ${}".format(product, price))
print("You want {}. It costs ${:.2f}".format(product, price))

# f-string version
print(f"You want {product}. It costs ${price}")
print(f"You want {product}. It costs ${price:.2f}")


# Input, Processing, Output

# 1. Write a program that calculates a new value based on an
# original value and a (percentage-like) increase or decrease.
# Example:
# Original: 100, Change: 0.05, Result: 105
# Original: 50.5, Change: -0.1, Result: 45.45

# Pseudocode:
# get original_value, change
# new_value = original_value * (1 + change)
# print new_value

original_value = float(input("Original: "))
change = float(input("Change: "))
new_value = original_value * (1 + change)
print(new_value)


# Decision Structures

# 2. Ask the user for the time of day (0-23 hours)
# and if they are coming or going.
# Then print a statement about their situation like:
# It is before noon and you are coming. Hi!
# It is after noon and you are going. Bye!

# Pseudocode:
# get time, state
# if time < 12
#     noon_message = before
# else
#     noon_message = after
# if state == coming
#     direction_message = Hi
# else
#     direction_message = Bye
# print noon_message, direction_message

time = int(input("Time: "))
state = input("Coming or going? ").lower()
if time < 12:
    noon_message = "before"
else:
    noon_message = "after"
if state == "coming":
    direction_message = "coming. Hi!"
else:
    direction_message = "going. Bye!"
print("It is {} noon and you are {}".format(noon_message, direction_message))


# 3. Coffee orders made simple.

# Pseudocode:
# get colour, size
# if size is small
#     cost = 3
# else if size is medium
#     cost = 4
# else
#     cost = 5
# if colour is white
#     cost = cost + 1
# print cost

colour = input("Colour: ").lower()
size = input("Size: ").lower()
if size == "small":
    cost = 3
elif size == "medium":
    cost = 4
else:
    cost = 5
if colour != "black":
    cost += 1
print("${}".format(cost))


# Repetition Structures

# 4. Coffee orders with error-checking
# Pseudocode:
# get colour
# while colour is not "black" and colour is not "white" 
#     print error
#     get colour
# while size is not "small" and size is not "medium" and size is not "large"
#     print error
#     get size
# if size is small
#     cost = 3
# else if size is medium
#     cost = 4
# else
#     cost = 5
# if colour is white
#     cost = cost + 1
# print cost

colour = input("Colour: ").lower()
while colour != "black" and colour != "white":
    print("Invalid input")
    colour = input("Colour: ").lower()
size = input("Size: ").lower()
while size != "small" and size != "medium" and size != "large":
    print("Invalid input")
    size = input("Size: ").lower()
if size == "small":
    cost = 3
elif size == "medium":
    cost = 4
else:
    cost = 5
if colour != "black":
    cost += 1
print("${}".format(cost))

# 5. Write a program to ask the user for a low value and a
# high value, then print all of the integers between those
# values inclusive and show the total of those numbers.
# Example, if the inputs were 10 and 20, you would print:
# 10 11 12 13 14 15 16 17 18 19 20 totals: 165

# Pseudocode:
# get low, high
# total = 0
# for i from low to high
#     print i
#     total = total + i
# print total

low = int(input("Low: "))
high = int(input("High: "))
while high < low:
    print("High must be >=", low)
    high = int(input("High: "))
total = 0
for i in range(low, high + 1):
    print(i, end=" ")
    total += i
print("totals:", total)
