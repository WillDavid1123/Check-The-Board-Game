from graphics import *

def main():
    width = 1000
    height = 600
    win = GraphWin("Check The Board", width, height)
    win.setCoords(0, 0, 100, 100)
    text = win.getMouse()


if __name__ == "__main__":
    main()