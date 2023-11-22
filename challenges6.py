while True:
    ("Menu:")
    print ("y to multipy by 2 again")
    print("n to stop multiplying")

    choice = (input("Please enter choice(y/n): "))
    if choice == "y":
        while True:
            number = (int(input("please input a number you wish to multiply: ")))
            if number != 1:
                print ('please enter correct number')
            else:
                mult = number*2
                print("the answer is:",mult,)
                break
    elif choice =="n":
        print("thanks for using this program")
        break
    else: 
        print("please enter y or n")
