number1 = False
number2 = False

while type(number1) != int:
    input1 = input("Give me a number: ")
    try:
        number1 = int(input1)
    except ValueError:
        print("Please try again.")
    
while type(number2) != int:
    number2 = input("Give me another number: ")

# number1 = input("Give me a number: ")
# number2 = input("Give me another number: ")

if number1 > number2:
    print "Your first number is larger than your second number"
elif number1 < number2:
    print "Your second number is larger than your first number"
else:
    print "Your numbers are the same"
