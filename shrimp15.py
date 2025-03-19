


import tkinter.messagebox
import turtle
import tkinter
import math
import random
sea = turtle.Screen()
sea.title("Sharks and Shrimps")
sea.bgcolor("dark blue")
sea.setup(width=800, height=800)
sea.setworldcoordinates(-100, -100, 700, 700)


def square(pen, distance):
    for i in range(4):
        pen.forward(distance)
        pen.left(90)

speed = 100
grid = turtle.Turtle()
grid.speed(speed)
grid.shape("triangle")
grid.color("dark turquoise")
grid.penup()
grid.goto(0,0)
grid.pendown()
square(grid, 600)

for i in range(1,6):
    grid.penup()
    grid.goto(0,100*i)
    grid.pendown()
    grid.forward(600)

for i in range(1,6):
    grid.penup()
    grid.goto(100*i,0)
    grid.pendown()
    grid.left(90)
    grid.forward(600)
    grid.penup()
    grid.left(90)
    grid.forward(100)
    grid.pendown()
    grid.left(90)
    grid.forward(600)
    grid.penup()
    grid.left(90)
    grid.forward(100)

grid.hideturtle()


speed = 100
team_w_colour = "white"
team_w_pencolour = "white"



white_shark = r'C:/Users/aries/Desktop/codes/white_shark.gif'
white_moving_shark = './white_moving_shark.gif'
turtle.register_shape(white_shark)
turtle.register_shape(white_moving_shark)
shark_w = turtle.Turtle()
shark_w.shape(white_shark)
shark_w.pencolor(team_w_pencolour)
shark_w.penup()
first_shark_w_x = random.randint(0, 300)
first_shark_w_y = random.randint(300, 600)
shark_w.goto(first_shark_w_x, first_shark_w_y)

white_fish = './white_fish.gif'
turtle.register_shape(white_fish)
fish_w = turtle.Turtle()
fish_w.shape(white_fish)
fish_w.color(team_w_colour)
fish_w.pencolor("turquoise")
fish_w.pensize(35)
fish_w.penup()
first_fish_w_x = random.randint(0, 300)
first_fish_w_y = random.randint(0, 600)
fish_w.goto(first_fish_w_x, first_fish_w_y)

white_shrimp = './white_shrimp.gif'
turtle.register_shape(white_shrimp)
shrimp_w = turtle.Turtle()
shrimp_w.shape(white_shrimp)
shrimp_w.color(team_w_colour)
shrimp_w.pencolor("turquoise")
shrimp_w.pensize(35)
shrimp_w.penup()
first_shark_w_x = random.randint(0, 300)
first_shark_w_y = random.randint(0, 300)
shrimp_w.goto(50, 203)

team_g_colour = "green"
team_g_pencolour = "green"

green_shark = './green_shark.gif'
turtle.register_shape(green_shark)
shark_g = turtle.Turtle()
shark_g.shape(green_shark)
shark_g.color(team_g_colour)
shark_g.pencolor(team_g_pencolour)
shark_g.pensize(55)
shark_g.penup()
first_shark_g_x = random.randint(300, 600)
first_shark_g_y = random.randint(300, 600)
shark_g.goto(first_shark_g_x, first_shark_g_y)

green_fish = './green_fish.gif'
fish_g = turtle.Turtle()
turtle.register_shape(green_fish)
fish_g.shape(green_fish)
fish_g.color(team_g_colour)
fish_g.pencolor("light green")
fish_g.pensize(55)
fish_g.penup()
first_fish_g_x = random.randint(300, 600)
first_fish_g_y = random.randint(0, 600)
fish_g.goto(first_fish_g_x, first_fish_g_y)

green_shrimp = './green_shrimp.gif'
turtle.register_shape(green_shrimp)
shrimp_g = turtle.Turtle()
shrimp_g.shape(green_shrimp)
shrimp_g.color(team_g_colour)
shrimp_g.pensize(55)
shrimp_g.pencolor("light green")
shrimp_g.penup()
first_shrimp_g_x = random.randint(300, 600)
first_shrimp_g_y = random.randint(0, 300)
shrimp_g.goto(first_shrimp_g_x, first_shrimp_g_y)

animals_positions_w = []
animals_positions_g = []




fill = turtle.Turtle()
fill_pos = []


def one_coloured_goto(animal):
        fill.hideturtle()
        fill.penup()
        fill.speed(500)
        
        if animal == shark_w and len(shark_w_pos) > 1 and shark_w_pos[-2] not in fill_pos:
            fill.goto(shark_w_pos[-2])
        elif animal == fish_w and len(fish_w_pos) > 1 and fish_w_pos[-2] not in fill_pos:
            fill.goto(fish_w_pos[-2])
        elif animal == shrimp_w and len(shrimp_w_pos) > 1 and shrimp_w_pos[-2] not in fill_pos:
            fill.goto(shrimp_w_pos[-2])
        fill.penup()
        fill.speed(500)
        if animal == shark_g and len(shark_g_pos) > 1 and shark_g_pos[-2] not in fill_pos:
            fill.goto(shark_g_pos[-2])
        if animal == fish_g and len(fish_g_pos) > 1 and fish_g_pos[-2] not in fill_pos:
            fill.goto(fish_g_pos[-2])
        if animal == shrimp_g and len(shrimp_g_pos) > 1 and shrimp_g_pos[-2] not in fill_pos:
            fill.goto(shrimp_g_pos[-2])

        if animal in trapped_animals:
            fill.goto(trappened_pos[-1])
            
        

def one_fill_bubbles_w(animal):
    fill.hideturtle()
    fill.setheading(135)
    fill.forward(5)
    fill.pensize(5)
    fill.pencolor(team_w_pencolour)
    fill.pendown()
    fill.circle(3)
    fill.penup()
    fill.setheading(150)
    fill.forward(15)
    fill.pendown()
    fill.circle(10)
    fill.penup()
    fill.setheading(90)
    fill.forward(20)
    fill.pendown()
    fill.circle(15)

def one_fill_bubbles_g(animal):
    fill.hideturtle()
    fill.setheading(270)
    fill.forward(40)
    fill.pensize(5)
    fill.pencolor(team_g_pencolour)
    fill.pendown()
    fill.circle(3)
    fill.penup()
    fill.setheading(15)
    fill.forward(20)
    fill.pendown()
    fill.circle(10)
    fill.penup()
    fill.setheading(65)
    fill.forward(40)
    fill.pendown()
    fill.circle(15)



import numpy

cell1 = [[0,100],[100,100],[100,0],[0,0]]
first_cells_of_rows = []
all_cells = []
all_cells.append(numpy.array(cell1))

def cell_up():
    first_cell = [[0,100],[100,100],[100,0],[0,0]]
    first_cells_of_rows.append(numpy.array(first_cell))
    for n in range(5):
        for i in first_cell:
            i[1]+=100
        first_cells_of_rows.append(numpy.array(first_cell))
        all_cells.append(numpy.array(first_cell))

cell_up()

def next_cell(first_cell):
    for n in range(5):
        for i in first_cell:
            i[0]+=100
        all_cells.append(numpy.array(first_cell))

next_cell(first_cells_of_rows[0])
next_cell(first_cells_of_rows[1])
next_cell(first_cells_of_rows[2])
next_cell(first_cells_of_rows[3])
next_cell(first_cells_of_rows[4])
next_cell(first_cells_of_rows[5])







skip = []
skip_w = []
skip_g = []

def shrimp_w_tickles_shark_g():
    if shrimp_w.pos() == shark_g.pos():
        print("Shrimp tickles the Shark!")
        shark_g.hideturtle()
        skip.append(shark_g)
        skip_g.append(shark_g)
        if shark_g in team_g:
            team_g.remove(shark_g)
        animals_positions_g.append(shark_g.pos())
        #if shrimp_w_pos[-1] == animals_positions_w[-1] or shark_g_pos[-1] == animals_positions_g[-1]:
        #    tkinter.messagebox.showinfo(title= "shark is gone", message="Shrimp tickled Shark!")
        


def shark_w_eats_fish_g():
    if fish_g.pos() == shark_w.pos():
        print("Shark eats Fish!")
        fish_g.hideturtle()
        skip.append(fish_g)
        skip_g.append(fish_g)
        if fish_g in team_g:
            team_g.remove(fish_g)
        animals_positions_g.append(fish_g.pos())
        #order_reset()
        

def fish_w_eats_shrimp_g():
    if fish_w.pos() == shrimp_g.pos():
        print("Fish eats Srimp!")
        shrimp_g.hideturtle()
        skip.append(shrimp_g)
        skip_g.append(shrimp_g)
        if shrimp_g in team_g:
            team_g.remove(shrimp_g)
        animals_positions_g.append(shrimp_g.pos())
        #order_reset()


def shrimp_g_tickles_shark_w():
    if shrimp_g.pos() == shark_w.pos():
        print("Shrimp tickles the Shark!")
        shark_w.hideturtle()
        skip.append(shark_w)
        skip_w.append(shark_w)
        if shark_w in team_w:
            team_w.remove(shark_w)
        animals_positions_w.append(shark_w.pos())
        #order_reset()

def shark_g_eats_fish_w():
    if fish_w.pos() == shark_g.pos():
        print("Shark eats Fish!")
        fish_w.hideturtle()
        skip.append(fish_w)
        skip_w.append(fish_w)
        if fish_w in team_w:
            team_w.remove(fish_w)
        animals_positions_w.append(fish_w.pos())
        #order_reset()

def fish_g_eats_shrimp_w():
    if fish_g.pos() == shrimp_w.pos():
        print("Fish eats Srimp!")
        shrimp_w.hideturtle()
        skip.append(shrimp_w)
        skip_w.append(shrimp_w)
        if shrimp_w in team_w:
            team_w.remove(shrimp_w)
        animals_positions_w.append(shrimp_w.pos())

def eaten(animal):
                if shark_w.pos() == fish_g.pos():
                    shark_w_eats_fish_g()
                    order_reset()
                    if animal == shark_w:
                        fill.penup()
                        fill.goto(fish_g_pos[-1])
                        just_bubbles(fish_g)
                    elif animal == fish_g:
                        one_coloured_goto(fish_g)
                        just_bubbles(fish_g)
                elif fish_w.pos() == shrimp_g.pos():
                    fish_w_eats_shrimp_g()
                    order_reset()
                    if animal == fish_w:
                        fill.penup()
                        fill.goto(shrimp_g_pos[-1])
                        just_bubbles(shrimp_g)
                    elif animal == shrimp_g:
                        one_coloured_goto(shrimp_g)
                        just_bubbles(shrimp_g)
                elif shrimp_w.pos() == shark_g.pos():
                    shrimp_w_tickles_shark_g()
                    order_reset()
                    if animal == shrimp_w:
                        fill.penup()
                        fill.goto(shark_g_pos[-1])
                        just_bubbles(shark_g)
                    elif animal == shark_g:
                        one_coloured_goto(shark_g)
                        just_bubbles(shark_g)
                elif shark_g.pos() == fish_w.pos():
                    shark_g_eats_fish_w()
                    order_reset()
                    if animal == shark_g:
                        fill.penup()
                        fill.goto(fish_w_pos[-1])
                        just_bubbles(fish_w)
                    elif animal == fish_w:
                        one_coloured_goto(fish_w)
                        just_bubbles(fish_w)
                elif fish_g.pos() == shrimp_w.pos():
                    fish_g_eats_shrimp_w()
                    order_reset()
                    if animal == fish_g:
                        fill.penup()
                        fill.goto(shrimp_w_pos[-1])
                        just_bubbles(shrimp_w)
                    elif animal == shrimp_w:
                        one_coloured_goto(shrimp_w)
                        just_bubbles(shrimp_w)
                elif shrimp_g.pos() == shark_w.pos():
                    shrimp_g_tickles_shark_w()
                    order_reset()
                    if animal == shrimp_g:
                        fill.penup()
                        fill.goto(shark_w_pos[-1])
                        just_bubbles(shark_w)
                    elif animal == shark_w:
                        one_coloured_goto(shark_w)
                        just_bubbles(shark_w)

def animal_settles(animal):
    if animal not in skip:
        for i in all_cells:
            if animal.xcor() > i[0,0] and animal.xcor() < i[1,0] and animal.xcor() < i[2,0] and animal.xcor() > i[3,0] and animal.ycor() < i[0,1] and animal.ycor() < i[1,1] and animal.ycor() > i[2,1] and animal.ycor() > i[3,1]:
                animal.goto(((i[0,0]+i[1,0])/2, (i[1,1]+i[2,1])/2))
                
                cant_go_there(animal)
                eaten(animal)







def move_up(animal):
    animal.setheading(90)
    animal.forward(100)
    animal_settles(animal)
    cant_go_there(animal)
    one_coloured_goto(animal)
    next_go.set(1)

def move_down(animal):
    animal.setheading(270)
    animal.forward(100)
    animal_settles(animal)
    cant_go_there(animal)
    one_coloured_goto(animal)
    next_go.set(1)

def move_left(animal):
    animal.setheading(180)
    animal.forward(100)
    animal_settles(animal)
    cant_go_there(animal)
    one_coloured_goto(animal)
    next_go.set(1)

def move_left_up(animal):
    animal.setheading(135)
    animal.forward((math.sqrt(2)*100))
    animal_settles(animal)
    cant_go_there(animal)
    one_coloured_goto(animal)
    next_go.set(1)

def move_left_down(animal):
    animal.setheading(225)
    animal.forward((math.sqrt(2)*100))
    animal_settles(animal)
    cant_go_there(animal)
    one_coloured_goto(animal)
    next_go.set(1)

def move_right(animal):
    animal.setheading(0)
    animal.forward(100)
    animal_settles(animal)
    cant_go_there(animal)
    one_coloured_goto(animal)
    next_go.set(1)

def move_right_up(animal):
    animal.setheading(45)
    animal.forward((math.sqrt(2)*100))
    animal_settles(animal)
    cant_go_there(animal)
    one_coloured_goto(animal)
    next_go.set(1)

def move_right_down(animal):
    animal.setheading(315)
    animal.forward((math.sqrt(2)*100))
    animal_settles(animal)
    cant_go_there(animal)
    one_coloured_goto(animal)
    next_go.set(1)


   

team_w = [shark_w, fish_w, shrimp_w]
team_g = [shark_g, fish_g, shrimp_g]
shark_w_pos = []
fish_w_pos = []
shrimp_w_pos = []
shark_g_pos = []
fish_g_pos = []
shrimp_g_pos = []
order = []
def order_reset():

            order.clear()
            if len(team_w) == 1 and len(team_g) == 1:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
            elif len(team_w) == 1 and len(team_g) == 2:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
                order.insert(2, team_w[0])
                order.insert(3, team_g[1])
            elif len(team_w) == 1 and len(team_g) == 3:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
                order.insert(2, team_w[0])
                order.insert(3, team_g[1])
                order.insert(4, team_w[0])
                order.insert(5, team_g[2])
            elif len(team_w) == 2 and len(team_g) == 1:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
                order.insert(2, team_w[1])
                order.insert(3, team_g[0])
            elif len(team_w) == 2 and len(team_g) == 2:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
                order.insert(2, team_w[1])
                order.insert(3, team_g[1])
            elif len(team_w) == 2 and len(team_g) == 3:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
                order.insert(2, team_w[1])
                order.insert(3, team_g[1])
                order.insert(4, team_w[1])
                order.insert(5, team_g[2])
            elif len(team_w) == 3 and len(team_g) == 1:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
                order.insert(2, team_w[1])
                order.insert(3, team_g[0])
                order.insert(4, team_w[2])
                order.insert(5, team_g[0])
            elif len(team_w) == 3 and len(team_g) == 2:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
                order.insert(2, team_w[1])
                order.insert(3, team_g[1])
                order.insert(4, team_w[2])
                order.insert(5, team_g[1])
            elif len(team_w) == 3 and len(team_g) == 3:
                order.insert(0, team_w[0])
                order.insert(1, team_g[0])
                order.insert(2, team_w[1])
                order.insert(3, team_g[1])
                order.insert(4, team_w[2])
                order.insert(5, team_g[2])
            elif len(team_w) == 0 and len(team_g) == 1:
                order.insert(0, team_g[0])
            elif len(team_g) == 0 and len(team_w) == 1:
                order.insert(0, team_w[0])
            elif len(team_w) == 0 and len(team_g) == 2:
                order.insert(0, team_g[0])
                order.insert(0, team_g[1])
            elif len(team_g) == 0 and len(team_w) == 2:
                order.insert(0, team_w[0])
                order.insert(0, team_w[1])
            elif len(team_w) == 0 and len(team_g) == 3:
                order.insert(0, team_g[0])
                order.insert(0, team_g[1])
                order.insert(0, team_g[2])
            elif len(team_g) == 0 and len(team_w) == 3:
                order.insert(0, team_w[0])
                order.insert(0, team_w[1])
                order.insert(0, team_w[2])




def cant_go_there(animal):
    borders(animal)
    print(animals_positions_w)
    if animal in team_w and animal.pos() in animals_positions_w:
        if animal == shark_w and animal.pos() != shark_w_pos[-1]:
            animal.goto(shark_w_pos[-1])
        if animal == fish_w and animal.pos() != fish_w_pos[-1]:
            animal.goto(fish_w_pos[-1])
        if animal == shrimp_w and animal.pos() != shrimp_w_pos[-1]:
            animal.goto(shrimp_w_pos[-1])
    elif animal in team_w and animal.pos() not in animals_positions_w:
        animals_positions_w.append(animal.pos())
        if animal == shark_w:
            shark_w_pos.append(animal.pos())
        if animal == fish_w:
            fish_w_pos.append(animal.pos())
        if animal == shrimp_w:
            shrimp_w_pos.append(animal.pos())
        
        print(animals_positions_w)
    print(animals_positions_g)
    if animal in team_g and animal.pos() in animals_positions_g:
        if animal == shark_g and animal.pos() != shark_g_pos[-1]:
            animal.goto(shark_g_pos[-1])
        if animal == fish_g and animal.pos() != fish_g_pos[-1]:
            animal.goto(fish_g_pos[-1])
        if animal == shrimp_g and animal.pos() != shrimp_g_pos[-1]:
            animal.goto(shrimp_g_pos[-1])
    elif animal in team_g and animal.pos() not in animals_positions_g:
        animals_positions_g.append(animal.pos())
        if animal == shark_g:
            shark_g_pos.append(animal.pos())
        if animal == fish_g:
            fish_g_pos.append(animal.pos())
        if animal == shrimp_g:
            shrimp_g_pos.append(animal.pos())

        print(animals_positions_g)

trapped_animals = []
trappened_pos = []
def trapped(animal):
    def is_trapped(animal):
        trappened_pos.append(animal.pos())
        trapped_animals.append(animal)
        skip.append(animal)
        if animal in team_w:    
            team_w.remove(animal)
            animal.hideturtle()
            fill.penup()
            fill.speed(500)
            fill.goto(trappened_pos[-1])
            one_fill_bubbles_w(animal)
        if animal in team_g:
            team_g.remove(animal)
            animal.hideturtle()
            fill.penup()
            fill.speed(500)
            fill.goto(trappened_pos[-1])
            one_fill_bubbles_g(animal)
        
        

            
        
    trapped = tkinter.Button(text="trapped", command= lambda: is_trapped(animal))
    trapped.place(x=100, y=75)
    



escaped = []
escaped_w = []
escaped_g = []

def borders(animal):
    if animal.xcor() < 0 or animal.xcor() > 600 or animal.ycor() < 0 or animal.ycor() > 600:
        if animal == shark_w:
            if fish_g in skip:
                escaped.append(shark_w)
                escaped_w.append(shark_w)
                skip_w.append(shark_w)
                skip.append(shark_w)
                team_w.remove(shark_w)
                shark_w_pos.append(shark_w.pos())
            else:
                shark_w.goto(shark_w_pos[-1])
        if animal == fish_w:
            if shrimp_g in skip:
                escaped.append(fish_w)
                escaped_w.append(fish_w)
                skip_w.append(fish_w)
                skip.append(fish_w)
                team_w.remove(fish_w)
                fish_w_pos.append(fish_w.pos())
            else:
                fish_w.goto(fish_w_pos[-1])
        if animal == shrimp_w:
            if shark_g in skip:
                escaped.append(shrimp_w)
                escaped_w.append(shrimp_w)
                skip_w.append(shrimp_w)
                skip.append(shrimp_w)
                team_w.remove(shrimp_w)
                shrimp_w_pos.append(shrimp_w.pos())
            else:
                shrimp_w.goto(shrimp_w_pos[-1])
        
        if animal == shark_g:
            if fish_w in skip:
                escaped.append(shark_g)
                escaped_g.append(shark_g)
                skip_g.append(shark_g)
                skip.append(shark_g)
                team_g.remove(shark_g)
                shark_g_pos.append(shark_g.pos())
            else:
                shark_g.goto(shark_g_pos[-1])
        if animal == fish_g:
            if shrimp_w in skip:
                escaped.append(fish_g)
                escaped_g.append(fish_g)
                skip_g.append(fish_g)
                skip.append(fish_g)
                team_g.remove(fish_g)
                fish_g_pos.append(fish_g.pos())
            else:
                fish_g.goto(fish_g_pos[-1])
        if animal == shrimp_g:
            if shark_w in skip:
                escaped.append(shrimp_g)
                escaped_g.append(shrimp_g)
                skip_g.append(shrimp_g)
                skip.append(shrimp_g)
                team_g.remove(shrimp_g)
                shrimp_g_pos.append(shrimp_g.pos())
            else:
                shrimp_g.goto(shrimp_g_pos[-1])
    

        


def the_button(animal):
    
    animal_settles(animal)

    up_button = tkinter.Button(text="up", command= lambda: move_up(animal))
    up_button.place(x=706,y=15)

    down_button = tkinter.Button(text="down", command= lambda: move_down(animal))
    down_button.place(x=700,y=45)

    left_button = tkinter.Button(text="left", command= lambda: move_left(animal))
    left_button.place(x=662,y=45)

    right_button = tkinter.Button(text="right", command= lambda: move_right(animal))
    right_button.place(x=750,y=45)

    left_up_button = tkinter.Button(text="left_up", command= lambda: move_left_up(animal))
    left_up_button.place(x=655,y=15)

    left_down_button = tkinter.Button(text="left_down", command= lambda: move_left_down(animal))
    left_down_button.place(x=640,y=73)

    right_up_button = tkinter.Button(text="right_up", command= lambda: move_right_up(animal))
    right_up_button.place(x=738,y=15)

    right_down_button = tkinter.Button(text="right_down", command= lambda: move_right_down(animal))
    right_down_button.place(x=725,y=73)





next_go = tkinter.IntVar()
next_button = tkinter.Button(text="next", command= lambda: next_go.set(1))
next_button.place(x=300, y=50)
next_button.config(height= 3, width= 10, bg= "yellow")



def just_bubbles(animal):
    if animal == shark_w and len(shark_w_pos) > 1 and shark_w_pos[-2] not in fill_pos:
        one_fill_bubbles_w(animal)
    elif animal == fish_w and len(fish_w_pos) > 1 and fish_w_pos[-2] not in fill_pos:
        one_fill_bubbles_w(animal)
    elif animal == shrimp_w and len(shrimp_w_pos) > 1 and shrimp_w_pos[-2] not in fill_pos:
        one_fill_bubbles_w(animal)
    elif animal == shark_g and len(shark_g_pos) > 1 and shark_g_pos[-2] not in fill_pos:
        one_fill_bubbles_g(animal)
    elif animal == fish_g and len(fish_g_pos) > 1 and fish_g_pos[-2] not in fill_pos:
        one_fill_bubbles_g(animal)
    elif animal == shrimp_g and len(shrimp_g_pos) > 1 and shrimp_g_pos[-2] not in fill_pos:
        one_fill_bubbles_g(animal)


for animal in team_w:
    animal_settles(animal)
    animals_positions_w.append(animal.pos())
for animal in team_g:
    animal_settles(animal)
    animals_positions_g.append(animal.pos())


def wins():
    if len(team_w) == 0 and len(team_g) == 0:
        if len(escaped_w) > len(escaped_g):
            print("w wins")
            tkinter.messagebox.showinfo(title= "winner", message="White wins!")
        elif len(escaped_w) < len(escaped_g):
            print("g wins")
            tkinter.messagebox.showinfo(title= "winner", message="Green wins!")
        else:
            print("Draw!")
            tkinter.messagebox.showinfo(title= "winner", message="It's a Draw!")

w_s_m1 = './white_shark_move1.gif'
w_s_m2 = './white_shark_move2.gif'
turtle.register_shape(w_s_m1)
turtle.register_shape(w_s_m2)







order = [shark_w, shark_g, fish_w, fish_g, shrimp_w, shrimp_g]
def move():
    
    
    while True:
        
         
        
        #order_reset()   
        for animal in order:
            order_reset()
            
            if animal not in skip:
                if animal == shark_w:
                    for i in range(30):
                        shark_w.shape(w_s_m1)
                        shark_w.shape(w_s_m2)
                else:
                    shark_w.shape(white_shark)
                
                
                the_button(animal)
                cant_go_there(animal)
                order_reset()
                
            
            

            trapped(animal)
            
            next_button.wait_variable(next_go)
            just_bubbles(animal)
            
            wins()
            
            


move()

sea.listen()
turtle.done()