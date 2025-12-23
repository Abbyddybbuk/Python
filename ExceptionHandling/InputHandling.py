def ask_for_input():
    while True:
        try:
            value = int(input("Please enter an integer: "))
        except ValueError:
            print("That was not a valid integer. Please try again.")
            continue
        else:
            print(f"You entered the integer: {value}")
            break
        finally:
            print("Execution of the input function is complete.")

ask_for_input()