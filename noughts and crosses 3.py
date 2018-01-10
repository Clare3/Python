import random
#slots are spaces in the grid
slots=["a","b","c","d","e","f","g","h","i"]
D={"a":8,"b":1,"c":6,"d":3,"e":5,"f":7,"g":4,"h":9,"i":2,0:0,"X":0}
Dinv={8:"a",1:"b",6:"c",3:"d",5:"e",7:"f",4:"g",9:"h",2:"i"}
#this is because noughts and crosses can correspond to choosing 3 numbers that add up to 15
pchoices=[]
cchoices=[]
#where the computer and player have put their marks
#set up these variables first
win=None
turn=None
#function for drawing the grid as it stands
def grid():
    print("\t\t ",slots[0]," | ",slots[1]," | ",slots[2],"\n\t\t------------",
           "\n\t\t ",slots[3]," | ",slots[4]," | ",slots[5],"\n\t\t------------\n\t\t ",slots[6]," | ",slots[7]," | ",slots[8])
#function to write the instructions
def instructions():
    print("Welcome to noughts and crosses!",
           "\n\nYou will play against me, the computer.",
           "\n\nTo tell me your choices, you will choose a letter according to the grid:\n\n")
    grid()
#what to do when it's the player's turn
def player():
    #this win was to try and remove problems - safe to assume noone has won yet
    win=None
    p=input("\nWhich letter represents your choice? ")
    #check it's a valid and unchosen choice
    while p not in slots or p==0 or p=="X":
        print("\nSorry, that space is not available. \nThe grid looks like this at the moment:\n\n")
        grid()
        p=input("\nWhich letter represents your choice? ")
    k=slots.index(p)
    #find the one they chose and take it out of the options
    plocal=pchoices[:]
    plocal.append(p)
    #check whether they've got 3 numbers that add up to 15
    for i in pchoices:
        for j in pchoices:
            for m in pchoices:
                if D.get(i)+D.get(j)+D.get(m)==15 and i!=j and i!=m and j!=m:
                    print("\nWell done! You win!")
                    win="player"
                    print(win)
                    #For some reason this break doesn't work
                    #so it prints that they've won 6 times
                    return (win,p,k)
    return (win,p,k)
#what to do when it's the computer's turn
def computer():
    win=None
    q=compchoice()
    #the computer picks according to the function below, and if it doesn't choose,
    #it picks again.
    while q not in slots or q==0 or q=="X":
        q=random.choice(slots)
    l=slots.index(q)
    clocal=cchoices[:]
    clocal.append(q)
    for i in clocal:
        for j in clocal:
            for k in clocal:
                if D.get(i)+D.get(j)+D.get(k)==15 and i!=j and i!=k and j!=k:
                    print("\nYay! I win!")
                    win="computer"
                    return (win,q,1)
    return (win,q,l)
#how the computer chooses its guess
def compchoice():
    #if it's the first turn, either go in the middle or in a corner
    corners=["a","c","g","i"]
    if slots==["a","b","c","d","e","f","g","h","i"]:
        z=random.randint(0,1)
        if z==1:
            q="e"
            return q
        elif z==0:
            q=random.choice(corners)
            return q
    #if the computer can win, then do so
    for i in cchoices:
        for j in cchoices:
            #if the value that needs to be added to i and j to get 15 is available, 
            if i!=j and Dinv.get(15-D.get(i)-D.get(j)) in slots:
                #...then choose it
                q=Dinv.get(15-D.get(i)-D.get(j))
                return q
    #if the player can win, block them
    for i in pchoices:
        for j in pchoices:
            #if the value that needs to be added to i and j to get 15 is available, 
            if i!=j and Dinv.get(15-D.get(i)-D.get(j)) in slots:
                #...then choose it
                q=Dinv.get(15-D.get(i)-D.get(j))
                return q
    #otherwise, go in the middle, if it's free
    if "e" in slots:
        q="e"
        return q
    #or in a corner
    cornavailable=[]
    #find which corners are free
    for i in corners:
        if i in slots:
            cornavailable.append(i)
    #and pick one at random, if you can
    if cornavailable:
        q=random.choice(cornavailable)
    #if not, it'll leave q empty and the old code will tell it to pick q at random
        return q
instructions()
print("\n\nWould you like to go first?")
while turn!="yes" and turn!="no":
    turn=input("\nType 'yes' or 'no': ")
#The flow of the game - keep going if noone's won
#Except that it keeps going anyway
while win==None and ("a" in slots or "b" in slots or "c" in slots or "d" in slots or "e" in slots or "f" in slots or "g" in slots or "h" in slots or "i" in slots):
    if turn=="yes":
        P=player()
        win=P[0]
        pchoices.append(P[1])
        slots[P[2]]=0
        grid()
        turn="no"
        continue
    if turn=="no":
        input("My turn! \nPress the enter key when you're ready to see my move!")
        C=computer()
        win=C[0]
        cchoices.append(C[1])
        slots[C[2]]="X"
        grid()
        turn="yes"

input("Press the enter key to exit")
