import turtle
import winsound
import random

speedcon = 1
speed = [random.randrange(20, 80)/100 * speedcon, random.randrange(20, 80)/100 * speedcon]

okno = turtle.Screen()
okno.title("Ping Pong")
okno.bgcolor('black')
okno.setup(width=1920, height=1080)
okno.tracer(0)

# Paletka 1
paletka_1 = turtle.Turtle()
paletka_1.speed(0)
paletka_1.shape("square")
paletka_1.shapesize(5, 0.5)
paletka_1.color("white")
paletka_1.penup()
paletka_1.goto(-350, 10)

# Paletka 2
paletka_2 = turtle.Turtle()
paletka_2.speed(0)
paletka_2.shape("square")
paletka_2.shapesize(5, 0.5)
paletka_2.color("white")
paletka_2.penup()
paletka_2.goto(350, 10)

# Kula
kulka = turtle.Turtle()
kulka.speed(0)
kulka.shape("circle")
kulka.color("white")
kulka.penup()
kulka.goto(0, 0)
kulka.dx = speed[0]
kulka.dy = speed[1]

# Ścian 1
wall = turtle.Turtle()
wall.speed(0)
wall.shape("square")
wall.shapesize(0.1, 40)
wall.color("white")
wall.penup()
wall.goto(0, 301)

#Ściana 2
wall_2 = turtle.Turtle()
wall_2.speed(0)
wall_2.shape("square")
wall_2.shapesize(0.1, 40)
wall_2.color("white")
wall_2.penup()
wall_2.goto(0, - 301)

# Bramka 1
bramka_1 = turtle.Turtle()
bramka_1.speed(0)
bramka_1.shape("square")
bramka_1.shapesize(30, 0.01)
bramka_1.color("red")
bramka_1.penup()
bramka_1.goto(-401,0)

# Bramka 2
bramka_2 = turtle.Turtle()
bramka_2.speed(0)
bramka_2.shape("square")
bramka_2.shapesize(30, 0.01)
bramka_2.color("red")
bramka_2.penup()
bramka_2.goto(401, 0)

#Linia boiska
linia = turtle.Turtle()
linia.speed(0)
linia.shape("square")
linia.shapesize(30,0.01)
linia.color("white")
linia.penup()
linia.goto(0, 0)

#Boisko circle
circle = turtle.Turtle()
circle.speed(5)
circle.goto(0, -100)
circle.color("white")
circle.circle(100)
circle.penup()
circle.hideturtle()

# Wyniik
wynik = turtle.Turtle()
wynik.hideturtle()
wynik.speed(0)
wynik.penup()
wynik.color("white")
wynik.goto(0, 305)
punkty_1 = [0]
punkty_2 = [0]
wynikx = [wynik.xcor()]
wynik.write(str(punkty_1[0]) + ' SCORE ' + str(punkty_2[0]), align="center", font=("Verdana", 50, 'normal'))

# Start
game_start = turtle.Turtle()
game_start.hideturtle()
game_start.speed(0)
game_start.penup()
game_start.color("white")
game_start.goto(0, -350)
game_start.write("Press space bar to play", align="center", font=("Vardena", 30, "normal"))

#Funkcje
def paletka_1_up():
    y = paletka_1.ycor()
    if y <= 240:
        y += 20
        paletka_1.sety(y)
    else:
        return

def paletka_1_down():
    y = paletka_1.ycor()
    if -240 <= y:
        y -= 20
        paletka_1.sety(y)
    else:
        return

def paletka_2_up():
    y = paletka_2.ycor()
    if y <= 240:
        y += 20
        paletka_2.sety(y)
    else:
        return

def paletka_2_down():
    y = paletka_2.ycor()
    if -240 <= y:
        y -= 20
        paletka_2.sety(y)
    else:
        return

def gol(punkty):
    punkty[0] += 1
    wynik.clear()
    wynik.write(str(punkty_1[0]) + ' SCORE ' + str(punkty_2[0]), align="center", font=("Verdana", 50, 'normal'))
    kulka.goto(0, 0),
    paletka_1.goto(-350, 10)
    paletka_2.goto(350, 10)
    kulka.dx *= -1
    kulka.dx /= abs(kulka.dx) / (random.randrange(20, 80) / 100 * speedcon)
    kulka.dy /= abs(kulka.dy) / (random.randrange(20, 80) / 100 * speedcon)

def odbicie(kuly):
    kulka.sety(kuly)
    kulka.dy *= -1
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

def odbicie_paletki(paletkay,fast):
    kulka.setx(paletkay)
    kulka.dx *= -1
    kulka.dx += fast
    kulka.dy += fast
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

# Klawisze
okno.listen()
okno.onkeypress(paletka_1_up, "w")
okno.onkeypress(paletka_1_down, "s")
okno.onkeypress(paletka_2_up, "Up")
okno.onkeypress(paletka_2_down, "Down")


start = [0]
def start_game():
    start[0] += 1
    game_start.clear()
okno.onkeypress(start_game, "space")
while start[0] == 0:
    okno.update()

while True:
    okno.update()
    # Kulka Lata
    kulka.setx(kulka.xcor() + kulka.dx)
    kulka.sety(kulka.ycor() + kulka.dy)
    #Kulka vs ściany
    if kulka.ycor() > 290:
        odbicie(290)
    if kulka.ycor() < -290:
        odbicie(-290)
    if kulka.xcor() > 390:
        gol(punkty_1)
    if kulka.xcor() < -390:
        gol(punkty_2)
    #Kulka vs paletki
    if -350 <= int(kulka.xcor()) <= -340 and paletka_1.ycor() - 60 < kulka.ycor() < paletka_1.ycor() + 60:
        odbicie_paletki(-330, 0.1)
    if 350 >= int(kulka.xcor()) >= 340 and paletka_2.ycor() - 60 < kulka.ycor() < paletka_2.ycor() + 60:
        odbicie_paletki(330, -0.1)