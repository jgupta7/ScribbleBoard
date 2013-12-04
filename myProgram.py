#Jason Gupta
#902983368; jgupta7@gatech.edu
#I worked on this homework assignment alone, using only this semester's course materials.
#
#Program: Scribble Board!!
#This program is very similar to paint. It allows you to create simple objects in different colors. You can ever make text, erase, and free draw!
#This program works by sensing your mouse movement constantly through a while loop. Once your move moves to the toolbar area, based on where it is, the code for that tool is executed.
#If your next click is on the tool, the program registers this and allows you to use the properties of that shape to create it on the canvas, using the Graphics module.
#The pen tool works by tracking the mouse movement on click and before release. Each point is added to a list. This list is then iterated through to create curves which smoothly connect the points.
#The circle tool works by using the pythagorean theorm to determine the radius of the circle, and then making it using the Graphics module.
#The colors work through a global color variable. This variable is a string and changes based on which color is chosen. It is set as the color for each tool, and is defaulted at black.
#
#NOTE- Please refer to the instructional video/readme file to understand how to use the program properly!!
#
#I got the idea for this program because I recently bought an iPad. I had a blast playing with the many drawing programs and was inspired to make my own.
#Due to my limited knowledge of python, there are a couple parts of the program that are not exceptionally user friendly, but it is easy to get used to, and it works well after that!
#

from Graphics import *
from Myro import *
import math


scribWin = Window("Scribble Board", 1040, 640)
scribWin.setBackground(makeColor(244, 244, 244))
toolbarTxt = Text((92,38), "Toolbar:")
toolbarTxt.fill = Color("brown")
toolbarTxt.fontSize = 35
toolbarTxt.draw(scribWin)
#make the toolbar
pencil = makePicture("pencil.png")
pencil.draw(scribWin)
pencil.move(160,0)
eraser = makePicture("eraser.png")
eraser.draw(scribWin)
eraser.move(240,0)
rect = makePicture("rect.png")
rect.draw(scribWin)
rect.move(320,0)
line = makePicture("line.png")
line.draw(scribWin)
line.move(400,0)
circle = makePicture("circle.png")
circle.draw(scribWin)
circle.move(480,0)
#make color swatches
colorTxt = Text((600,38),"Colors!")
colorTxt.rotate(45)
colorTxt.fill = makeColor("brown")
colorTxt.fontSize = 26
colorTxt.draw(scribWin)
white = makePicture("white.png")
white.draw(scribWin)
white.move(640,0)
red = makePicture("red.png")
red.draw(scribWin)
red.move(680,0)
orange = makePicture("orange.png")
orange.draw(scribWin)
orange.move(720,0)
yellow = makePicture("yellow.png")
yellow.draw(scribWin)
yellow.move(760,0)
green = makePicture("green.png")
green.draw(scribWin)
green.move(800,0)
blue = makePicture("blue.png")
blue.draw(scribWin)
blue.move(840,0)
purple = makePicture("purple.png")
purple.draw(scribWin)
purple.move(880,0)
black = makePicture("black.png")
black.draw(scribWin)
black.move(920,0)
#make text icon
text = makePicture("text.png")
text.draw(scribWin)
text.move(960,0)
#divider
divider = Line((0,75), (1040,75))
divider.fill = makeColor("black")
divider.draw(scribWin)
#close button
close = makePicture("close.png")
close.draw(scribWin)

#### MAIN CODE ####
color = "black"

global color
closeval = True
while closeval == True:
    mousePos = getMouseNow()

    def pencil():
        iterList = []
        mouseLoc = getMouse()
        if mouseLoc[0] in range(160,240) and mouseLoc[1] in range(0,75):
            mouseLoc1 = getMouse()
            if mouseLoc1[1] in range(75,640):
                while getMouseState() == "down":
                    currPos1 = getMouseNow()
                    currPos2 = getMouseNow()
                    currPos3 = getMouseNow()
                    currPos4 = getMouseNow()
                    iterList.append(currPos1)
                    iterList.append(currPos2)
                    iterList.append(currPos3)
                    iterList.append(currPos4)
                x = 1
                while x < len(iterList):
                    if x % 2 == 0 and x >= 4:
                        iterCurve = Curve((iterList[x-4]),(iterList[x-3]),(iterList[x-2]),(iterList[x-1]))
                        iterCurve.outline = makeColor(color)
                        iterCurve.draw(scribWin)

                    x = x + 1
    def eraser():
        mouseLoc = getMouse()
        if mouseLoc[0] in range(240,320) and mouseLoc[1] in range(0,75):
            mouseLoc1 = getMouse()
            if mouseLoc1[1] in range(75,640):
                mouseLoc2 = getMouse()
                if mouseLoc2[1] in range (75,640):
                    newRect = Rectangle((mouseLoc1[0],mouseLoc1[1]), (mouseLoc2[0], mouseLoc2[1]))
                    newRect.fill = makeColor(244, 244, 244)
                    newRect.outline = makeColor(244, 244, 244)
                    newRect.draw(scribWin)
    def rect():
        mouseLoc = getMouse()
        if mouseLoc[0] in range(320,400) and mouseLoc[1] in range(0,75):
            mouseLoc1 = getMouse()
            if mouseLoc1[1] in range(75,640):
                mouseLoc2 = getMouse()
                if mouseLoc2[1] in range (75,640):
                    newRect = Rectangle((mouseLoc1[0],mouseLoc1[1]), (mouseLoc2[0], mouseLoc2[1]))
                    newRect.fill = makeColor(color)
                    newRect.draw(scribWin)


    def line():
        mouseLoc = getMouse()
        if mouseLoc[0] in range(400,480) and mouseLoc[1] in range(0,75):
            mouseLoc1 = getMouse()
            if mouseLoc1[1] in range(75,640):
                mouseLoc2 = getMouse()
                if mouseLoc2[1] in range (75,640):
                    newLine = Line((mouseLoc1[0],mouseLoc1[1]), (mouseLoc2[0], mouseLoc2[1]))
                    newLine.outline = makeColor(color)
                    newLine.draw(scribWin)


    def circle():
        mouseLoc = getMouse()
        if mouseLoc[0] in range(480,560) and mouseLoc[1] in range(0,75):
            mouseLoc1 = getMouse()
            if mouseLoc1[1] in range(75,640):
                mouseLoc2 = getMouse()
                if mouseLoc2[1] in range (75,640):
                    yDif = abs(mouseLoc2[1] - mouseLoc1[1]) ** 2
                    xDif = abs(mouseLoc2[0] - mouseLoc1[0]) ** 2
                    hypo = math.sqrt((yDif + xDif))
                    if (mouseLoc1[1] - hypo) > 75 and (mouseLoc[1] + hypo) < 640:
                        newCircle = Circle((mouseLoc1[0],mouseLoc1[1]), hypo)
                        newCircle.fill = makeColor(color)
                        newCircle.draw(scribWin)
    def text():
        mouseLoc = getMouse()
        if mouseLoc[0] in range(960,1040) and mouseLoc[1] in range(0,75):
            mouseLoc1 = getMouse()
            if mouseLoc1[1] in range(75,640):
                textInput = input("What text do you want to enter?")
                fontInput = int(input("What size font? (Enter a number 8-40)"))
                if fontInput in range(8,41):
                    newText = Text((mouseLoc1[0],mouseLoc1[1]),textInput)
                    newText.fill = makeColor(color)
                    newText.fontSize = fontInput
                    newText.draw(scribWin)
                else:
                    print("Your font entry was not in range.")

    def detectColor():

        global color
        whiteX = range(640,680)
        redX = range(680,720)
        orangeX = range(720,760)
        yellowX = range(760,800)
        greenX = range(800,840)
        blueX = range(840,880)
        purpleX = range(880,920)
        blackX = range(920,960)
        y = range(0,75)

        mouseLoc = getMouse()
        if mouseLoc[0] in whiteX and mouseLoc[1] in y:
            color = "white"

        elif mouseLoc[0] in redX and mouseLoc[1] in y:
            color = "red"

        elif mouseLoc[0] in orangeX and mouseLoc[1] in y:
            color = "orange"

        elif mouseLoc[0] in yellowX and mouseLoc[1] in y:
            color = "yellow"

        elif mouseLoc[0] in greenX and mouseLoc[1] in y:
            color = "green"

        elif mouseLoc[0] in blueX and mouseLoc[1] in y:
            color = "blue"

        elif mouseLoc[0] in purpleX and mouseLoc[1] in y:
            color = "purple"

        elif mouseLoc[0] in blackX and mouseLoc[1] in y:
            color = "black"

    def close():
        mouseLoc = getMouse()
        global closeval
        if mouseLoc[0] in range(0,30) and mouseLoc[1] in range(0,75):
            scribWin.close()
            closeval == False
            


    #call toolbar functions

    if mousePos[0] in range(640,960) and mousePos[1] in range(0,75):
        detectColor()
    elif mousePos[0] in range(160,240) and mousePos[1] in range(0,75):
        pencil()
    elif mousePos[0] in range(240,320) and mousePos[1] in range(0,75):
        eraser()
    elif mousePos[0] in range(320,400) and mousePos[1] in range(0,75):
        rect()
    elif mousePos[0] in range(400,480) and mousePos[1] in range(0,75):
        line()
    elif mousePos[0] in range(480,560) and mousePos[1] in range(0,75):
        circle()
    elif mousePos[0] in range(960,1040) and mousePos[1] in range(0,75):
        text()
    elif mousePos[0] in range(0,30) and mousePos[1] in range(0,75):
        close()
