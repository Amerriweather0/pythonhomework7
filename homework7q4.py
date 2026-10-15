
from graphics import *
import time


def main():
    height = float(input("Enter the initial height in meters: "))

    if height <= 0:
        print("Height must be greater than zero.")
        return

    win = GraphWin("Bouncing Ball", 500, 500)
    win.setCoords(0, 0, 1, height)

    radius = height * 0.02
    ball = Circle(Point(0.5, height - radius), radius)
    ball.setFill("red")
    ball.draw(win)

    # Draw the ground.
    ground = Line(Point(0, 0), Point(1, 0))
    ground.draw(win)

    current_height = height
    step = height / 100

    # Drop the ball and animate each bounce.
    while current_height >= 0.001:
        # Move the ball downward to the ground.
        while ball.getCenter().getY() > radius:
            center = ball.getCenter()
            new_y = max(radius, center.getY() - step)
            ball.move(0, new_y - center.getY())
            time.sleep(0.01)

        # Each bounce reaches 60% of the previous height.
        current_height = current_height * 0.60

        # Move the ball upward to the new bounce height.
        target_y = max(radius, current_height)

        while ball.getCenter().getY() < target_y:
            center = ball.getCenter()
            new_y = min(target_y, center.getY() + step)
            ball.move(0, new_y - center.getY())
            time.sleep(0.01)

    win.getMouse()
    win.close()


main()
