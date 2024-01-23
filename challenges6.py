while True:
    try:
        user_input = float(input("Enter a number: "))
        answer = input("Do you want to double the number? (y/n): ").lower()
        while True:
            if answer == 'y':
                user_input *= 2
                print(f"The doubled number is: {user_input}")
            else:
                print("thanks for using program!")
                break
    except ValueError:
        print("Invalid input. Please enter a valid number.")