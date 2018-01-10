import random
while True:
    DICTIONARY = ("George is a poo", "well bugger me!", "fuck wank bollocks", "piss off dickhead", "shitface arsehole")
    HINTS = ("GIAP","WBM","FWB","POD","SA")
    word=random.choice(DICTIONARY)
    w=word
    L=len(w)
    N=""
    while len(N)<L:
        p=int(random.randrange(len(w)))
        N+=w[p]
        w=w[0:p]+w[p+1:len(w)]
    print("I've chosen a phrase. Guess the phrase from this anagram: ",N,
          "\nOr, enter 'hint' if you're stuck")
    guess=input(" ")
    while guess!=word:
        if guess=="hint":
            for i in range(3):
                if word==DICTIONARY[i]:
                    h=HINTS[i]
                    break
            print("The first letters are: ",h)
            guess=input("Now have a guess!")
            continue
        print("That's not right!")
        w=word
        L=len(w)
        N=""
        while len(N)<L:
            p=int(random.randrange(len(w)))
            N+=w[p]
            w=w[0:p]+w[p+1:len(w)]
        print("Another anagram is: ",N)
        guess=input("Try again")
    print("\nWell done! That's just the ticket!")
    input("\nHere's another one!")
