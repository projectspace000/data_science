input1 = input("Please enter an integer: ")

try:
   number1 = int(input1)
except ValueError:
   print("That's not an int!")
else:
    print(number1)

number2 = int(input("Please enter another integer: "))

if number1 > number2:
    print "Your first number is larger than your second number"
elif number1 < number2:
    print "Your second number is larger than your first number"
else:
    print "Your numbers are the same"
