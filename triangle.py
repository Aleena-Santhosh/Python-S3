import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("My Turtle equilateral triangle") 


my_turtle = turtle.Turtle()
my_turtle.fillcolor("red")
my_turtle.pencolor("darkgreen") 
my_turtle.pensize(8) 

my_turtle.begin_fill()
for _ in range(3): 
    my_turtle.forward(100) 
    my_turtle.right(-120) 
my_turtle.end_fill()
turtle.done()