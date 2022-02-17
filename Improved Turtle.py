from turtle import *
import random
import time


x = random.randint(30, 180)  # picks a number between 30 and 180 for the angle.
y = 360 // x  # divides the angle by 360 so you get how many times the last loop loops.


# Asks for a number and takes that input to variable 'a'
a = int(input("How many snowflakes do you want?"))

# enables RGB
colormode(255)
speed(50)
Screen().bgcolor("gray")


# creates the 'snowflake' function which includes a loop in a loop
def snowflake(size):
    for i in range(3):
        for i in range(3):
            forward(10 * size / 3)
            backward(10 * size / 3)
            right(45)
        left(90)
        backward(30)
        left(x)
    right(90)
    forward(90)


# loops with the variable 'a' we got earlier
for i in range(a):
    pensize(random.randint(1, 5))
    r = random.randint(0, 255)  # Random number from 0-255 for RGB
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color(r, g, b)
    penup()
    goto(random.randint(-300, 300), random.randint(-300, 300))
    pendown()
    for i in range(y):
        size = random.randint(1, 5)
        snowflake(size)
        left(x)
time.sleep(1.5)  # Pauses for 1.5 seconds
penup()
goto(0, 0)
pendown()
color("black")
# It is indeed not christmas, don't know where these snowflakes are coming from
write("It isn't christmas..", align="center", font=("Arial", 30, "bold"))
done()
