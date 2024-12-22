# Read the user's age
age = int(input())

# Check the age and print the corresponding category
# TODO: Write your if statement here
if 18 > age:
    print("Minor")
elif 18 <= age <= 63:
    print("Adult")
elif age >= 65:
    print("Senior")