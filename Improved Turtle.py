from turtle import *
import random
import time

#Asks for a number and takes that input to variable 'x'
x = int(input("How many snowflakes do you want?"))

#enables RGB
colormode(255)
speed(50)
Screen().bgcolor("gray")

#creates the 'snowflake' function which includes a loop in a loop
def snowflake():
    for i in range(3):
        for i in range(3):
            forward(30)
            backward(30)
            right(45)
        left(90)
        backward(30)
        left(45)
    right(90)
    forward(90)

# loops with the variable 'x' we got earlier
for i in range(x):
    for i in range(8):
        snowflake()
        left(45)
    pensize(random.randint(1, 10))
    r = random.randint(0, 255) # Random number from 0-255 for RGB
    g = random.randint(0, 255) # ^
    b = random.randint(0, 255) # ^
    color(r, g, b)
    penup()
    goto(random.randint(-300, 300), random.randint(-300, 300))
    pendown()
time.sleep(1.5) # Pauses for 1.5 seconds
penup()
goto(0, 0)
pendown()
color("black")
# It is indeed not christmas, don't know where these snowflakes are coming from
write("It isn't christmas..", align="center", font=("Arial", 30, "bold"))
done()
