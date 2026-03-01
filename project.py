import turtle
import random
screen = turtle.Screen()
screen.bgcolor('#242124')       
alex = turtle.Turtle()
alex.speed(0)
alex.color("white")


def draw_star(t, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(random.randint(0, 360))
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(10)
        t.right(144)
    t.end_fill()

for i in range(40):
    x = random.randint(-800, 0)
    y = random.randint(0, 800)
    draw_star(alex, x, y)

for i in range(40):
    x = random.randint(0, 800)
    y = random.randint(0, 800)
    draw_star(alex, x, y)

for i in range(40):
    x = random.randint(-800, 800)
    y = random.randint(-800, 0)
    draw_star(alex, x, y)

def draw_frame(t):
    t.penup()
    t.goto(-350, -400) 
    t.setheading(0)
    t.color("white")
    t.begin_fill()
    
    for _ in range(2):
        t.forward(700)
        t.left(90)
        t.forward(800)
        t.left(90)
    t.end_fill()

    t.goto(-310, -300)
    t.color("light blue") 
    t.begin_fill()
    for _ in range(2):
        t.forward(620)
        t.left(90)
        t.forward(660)
        t.left(90)
    t.end_fill()

draw_frame(alex)

alex.penup()
alex.goto(0, -250) 
alex.pendown()
alex.width(10)

alex.color('white')
for i in range(25):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    
    alex.penup()
    alex.goto(x, y)
    
    alex.setheading(-45)
    alex.pendown()
    alex.forward(10)
    alex.left(90)
    alex.forward(10)
    alex.penup()

alex.width(1)

alex.color("black")
alex.fillcolor("bisque") 
trapezoid_corners = [(-20, -250), (20, -250), (100, 50), (-100, 50)]

alex.penup()
alex.goto(trapezoid_corners[0]) 
alex.pendown()

alex.fillcolor("bisque") 
alex.begin_fill()

for i in range(4):
    x, y = trapezoid_corners[i]
    alex.goto(x, y)

alex.goto(trapezoid_corners[0])
alex.end_fill()


alex.width(5) 
alex.color('forest green')

alex.penup()
alex.goto(-80, 50)
alex.setheading(110)
alex.pendown()
alex.forward(60)

alex.penup()
alex.goto(-40, 50) 
alex.setheading(110) 
alex.pendown()
alex.forward(20)

alex.penup()
alex.goto(0, 50)
alex.setheading(90)  
alex.pendown()
alex.forward(70)

alex.penup()
alex.goto(40, 50)
alex.setheading(65)  
alex.pendown()
alex.forward(20)

alex.penup()
alex.goto(80,50)
alex.setheading(65)
alex.pendown()
alex.forward(60)

alex.width(1) 

def draw_heart(t, x, y, words):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    
    t.color("red")
    t.begin_fill()
    t.left(50)
    t.forward(30)      
    t.circle(15, 200)  
    t.right(140)
    t.circle(15, 200)
    t.forward(30)
    t.end_fill()
    
    t.penup()
    t.goto(x, y + 8) 
    t.setheading(0)
    t.color("pink")
    t.begin_fill()
    t.left(50)
    t.forward(22)      
    t.circle(11, 200)  
    t.right(140)
    t.circle(11, 200)
    t.forward(22)
    t.end_fill()
    
    t.penup()
    t.goto(x, y + 25) 
    t.color("black")
    t.write(words, align="center", font=("Comic Sans MF", 10))

draw_heart(alex, -95, 100, "Empathetic")  
draw_heart(alex, -40, 60, "Caring")
draw_heart(alex, 6, 110, "Smart")
draw_heart(alex, 50, 60, "Charming")
draw_heart(alex, 110, 100, "Mine")   


alex.goto(-100, 20) 
alex.setheading(0)  
alex.pendown()

alex.color("red")
alex.begin_fill()
for i in range(2):
    alex.forward(200) 
    alex.left(90)
    alex.forward(30)  
    alex.left(90)
alex.end_fill()

alex.penup()
alex.goto(0, 25)    
alex.color("white") 
alex.write("Everything I Love About You", align="center", font=("Arial", 13, "bold"))

dot_locations = [
    (-50,7),(0, -50), (40, -100), (-40, -100), (50,7),
    (0, -150), (26, -200), (-26, -200)
]
for x, y in dot_locations:
    alex.penup()
    alex.goto(x, y)
    alex.dot(18, "red")


alex.penup()
alex.goto(0, -370)  
alex.color("red") 
alex.write("You are my favourite person, always!", align="center", font=("Arial", 26, 'bold'))

screen.mainloop()