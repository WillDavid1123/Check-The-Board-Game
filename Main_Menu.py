from graphics import GraphWin, Rectangle, Text, Point, color_rgb, Image

def mainMenu (window):

    win = window
    #Background
    background = Image(Point(50,50), "MMBackground.gif")
    background.draw(win)


    #Title Text
    titleBox = Rectangle(Point(10,95), Point(90, 75))
    titleBox.setFill(color_rgb(132,132,130))
    titleBox.setOutline("white")
    titleBox.draw(win)
    titleText = Text(Point(50, 85), "CHECK THE BOARD")
    titleText.setSize(35)
    titleText.draw(win)

    #Start Button
    startBox = Rectangle(Point(30, 65), Point(70, 55))
    startBox.setFill(color_rgb(163,163,161))
    startBox.setOutline("white")
    startBox.draw(win)
    startText = Text(Point(50, 60), "Level Select")
    startText.setSize(20)
    startText.draw(win)

    #Options Button
    optionsBox = Rectangle(Point(30, 50), Point(70, 40))
    optionsBox.setFill(color_rgb(163,163,161))
    optionsBox.setOutline("white")
    optionsBox.draw(win)
    optionsText = Text(Point(50, 45), "Options")
    optionsText.setSize(20)
    optionsText.draw(win)

    #Help Button
    helpBox = Rectangle(Point(30, 35), Point(70, 25))
    helpBox.setFill(color_rgb(163,163,161))
    helpBox.setOutline("white")
    helpBox.draw(win)
    helpText = Text(Point(50, 30), "Help")
    helpText.setSize(20)
    helpText.draw(win)

    #Exit Button
    exitBox = Rectangle(Point(30, 20), Point(70, 10))
    exitBox.setFill(color_rgb(163,163,161))
    exitBox.setOutline("white")
    exitBox.draw(win)
    exitText = Text(Point(50, 15), "Exit")
    exitText.setSize(20)
    exitText.draw(win)
    
    win.getMouse()


def main():
    w = 1000
    h = 650
    win = GraphWin("Check The Board", w , h)
    win.setCoords(0.0 ,0.0 ,100.0, 100.0)
    mainMenu(win)

if __name__ == "__main__":
    main()