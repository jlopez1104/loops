invitations = 0

while True:
    name = input("Who would you like to invite to the party? (Type 'done' to finish): ")
    if name == 'done':
        print("amount of invitations",invitations)
        print("thanks for using code")
        break
    
    print("{} has now been invited.".format(name))
    invitations += 1

    print("You have invited {} people to the party.".format(invitations))