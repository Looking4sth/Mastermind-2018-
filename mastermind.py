# masterMind.py
# CSC 110
# Hung Vu
# 12/10/18

# This module will simulate master mind game.

from random import*
from graphics import*

colorList = ["green","red","yellow","orange","pink","violet"]

def setting ():
    # Setting
    # turn
    win2 = GraphWin("masterMind", 600, 600)
    win2.setBackground("light blue")
    win2.setCoords(0,0,120,120)

    text5 = Text(Point(30,90), "Type in the turn limit, max is 17 (E.g: 6 => you need to find the secret code in 5 turns to win)")
    text5.setSize(10)
    text5.move(30,-20)
    text5.draw(win2)
    
    entry2 = Entry(Point(30,85),20)
    entry2.move(30,-20)
    entry2.draw(win2)
    
    # code length
    text6 = Text(Point(30,80), "Type in the code length (max is 10) ")
    text6.move(30,-20)
    text6.setSize(10)
    text6.draw(win2)

    text7 = Text(Point(60,40), "Click to continue")
    text7.setFill("Brown")
    text7.setStyle("bold italic")
    text7.setSize(10)
    text7.draw(win2)
                 
    
    entry3 = Entry(Point(30,75),20)
    entry3.move(30,-20)
    entry3.draw(win2)

    win2.getMouse()
    turn = entry2.getText()
    length = entry3.getText()
    win2.close()
    
    return turn,length

def generateSecretCode(codeLength):
    secretCode = []
    for i in range(codeLength):
        number = randrange(0,6)
        secretCode.append(colorList[number][0])
    #print (secretCode)
    return secretCode
    
    #tempSC = list(SC)
    #print(tempSC)
    #return tempSC

def copy(secretCode,codeLength):
    tempSCode = []
    for i in range (codeLength):
        tempSCode.append(secretCode[i])
    #print(tempSCode)
    return tempSCode

def drawBoard():
    # In-game
    win = GraphWin("masterMind", 600, 600)
    win.setBackground("light blue")
    win.setCoords(0,0,240,240)

    text = Text(Point(29,220), "List of color")
    text.move(29,0)
    text.draw(win)

    text1 = Text(Point(30,210),"green, red, yellow, orange, pink, violet")
    text1.move(30,0)
    text1.draw(win)

    text2 = Text(Point(30,200), "Type in the first letter of the color you choose (E.g: rrrr) ")
    text2.move(30,0)
    text2.setSize(9)
    text2.draw(win)

    text3 = Text(Point(90,220), "Click to check")
    text3.move(90,0)
    text3.setStyle("bold italic")
    text3.setFill("Brown")
    text3.draw(win)

    line = Line(Point (60,240), Point(60,0))
    line.move(60,0)
    line.setOutline("red")
    line.draw(win)

    return win
    #print(times)
    #print(right)

def winInfo(win,turn,codeLength):


    entry = Entry(Point(30,190),20)
    entry.move(30,0)
    entry.draw(win)


  
    for j in range (turn-1):
        for i in range (codeLength):
            circ = Circle(Point(15+10*i, 5+11*j),4)
            circ.draw(win)
            
    for j in range (turn-1):
        for i in range (codeLength):
            circ1 = Circle(Point(135+10*i, 5+11*j),2)
            circ1.draw(win)
    win.getMouse()
    
    inputGuess = entry.getText()
    listGuess=[]
    colorGuess=[]
    letterList=[]

    for i in range(codeLength):
        listGuess.append(inputGuess[i])

    for i in range(codeLength):
        colorGuess.append(inputGuess[i])
    
    for i in range(6):
        letterList.append(colorList[i][0])
        for j in range(len(colorGuess)):
            if colorGuess[j] == letterList[i]:
                #print(colorGuess[j])
                colorGuess[j] = colorList[i]
        
    #print(letterList)
    #print(listGuess)
    #print(colorGuess)   
    #colorGuess = inputGuess.split(",")
    #listGuess = []
    
    #for i in range(codeLength):
        #listGuess.append(inputGuess.split(",")[i][0])

    return listGuess, colorGuess


def updateWin(window,times,check,colorGuess,codeLength,turnNumber):
    j = times
    for i in range (codeLength):
        circ = Circle(Point(15+10*i, 5+11*(j-1)),4)
        circ.setFill(colorGuess[i])
        circ.draw(window)
    #print(check)

    black,white = check.count("black"), check.count("white")
    for i in range (black):
        circ1 = Circle(Point(135+10*i, 5+11*(j-1)),2)
        circ1.setFill("black")
        circ1.draw(window)
    if black == 0:
        for n in range(white):
            circ2 = Circle(Point(135+10*n, 5+11*(j-1)),2)
            circ2.setFill("White")
            circ2.draw(window)
    else:
        for n in range(white):
            circ2 = Circle(Point(135+10*(black+n), 5+11*(j-1)),2)
            circ2.setFill("White")
            circ2.draw(window)
    

    if black == codeLength:
        text4 = Text(Point(90,105), "You won")
        text4.move(90,105)
        text4.setStyle("bold italic")
        text4.setFill("Brown")
        text4.draw(window)

        text7 = Text(Point(90,95), "Click to exit")
        text7.move(90,105)
        text7.setStyle("bold italic")
        text7.setFill("Brown")
        text7.draw(window)

        window.getMouse()
        window.close()

    if black < codeLength and times == (turnNumber-1):
        text5 = Text(Point(90,105), "You lost")
        text5.move(90,105)
        text5.setStyle("bold italic")
        text5.setFill("Brown")
        text5.draw(window)

        text6 = Text(Point(90,95), "Click to restart")
        text6.move(90,105)
        text6.setStyle("bold italic")
        text6.setFill("Brown")
        text6.draw(window)
        

    
    #print(turnNumber)
    #print(times)

    
    #print(len(check))
    #print(black,white)
        
def checkList(secretList,guessList):
    black = 0
    for i in range(len(secretList)):
        if secretList[i] == guessList[i]:
            black = black + 1
            secretList[i] = "black"
            guessList[i] = "black"
    for i in range(len(secretList)):
         if secretList[i] != "black" :
            for j in range(len(secretList)):
                if secretList[i] == guessList[j]:
                    secretList[i] = "white"
                    guessList[j] = "white"
    black , white = guessList.count("black"), guessList.count("white")
    #print(guessList)
    #print(black, white)
    
    result = "black "*black+ "white "*white
    result = result.split(" ")
    
    #print(result)
    return black, white, result

def main():
        
    turn = 1
    black = 0
    
    turnNumber, codeLength = setting()
    codeLength = int(codeLength)
    turnNumber = int(turnNumber)
    #print (turnNumber)
    win = drawBoard()

    secret = generateSecretCode(codeLength)
    #print(secret)

    while black < codeLength and turn < turnNumber:
        
        guess, color = winInfo(win,turnNumber,codeLength)
        temp = copy(secret,codeLength)
        #print (temp)
        #print(len(secret))
        #print(len(temp))
        
        black, white, check = checkList(temp,guess)
        
        updateWin(win,turn,check,color,codeLength,turnNumber)
        #print(check)
        #print(check)
        #print(check)
        #print(len(check))
        turn = turn + 1

    while black < codeLength and turn == turnNumber:
        win.getMouse()
        main()




main()
