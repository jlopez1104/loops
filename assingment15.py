while True:
  input = input("would you like to find the factoial of a number?(y/n): ")
  if input == "y":
    try:
      n = int(input("Enter a positive interger: "))
      if n <= 0:
        raise ValueError("Please enter a positive interger.")
    except ValueError:
      print("please enter a positive interger")
    else:
      print("the factorizations of", n, "are")
      for i in range(1, n + 1):
          if n % i == 0:
              factor = n // i
              print(f"{i} times {factor} equals {n}")
  else:
    print("thank you for using the program")
    break