number1 = 0
number2 = 0

while True:
    try:
        input1 = input("Please enter an integer: ")
        input1 = int(input1)
    except ValueError:
        print("That is not an integer, please try again.")
        continue
    else:
        number1 = input1
        break
while True:
    try:
        input2 = int(input("Please enter an integer: "))
    except ValueError:
        print("That is not an integer, please try again.")
        continue
    else:
        number2 = input2
        break

if number1 > number2:
    print "Your first number is larger than your second number"
elif number1 < number2:
    print "Your second number is larger than your first number"
else:
    print "Your numbers are the same"
