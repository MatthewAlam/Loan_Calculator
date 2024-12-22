# Save the input in this variable
ticket = list(map(int, input()))
# Add up the digits for each half

half1 = ticket[0] + ticket[1] + ticket[2]
half2 = ticket[-1] + ticket[-2] + ticket[-3]

# Thanks to you, 123this code w1ill work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")