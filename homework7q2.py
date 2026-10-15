
from graphics import *
import math


def drawPolygon(n, radius, center):
    angle = 360 / n
    vertices = []

    for i in range(n):
        theta = math.radians(i * angle)
        x = center.getX() + radius * math.cos(theta)
        y = center.getY() + radius * math.sin(theta)
        vertices.append(Point(x, y))

    polygon = Polygon(vertices)
    return polygon


def buttonClicked(point, button):
    x = point.getX()
    y = point.getY()

    p1 = button.getP1()
    p2 = button.getP2()

    left = min(p1.getX(), p2.getX())
    right = max(p1.getX(), p2.getX())
    bottom = min(p1.getY(), p2.getY())
    top = max(p1.getY(), p2.getY())

    return left <= x <= right and bottom <= y <= top


def main():
    win = GraphWin("Polygon Drawer", 500, 400)
    win.setCoords(0, 0, 500, 400)

    label = Text(Point(100, 350), "Number of sides:")
    label.draw(win)

    sidesEntry = Entry(Point(200, 350), 5)
    sidesEntry.setText("5")
    sidesEntry.draw(win)

    button = Rectangle(Point(300, 330), Point(400, 370))
    button.setFill("lightblue")
    button.draw(win)

    buttonLabel = Text(Point(350, 350), "Graph")
    buttonLabel.draw(win)

    while True:
        click = win.getMouse()

        if buttonClicked(click, button):
            if buttonLabel.getText() == "Graph":
                try:
                    n = int(sidesEntry.getText())

                    if n < 3:
                        label.setText("Enter sides (3+):")
                        continue

                    polygon = drawPolygon(
                        n, 100, Point(250, 180)
                    )
                    polygon.setOutline("blue")
                    polygon.setWidth(2)
                    polygon.draw(win)

                    buttonLabel.setText("Exit")

                except ValueError:
                    label.setText("Enter a valid number:")
            else:
                break

    win.close()


main()
