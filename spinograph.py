import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

spiro = turtle.Turtle()
spiro.speed(10)
spiro.color("red")

spiro.penup()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] # Colors that appear

def draw_spinograph(R, r, d):
    
    loops = int(math.lcm(R, r) / r) # Calculates the number of loops needed to complete the pattern

    for t in range(0, loops * 360, 1):
        angle = math.radians(t)

        # Parametric equations of the spinograph
        x = (R - r) * math.cos(angle) + d * math.cos(((R - r)/r) * angle)
        y = (R - r) * math.sin(angle) - d * math.sin(((R - r) / r) * angle)

        spiro.color(colors[(t // 40) % len(colors)])
        spiro.goto(x, y)
        spiro.pendown()
    
    spiro.hideturtle()
    turtle.done


R = 202 # Radius of large fixed circle
r = 30 # Radius of small inner rolling circle
d = 20 # Distance between the pen point and the center of rolling circle

def main():
    draw_spinograph(R, r, d)

main()

