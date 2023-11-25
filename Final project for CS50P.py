import time
import random
def kbc():

            print("You selected KBC")
            print(" ")
            print(" ")
            import random
            count = 0
            if count > 0:
                print(f"You secured at {money}")
            questions = [
                        ["who is the president of the india?",
                        "narendra", "rahul", "Indira", "Manmohan", "a"],
                        ["What is the capital of France?",
                        "Berlin", "Madrid", "Paris", "Rome", "c"],
                        ["Which gas is most abundant in Earth's atmosphere?",
                        "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "b"],
                        ["What is the largest planet in our solar system?",
                        " Earth", "Mars", "Jupitar", "Venus", "c"],
                        ["Who wrote the play Romeo and Juliet?",
                        "Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy", "b"],
                        ["In which year did Christopher Columbus first set foot in the Americas?",
                        "1942", "1517", "1620", "1776", "a"],
                        ["Which gas do plants absorb from the atmosphere during photosynthesis?",
                        "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "c"],
                        ["What is the currency of Japan?",
                        "Dollar", "Euro", "Yen", "Peso", "c"],
                        ["Which planet is known as the Red Planet?",
                        " Earth", "Mars", "Jupitar", "Venus", "b"],
                        ["Which country is known as the Land of the Rising Sun?",
                        "South Korea", "China", "Indira", "Japan", "d"],
                        ["What is the largest mammal in the world?",
                        "African Elephant", "Blue Whale", "Giraffe", "Hippopotamus", "b"],
                        ["Which of the following is a primary color?",
                        "Green", "Yellow", "Orange", "Black", "b"],
                        ]

            levels = [5000,"10 thousand","20 thousand","40 thousand","80 thousand","1.6 lakhs","3.2 lakhs","6.4 lakhs","12.8 lakhs","24 lakhs","50 lakhs","1 crore"]


            i = 0
            money = 0
            for i in range(0,len(questions)):
                question = questions[i]
                print(f"Question for rupees {levels[i]}")
                print(f"{question[0]}")
                print(f"a.{question[1]}")
                print(f"b.{question[2]}")
                print(f"c.{question[3]}")
                print(f"d.{question[4]}")

                reply = input("Enter your answer(a to d) ")
                if reply == question[-1]:
                    print("Correct answer")
                    totalprice = 0
                    print(f"total price  which you won is {levels[i]}")
                    money = levels[i]
                    print(" ")
                    print(" ")

                elif money == levels[-1]:
                    print(f"You won the price of",money)
                    break

                else:
                    print("Wrong answer!")
                    break
                if (money == levels[6] ):
                    # print(f"Now you secured at {money[6]}")
                    money == levels[6]
                elif (money == levels[1] ):
                    # print(f"Now you secured at {money[1]}")
                    money == levels[1]
                else :
                    pass
                count += 1

            time.sleep(3)

def snake_and_ladder():
            print("You selected Snake and Ladder")
            print(" ")
            print(" ")
            snake_and_ladder = {22: 7, 49: 12, 57: 76, 61: 54, 88: 4, 6: 14, 11: 28, 38: 59, 17: 74, 81: 98}

            player_position = 0

            while player_position < 100:
                print(f"You are at position {player_position}")

                dice = int(input("Enter the dice value (1-6): "))

                if dice < 1 or dice > 6:
                    print("Invalid input. Please enter a value between 1 and 6.")
                    continue

                player_position += dice

                if player_position in snake_and_ladder:
                    new_position = snake_and_ladder[player_position]
                    if new_position > player_position:
                        print(f"Congratulations, you climbed a ladder! You are now at position {new_position}")
                    else:
                        print(f"Oops, you landed on a snake! You are now at position {new_position}")
                    player_position = new_position

            if player_position >= 100:
                print("Congratulations! You won the game!")
            time.sleep(3)

def Tic_Tac_Toe():
            print("You are playing Tic, Tac, Toe")
            print(" ")
            print(" ")
            def sum(a, b, c ):
                return a + b + c

            def printBoard(xState, zState):
                zero = 'X' if xState[0] else ('O' if zState[0] else 0)
                one = 'X' if xState[1] else ('O' if zState[1] else 1)
                two = 'X' if xState[2] else ('O' if zState[2] else 2)
                three = 'X' if xState[3] else ('O' if zState[3] else 3)
                four = 'X' if xState[4] else ('O' if zState[4] else 4)
                five = 'X' if xState[5] else ('O' if zState[5] else 5)
                six = 'X' if xState[6] else ('O' if zState[6] else 6)
                seven = 'X' if xState[7] else ('O' if zState[7] else 7)
                eight = 'X' if xState[8] else ('O' if zState[8] else 8)
                print(f"{zero} | {one} | {two} ")
                print(f"--|---|---")
                print(f"{three} | {four} | {five} ")
                print(f"--|---|---")
                print(f"{six} | {seven} | {eight} ")

            def checkWin(xState, zState):
                wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
                for win in wins:
                    if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
                        print("X Won the match")
                        return 1
                    if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
                        print("O Won the match")
                        return 0
                return -1


            xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            turn = 1 # 1 for X and 0 for O
            print("Welcome to Tic Tac Toe")
            while(True):
                printBoard(xState, zState)
                if(turn == 1):
                    print("X's Chance")
                    value = int(input("Please enter a value(0 to 8): "))
                    xState[value] = 1
                else:
                    print("O's Chance")
                    value = int(input("Please enter a value(0 to 8): "))
                    zState[value] = 1
                cwin = checkWin(xState, zState)
                if(cwin != -1):
                    printBoard(xState, zState)
                    print("Match over")
                    break

                turn = 1 - turn

def Snake():
            print("You are playing Snake, Water and Gun game")
            print(" ")
            print(" ")
            print("Rules For game")
            rules = """Snake won against water,
Water won against Gun and
Gun won against Snake"""
            choice = """Enter quit for Quit Game
Enter your choice : """
            print(rules)
            while True:
                a = input(choice)
                game = ["Snake", "snake","Water","water","Gun", "gun", "Quit", "quit"]

                if a == game[0] or a == game[1]:
                    a = 1
                elif a== game[2] or a == game[3]:
                    a = 2
                elif a == game[4] or a==game[5]:
                    a = 3

                lst = [1,2,3]
                c = int(random.choice(lst))

                if a == c:
                    print("Mathch draw")

                elif a==1 and c==2:
                    print("You Win")

                elif a==1 and c==3:
                    print("You loss")

                elif a==2 and c==1:
                    print("You Loss")

                elif a==2 and c==3:
                    print("You win")

                elif a==3 and c==1:
                    print("You Win")

                elif a==3 and c==2:
                    print("You Loss")

                elif a == game[6] or game[7]:
                    break

                else :
                    print("Invalid input")

                if c == lst[0]:
                    c = game[0]
                elif c == lst[1]:
                    c = game[2]
                else :
                    c = game[2]

                if a == lst[0]:
                    a = game[0]
                elif a == lst[1]:
                    a = game[2]
                else:
                    a = game[4]
                print(f"Computer choose {c} and you choose {a}")
                print(" ")
                print(" ")
                print(" ")

            time.sleep(2)
            # else:
            #     print("Invalid Input")
            # time.sleep(2)
def main():
    a = """Enter 1 for kbc
Enter 2 For Snake and ladder
Enter 3 for Tic Tac Toe
Enter 4 for Snake, Water, Gun"""
    t = 2
    print(a)

    name = int(input("Enter the number for game : "))

    while True:

        if name == 1:
            kbc()

        elif name == 2:
            snake_and_ladder()

        elif name == 3:
            Tic_Tac_Toe()

        elif name == 4:
            Snake()

if __name__ == "__main__":
    main()
