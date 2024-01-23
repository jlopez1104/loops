num_people = int(input("How many people would you like to invite to your party? "))
if num_people < 10:
    for i in range(num_people):
        name = input("Enter the name of person {}: ".format(i + 1))
        print("{} has been invited.".format(name))
else:
    print("Too many people. Please invite fewer than 10.")