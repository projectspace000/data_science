# sorts a user generated list of integers

a = input("What is your first integer? ")
b = input("What is your second integer? ")
c = input("What is your third integer? ")

list = [a, b, c]

print("Here is the original list: " + str(list))

sorted_list = sorted(list)

print("Here is the sorted list: " + str(sorted_list))