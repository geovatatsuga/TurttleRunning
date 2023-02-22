import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow',
          'black', 'purple', 'pink', 'brown', 'cyan']
COLORS_PT = {'red': 'Vermelho', 'Green': 'Verde', 'blue': 'Azul', 'orange': 'Laranja', 'yellow': 'Amarelo',
             'black': 'Preto', 'Purple': 'Roxo', 'pink': 'Rosa', 'rown': 'Marrom', 'cyan': 'Ciano'}

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Digite o número de tartarugas (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Coloque um número... Tente denovo"!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Número não está entre 2-10... Tente denovo!')


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Corrida de tartarugas!')

    finish_line = turtle.Turtle(visible=False)
    finish_line.speed('fastest')
    finish_line.penup()
    finish_line.goto(-WIDTH//2, HEIGHT//2 - 20)
    finish_line.pensize()
    finish_line.pendown()
    finish_line.setheading(0)
    finish_line.color('black')
    finish_line.begin_fill()
    finish_line.forward(WIDTH)
    finish_line.setheading(-90)
    finish_line.forward(40)
    finish_line.setheading(180)
    finish_line.forward(WIDTH)
    finish_line.setheading(90)
    finish_line.forward(40)
    finish_line.end_fill()


racers = get_number_of_racers()
init_turtle()


random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("O vencedor é a tartaruga com a cor:", COLORS_PT[winner])
pen = turtle.Turtle(visible=False)
pen.penup()
pen.goto(0, 0)
pen.write(f"A tartaruga {COLORS_PT[winner]} é a VENCEDORA!", align="center", font=("Arial", 24, "normal"))


time.sleep(5)
