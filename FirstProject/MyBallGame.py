from random import shuffle
myContainers = ['', 'O', '']

def shuffleList(myList):    
    shuffle(myList)
    return myList

print("Before shuffling:", myContainers)
print("After shuffling:", shuffleList(myContainers))


def userGuess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a container number (0, 1, or 2): ")
    return int(guess)   

def checkGuess(myList, userGuess):
    if myList[userGuess] == 'O':
        print("You found the ball! Congratulations!")
    else:
        print(f"Sorry, wrong guess. Try again! {myList}")

checkGuess(shuffleList(myContainers), userGuess())        