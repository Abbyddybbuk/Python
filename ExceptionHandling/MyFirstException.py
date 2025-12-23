def add(n1, n2):
    try:
        print(n1 + n2)
    except Exception as e:
        print(f"Error: {e}: Invalid inputs for addition.")
    else:
        print("Addition performed successfully.")



add(10, '20')  # This will raise an exception
add(10, 20)    # This will work fine
