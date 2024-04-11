import random

possibleColors = ["R", "B", "G", "Y", "W", "P", "O"]

def createCode(nFields, nColors):
    code = [None for _ in range(nFields)]
    if nColors < 1 or nColors > len(possibleColors):
        print("Invalid number of colors")
        return
    else:
        for i in range(len(code)):
            code[i] = random.choice(possibleColors[:nColors])
    return code

def checkInput(code, input):
    if len(code) != len(input):
        return "Invalid input"
    WrongColorWrongSpot = 0
    correctColorWrongSpot = 0
    correctColorCorrectSpot = 0

    for i in range(len(input)):
        char = input[i]
        if char in code:
            if char == code[i]:
                correctColorCorrectSpot += 1
            else:
                correctColorWrongSpot += 1
        else:
            WrongColorWrongSpot += 1
    print(correctColorCorrectSpot, correctColorWrongSpot, WrongColorWrongSpot)    
    if correctColorCorrectSpot == len(code):
        return "You won"
    else:
        return f"{correctColorCorrectSpot} color(s) were correct and in correct spot, {correctColorWrongSpot} color(s) were correct but in the wrong spot"


def playGame():
    hasNotWon = True
    amountFields = int(input("Enter the amount of fields: "))
    amountColors = int(input(f"Enter the amount of colors (max {len(possibleColors)}): "))
    if amountFields < 1:
        print("Invalid amount of fields")
        return
    print(f"The possible colors are {possibleColors[:amountColors]}")
    code = createCode(amountFields, amountColors)
    attempts = 0
    while hasNotWon:
        attempts += 1
        input_From_User = input("Enter your guess: ")
        feedback = checkInput(code, input_From_User)
        if feedback == "You won":
            hasNotWon = False
            print(f"You won on attempt {attempts}")
        else: 
            print(f"On attempt nr{attempts}, {feedback}")

playGame()