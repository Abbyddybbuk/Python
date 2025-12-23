try:
    file = open("NewFile.txt", "r")
    file.write("Hello, World!")
except TypeError as e:
    print(f"IOError occurred: {e}") 
except OSError as e:
    print(f"OSError occurred: {e}")
except Exception as e:
    print(f"Some other exception occurred: {e}")    
finally:
    file.close()
    print('It will execute no matter what')