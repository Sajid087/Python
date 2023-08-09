import random
#Here we start the game and give a choice of 1 or 2 player
print("Let's play Rock-Paper-Scissors\nChoose\n1-player: 1\n2-player: 2\n")
q = int(input())

#Here we twke the number of the rounds os the game
print("How many rounds you want to play? Enter an odd number")
j = int(input())
print("The Number of rounds are ",j)
print("\n")

i = 0
x = 0 #Player 1 points
y = 0 #Computer or Player 2 points

# 1 Player
if q == 1:
    print("Rock=1\nPaper=2\nScissors=3\n")

    #We take the name of player 1
    print("Enter your name")
    pla1 = input()
    print("The player name is "+pla1)

    while i<j:
        print("\nRound", i+1)

        #We take the input of the player 1
        a = int(input("\nEnter your choose"))

        #the computer generate a random number
        b = random.randint(1,3)

        if a == 1 and b == 1:
            print("It's a tie, you both have chosen rock")
        elif a == 1 and b == 2:
            print("Computer has won the round, "+pla1+" have chosen rock and the computer have chosen paper")
            y += 1
        elif a == 1 and b == 3:
            print(pla1+" has won the round, "+pla1+" have chosen rock and the computer have chosen scissor")
            x += 1
        elif a == 2 and b == 1:
            print(pla1+" has won the round, "+pla1+" have chosen paper and the computer have chosen rock")
            x += 1
        elif a == 2 and b == 2:
            print("It's a tie, you both have chosen paper")
        elif a == 2 and b == 3:
            print("Computer has won the round, "+pla1+" have chosen paper and the computer have chosen scissor")
            y += 1 
        elif a == 3 and b == 1:
            print("Computer has won the round, "+pla1+" have chosen scissor and the computer have chosen rock")
            y += 1
        elif a == 3 and b == 3:
            print("It's a tie, you both have chosen scissor")
        elif a == 3 and b == 2:
            print(pla1+" has won the round, "+pla1+" have chosen scissor and the computer have chosen paper")
            x += 1 
        i += 1

    if x > y:
        print("\n"+pla1+" have won the game")
    elif x==y:
        print("\nThe game is a tie")
    else:
        print("\nComputer have won the game")

# 2 Player 
else:
    print("Rock=1\nPaper=2\nScissors=3\n")

    #We take the name of player 1
    print("Enter Player 1 name")
    pla1 = input()
    print("The player 1 name is "+pla1)

    #We take the name of player 2
    print("\nEnter player 2 name")
    pla2 = input()
    print("The player 2 name is "+pla2)


    while i<j:
        print("\nRound", i+1)

        #We take the input of the Player 1
        a = int(input("Enter 1st player choose"))

        #We take the input of the Player 2
        b = int(input("Enter 2nd player choose"))

        if a == 1 and b == 1:
            print("It's a tie, you both have chosen rock")
        elif a == 1 and b == 2:
            print(pla2+" has won the round, "+pla1+" have chosen rock and the "+pla2+" have chosen paper")
            y += 1
        elif a == 1 and b == 3:
            print(pla1+" has won the round, "+pla1+" have chosen rock and the "+pla2+" have chosen scissor")
            x += 1
        elif a == 2 and b == 1:
            print(pla1+" has won the round, "+pla1+" have chosen paper and the "+pla2+" have chosen rock")
            x += 1
        elif a == 2 and b == 2:
            print("It's a tie, you both have chosen paper")
        elif a == 2 and b == 3:
            print(pla2+" has won the round, "+pla1+" have chosen paper and the "+pla2+" have chosen scissor")
            y += 1 
        elif a == 3 and b == 1:
            print(pla2+" has won the round, "+pla1+" have chosen scissor and the "+pla2+" have chosen rock")
            y += 1
        elif a == 3 and b == 3:
            print("It's a tie, you both have chosen scissor")
        elif a == 3 and b == 2:
            print(pla1+" has won the round, "+pla1+" have chosen scissor and the "+pla2+" have chosen paper")
            x += 1 
        i += 1
    
    if x > y:
        print("\n"+pla1+" have won the game")
    elif x==y:
        print("\nThe game is a tie")
    else:
        print("\n"+pla2+" have won the game")