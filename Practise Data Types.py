# Q. Write a program to take input for 2 numbers and print their sum.
# Q. Write a program to take input for 2 numbers and print their difference.
# Q. Write a program to take input for the length and the height of a rectangle. Calculate and print the perimeter and area of the rectangle.

# 1.

num1 = int(input("Enter one number."))
num2 = int(input("Enter another number."))

sum = num1 + num2
print(sum)

# 2.

num3 = int(input("Enter one number."))
num4 = int(input("Enter another number."))

sum1 = num3 - num4
print(sum1)

# 3.

length = int(input("Enter the length of your rectangle."))
height = int(input("Enter the height of your rectangle."))

length_2 = length * 2
height_2 = height * 2

sum2 = length_2 + height_2
print("Perimeter is: {}".format(sum2))

area = length * height
print("Area is: {}".format(area))

# Q. Ask the user to enter their first name and last name.
# Construct the full name and display it
# Fetch and display the initials 
# Find the length of the name
# Generate a username in lowercase by joining the first 3 letters of the first name and the first letter of the last name

# 4.

forename = input("Enter your first name.")
surname = input("Enter your last name.")

print("Your full name is,"+forename+" "+surname)
full_name = forename + surname
print(len(full_name))

initial1 = forename[0]
initial2 = surname[0]
intitial = initial1 + initial2
print(intitial)

nick1 = forename[0:4]
nick2 = surname[0]
nick = nick1 + " " + nick2
print(nick)

# Q. Create a program to ask for the marks of 3 subjects (for example- English, Math, Science, Computer Science, and Arts). 
# Calculate and print the total marks and average(mean) of the marks.

