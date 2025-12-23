##
def func(): 
    print("Function in one.py called")

print("Top Level in one.py")

if __name__ == "__main__":## to check if this file is being run directly or being imported
    print("one.py is being run directly")
else:
    print("one.py has been imported")       