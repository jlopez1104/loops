while True:
    input = input("would you like to see times tables up to 12?(y/n): ")
    if input == "y":
        user_input = input("Enter a number between 1 and 12: ")
        if user_input.isdigit():
            number = int(user_input)
            if 1 <= number <= 12:
                print("Times table for {} up to 12:".format(number))
                for i in range(1, 13):
                    result = number * i
                    print("{} x {} = {}".format(number, i, result))

            else:
                print("Please enter a number between 1 and 12.")
        else:
            print("Invalid input. Please enter a valid number.")
    else:
        print("thanks for using program")
        break