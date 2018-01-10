import random
#to make random numbers
x=random.randint(1,100)
y=input("I'm thinking of a number between 1 and 100.\n\nGuess my number! ")
while type(float(y))!=float:
    y=input("You have to choose a number")

while float(y)!=x:
    if float(y)>x:
        print("\nToo big!")
    elif float(y)<x:
        print("\nToo small!")
    else:
        print("You have to choose a number")
    y=input("\nHave another guess! ")
    while type(float(y))!=float:
        y=input("You have to choose a number")

print("\nSpot on! Well done!")
input("\n\nPress enter to exit")
