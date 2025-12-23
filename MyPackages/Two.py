import One

print("Top Level in two.py")

One.func()
if __name__ == "__main__":## to check if this file is being run directly or being imported
    print("two.py is being run directly")   
else:
    print("two.py has been imported")
