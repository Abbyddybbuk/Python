myFile = open('Summary.txt')
print(myFile.read())
print(myFile.read())  # This will print an empty string since the file pointer is at the end
myFile.seek(0)  # Reset the file pointer to the beginning
print(myFile.read())  # Now this will print the content of the file again
myFile.seek(0)  # Reset the file pointer to the beginning
print(myFile.readlines())  # This will print a list of lines in the file
myFile.close()  # Always good practice to close the file when done

with open('Summary.txt') as myFile2:
    contents = myFile2.read()
    print(contents) # The file is automatically closed after the with block


#with open('Summary.txt', mode='w') as myFile2:#mode can be r, w, a, r+; default is r(readable); w is writeable
#    contents = myFile2.read()
#    print(contents) # The file is automatically closed after the with block    

with open('Summary.txt', mode='a') as myFile2:#mode can be r, w, a, r+; default is r(readable); w is writeable; a is append
    myFile2.write("\nNew line added to the file.") 
    # The file is automatically closed after the with block 

with open('Summary.txt') as myFile3:
    contents = myFile3.read()    

with open('SummaryTest.txt', mode='w') as myFile4:
    myFile4.write("Created This file using Python")     

with open('SummaryTest.txt') as myFile5:
    contents1 = myFile5.read()
    print(contents1) # The file is automatically closed after the with block     