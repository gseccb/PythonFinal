# I pledge my honor I have abdied by the Stevens Honor System Elliott Braverman
import random
from sys import exit


class b():
    def __init__(self, spaces=9):
        self.gb = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.s = spaces

    def Pp(self):
        print("   0   1   2  ")
        print("0 ", self.gb[0][0], " ", self.gb[0][1], " ", self.gb[0][2])
        print("1 ", self.gb[1][0], " ", self.gb[1][1], " ", self.gb[1][2])
        print("2 ", self.gb[2][0], " ", self.gb[2][1], " ", self.gb[2][2])

    def Move(self, player, x=0, y=0):
        x = int(x)
        y = int(y)
        if(x<3 and y<3):
            if (self.gb[x][y] == "-"):
                self.s -= 1
                self.gb[x][y] = player
            else:
                print("Invalid Response Try again")
                self.Pp()
                x = input()
                y = input()
                self.Move(player, x, y)        
        else:
            print("Invalid Response Try again")
            self.Pp()
            x = input()
            y = input()
            self.Move(player, x, y)

    def Checkwin(self):
        if (self.gb[0][0] == self.gb[0][1] and self.gb[0][1] == self.gb[0][2] and self.gb[0][2] != "-") or (self.gb[1][0] == self.gb[1][1] and self.gb[1][1] == self.gb[1][2] and self.gb[1][2] != "-") or (self.gb[2][0] == self.gb[2][1] and self.gb[2][1] == self.gb[2][2] and self.gb[2][2] != "-") or (self.gb[0][0] == self.gb[1][0] and self.gb[1][0] == self.gb[2][0] and self.gb[2][0] != "-") or (self.gb[0][1] == self.gb[1][1] and self.gb[1][1] == self.gb[2][1] and self.gb[2][1] != "-") or (self.gb[0][2] == self.gb[1][2] and self.gb[1][2] == self.gb[2][2] and self.gb[2][2] != "-") or (self.gb[0][0] == self.gb[1][1] and self.gb[1][1] == self.gb[2][2] and self.gb[2][2] != "-") or (self.gb[2][0] == self.gb[1][1] and self.gb[1][1] == self.gb[0][2]) and self.gb[0][2] != "-":
            return True
        return False

    def MakeMove(self, player, x, y):
        self.Move(player, x, y)
        self.Pp()
        if (self.Checkwin()):
            print(player, " Wins!")
            exit()


def ComputerMove():
    if (board.s == 0):
        print("Tie")
        exit()
    move = random.randint(0, board.s)
    x = 0
    y = 0
    counter = 0
    while counter < move:
        if (x == 3):
            x = 0
            y += 1
        if (board.gb[x][y] == "-"):
            counter += 1
        if not counter == move:
            x += 1
    board.MakeMove(player2, x, y)


print("Hello, this is Tic Tac Toe")
TicTacToe = True
while TicTacToe:
    # choice 1 or 2 players used to only accept numbers
    print("One or Two Players?")
    temp = input()
    if (temp == "one") or (temp == "One") or (temp == "ONE"):
        temp = "1"
    if (temp == "two") or (temp == "Two") or (temp == "TWO"):
        temp = "2"
    if (temp == "1") or (temp == "2"):
        break
    else:
        print("Invalid response")
print("Heads Or Tails")
Coin = ["Heads", "Tails"]
temp1 = random.choice(Coin)
temp2 = input()
CW = False
if (temp2 == temp1) or (temp2 == "heads" and temp1 == "Heads") or (temp2 == "tails" and temp1 == "Tails") or (temp2 == "HEADS" and temp1 == "Heads") or (temp2 == "TAILS" and temp1 == "Tails"):
    # Coin flip to see who goes first used to be case sensitive
    print("You go First")
    CW = True
else:
    print("Opponent Goes First")

if (temp == "1"):  # choice in what you're represented by on the board
    player1 = "aa"
    while len(player1) > 1:
        print("what is your symbol?")
        player1 = input()
        if (len(player1) > 1):
            print("invalid length try again")
    player2 = "o"
else:
    player1 = "aa"
    while len(player1) > 1:
        print("what is your symbol?")
        player1 = input()
        if (len(player1) > 1):
            print("invalid length try again")
    player2 = "aa"
    while len(player2) > 1:
        print("what is your symbol?")
        player2 = input()
        if (len(player2) > 1):
            print("invalid length try again")

board = b()
board.Pp()
if (CW):
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
    else:
        ComputerMove()
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
    else:
        ComputerMove()
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
    else:
        ComputerMove()
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
    else:
        ComputerMove()
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (board.Checkwin() == False):
        print("Tie")
        exit()
else:
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
    else:
        ComputerMove()
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
    else:
        ComputerMove()
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
    else:
        ComputerMove()
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
    else:
        ComputerMove()
    print("where would you like to move Player 1?")
    x = input()
    y = input()
    board.MakeMove(player1, x, y)
    if (temp == "2"):
        print("where would you like to move Player 2?")
        x = input()
        y = input()
        board.MakeMove(player2, x, y)
        if (board.Checkwin() == False):
            print("Tie")
            exit()
    else:
        ComputerMove()
