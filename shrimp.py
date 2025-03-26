


import tkinter.messagebox
import turtle
import tkinter
import math
import random
import numpy
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

EMPTY = 0
SHARK = 1
FISH = 2
SHRIMP = 3
BUBBLES = 4

white_sea_grid = numpy.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
])

green_sea_grid = numpy.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
])

def grid_to_pixel(grid_n):
    grid_n = grid_n * 100 + 50
    return grid_n

def first_pos(grid, enemy_grid):
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    while True:
        if grid[x][y] == EMPTY:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
        if enemy_grid[x][y] == EMPTY:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
        return (x, y)

def grid_to_pixel_vector(position):
    return (grid_to_pixel(position[0])), grid_to_pixel(position[1])





white_shark = './white_shark.gif'
turtle.register_shape(white_shark)

white_fish = './white_fish.gif'
turtle.register_shape(white_fish)

white_shrimp = './white_shrimp.gif'
turtle.register_shape(white_shrimp)

green_shark = './green_shark.gif'
turtle.register_shape(green_shark)

green_fish = './green_fish.gif'

turtle.register_shape(green_fish)

green_shrimp = './green_shrimp.gif'
turtle.register_shape(green_shrimp)




TEAM_W = 0
TEAM_G = 1

all_y = []
all_x = []

shark_w_x = []
fish_w_x = []
shrimp_w_x = []
shark_g_x = []
fish_g_x = []
shrimp_g_x = []

shark_w_y = []
fish_w_y = []
shrimp_w_y = []
shark_g_y = []
fish_g_y = []
shrimp_g_y = []

escaped = []
escaped_w = []
escaped_g = []

class Animal:
    def __init__(self, team, animal, grid, x, y, image):
        self.team = team
        self.animal_type = animal
        self.grid = grid
        self.x = x
        self.y = y
        self.turtle = turtle.Turtle()
        self.position = self.set_position(first_pos(white_sea_grid, green_sea_grid))
        self.turtle.shape(image)

    def __str__(self):
        return "Animal Type -> {} \nPosition - > {}".format(self.animal_type, self.position)

    def set_position(self, position):
        if hasattr(self, "position"):
            self.grid[self.position[0]][self.position[1]] = BUBBLES
        self.grid[position[0]][position[1]] = self.animal_type
        self.position = position
        self.turtle.penup()
        self.turtle.goto(grid_to_pixel_vector(self.position))
        self.x.append(position[0])
        self.y.append(position[1])

        


    
shark_w = Animal(TEAM_W, SHARK, white_sea_grid, shark_w_x, shark_w_y, white_shark)
fish_w = Animal(TEAM_W, FISH, white_sea_grid, fish_w_x, fish_w_y, white_fish)
shrimp_w = Animal(TEAM_W, SHRIMP, white_sea_grid, shrimp_w_x, shrimp_w_y, white_shrimp)
shark_g = Animal(TEAM_G, SHARK, green_sea_grid, shark_g_x, shark_g_y, green_shark)
fish_g = Animal(TEAM_G, FISH, green_sea_grid, fish_g_x, fish_g_y, green_fish)
shrimp_g = Animal(TEAM_G, SHRIMP, green_sea_grid, shrimp_g_x, shrimp_g_y, green_shrimp)



def print_grid(team):
    if team == TEAM_W:
        print("white")
        print(numpy.flip(numpy.transpose(white_sea_grid), 0))
    elif team == TEAM_G:
        print("green")
        print(numpy.flip(numpy.transpose(green_sea_grid), 0))
    

def the_move(animal, x, y):
    if x < 6 and y < 6 and x >= 0 and y >= 0 and animal.grid[x][y] == EMPTY:
        animal.turtle.goto(grid_to_pixel(x), grid_to_pixel(y))
        animal.grid[x][y] = animal.animal_type
        bubbles(animal)
        animal.x.append(x)
        animal.y.append(y)
        bubbles_draw(animal)
        print_grid(animal.team)
        edges_and_bubbles(animal)
        next_go.set(1) 

def movement(animal, x, y):
    if animal not in allowed_to_escape:
        the_move(animal, x, y)
    if animal in allowed_to_escape:
        if x > 5 or y > 5 or x < 0 or y < 0:
            fill.penup()
            fill.goto(animal.turtle.pos())
            if animal in team_w:
                fill_bubbles_w()
            elif animal in team_g:
                fill_bubbles_g()
            animal.turtle.goto(grid_to_pixel(x), grid_to_pixel(y))
            escaped.append(animal)
            skip.append(animal)
            if animal in list_of_animals:
                list_of_animals.remove(animal)
            if animal in team_w:
                escaped_w.append(animal)
                team_w.remove(animal)
            elif animal in team_g:
                escaped_g.append(animal)
                team_g.remove(animal)
            next_go.set(1)
        else:
            the_move(animal, x, y)
        

def edges_and_bubbles(animal):
    def no_up(animal):
        if grid_to_pixel(animal.y[-1] + 1) > 600:
            return True
    def no_down(animal):
        if grid_to_pixel(animal.y[-1] - 1) < 0:
            return True
    def no_left(animal):
        if grid_to_pixel(animal.x[-1] - 1) < 0:
            return True
    def no_right(animal):
        if grid_to_pixel(animal.x[-1] + 1) > 600:
           return True
    def no_up_bubbles(animal):
        if animal.y[-1] + 1 < 6:
            if animal.grid[animal.x[-1]][animal.y[-1] + 1] !=EMPTY:
                return True
    def no_down_bubbles(animal):
        if animal.y[-1] - 1 >=0:        
            if animal.grid[animal.x[-1]][animal.y[-1] - 1] !=EMPTY:
                return True
    def no_left_bubbles(animal):  
        if animal.x[-1] - 1 >=0:      
            if animal.grid[animal.x[-1] - 1][animal.y[-1]] !=EMPTY:
                return True
    def no_left_up_bubbles(animal):   
        if animal.x[-1] - 1 >=0 and animal.y[-1] + 1 < 6:         
            if animal.grid[animal.x[-1] - 1][animal.y[-1] + 1] !=EMPTY:
                return True
    def no_left_down_bubbles(animal): 
        if animal.x[-1] - 1 >=0 and animal.y[-1] - 1 >=0:               
            if animal.grid[animal.x[-1] - 1][animal.y[-1] - 1] !=EMPTY:
                return True
    def no_right_bubbles(animal):
        if animal.x[-1] + 1 < 6:
            if animal.grid[animal.x[-1] + 1][animal.y[-1]] !=EMPTY:
                return True
    def no_right_up_bubbles(animal):     
        if animal.x[-1] + 1 < 6 and animal.y[-1] + 1 < 6:               
            if animal.grid[animal.x[-1] + 1][animal.y[-1] + 1] !=EMPTY:
                return True
    def no_right_down_bubbles(animal): 
        if animal.x[-1] + 1 < 6 and animal.y[-1] - 1 <=0:                       
            if animal.grid[animal.x[-1] + 1][animal.y[-1] - 1] !=EMPTY:
                return True
            
    if no_left(animal) and no_up(animal) and no_down_bubbles(animal) and no_right_down_bubbles(animal) and no_right_bubbles(animal):
        is_trapped(animal)
    elif no_right(animal) and no_up(animal) and no_down_bubbles(animal) and no_left_down_bubbles(animal) and no_left_bubbles(animal):
        is_trapped(animal)
    elif no_left(animal) and no_down(animal) and no_up_bubbles(animal) and no_right_up_bubbles(animal) and no_right_bubbles(animal):
        is_trapped(animal)
    elif no_right(animal) and no_down(animal) and no_up_bubbles(animal) and no_left_up_bubbles(animal) and no_left_bubbles(animal):
        is_trapped(animal)
    elif no_up(animal) and no_left_bubbles(animal) and no_right_bubbles(animal) and no_down_bubbles(animal) and no_left_down_bubbles(animal) and no_right_down_bubbles:
        is_trapped(animal)
    elif no_left(animal) and no_up_bubbles(animal) and no_down_bubbles(animal) and no_right_bubbles(animal) and no_left_up_bubbles(animal) and no_right_down_bubbles:
        is_trapped(animal)
    elif no_right(animal) and no_up_bubbles(animal) and no_down_bubbles(animal) and no_left_bubbles(animal) and no_left_up_bubbles(animal) and no_left_down_bubbles:
        is_trapped(animal)
    elif no_down(animal) and no_up_bubbles(animal) and no_right_bubbles(animal) and no_left_bubbles(animal)and no_left_up_bubbles and no_right_up_bubbles:
        is_trapped(animal)
    elif no_left_bubbles(animal) and no_left_up_bubbles(animal) and no_up_bubbles(animal) and no_right_up_bubbles(animal) and no_right_bubbles(animal) and no_right_down_bubbles(animal) and no_down_bubbles(animal) and no_left_down_bubbles(animal):
        is_trapped(animal)




def move_up(animal):
    movement(animal, (animal.x[-1]), (animal.y[-1] + 1))

def move_down(animal):
    movement(animal, (animal.x[-1]), (animal.y[-1] - 1))

def move_left(animal):
    movement(animal, (animal.x[-1] - 1), (animal.y[-1]))
    
def move_left_up(animal):
    movement(animal, (animal.x[-1] - 1), (animal.y[-1] + 1))
    
def move_left_down(animal):
    movement(animal, (animal.x[-1] - 1), (animal.y[-1] - 1))
    
def move_right(animal):
    movement(animal, (animal.x[-1] + 1), (animal.y[-1]))
    
def move_right_up(animal):
    movement(animal, (animal.x[-1] + 1), (animal.y[-1] + 1))
    
def move_right_down(animal):
    movement(animal, (animal.x[-1] + 1), (animal.y[-1] - 1))

def bubbles(animal):
    animal.grid[animal.x[-1]][animal.y[-1]] = BUBBLES


team_w = [shark_w, fish_w, shrimp_w]
team_g = [shark_g, fish_g, shrimp_g]


def the_button(animal):
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

fill = turtle.Turtle()

def fill_bubbles_w():
    fill.hideturtle()
    fill.setheading(135)
    fill.forward(5)
    fill.pensize(5)
    fill.pencolor("white")
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

def fill_bubbles_g():
    fill.penup()
    fill.hideturtle()
    fill.setheading(270)
    fill.forward(40)
    fill.pensize(5)
    fill.pencolor("green")
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

def bubbles_draw(animal):
    def bubbles_here(animal):
        if len(animal.x) > 1 and len(animal.y) > 1:
            if animal.grid[animal.x[-2]][animal.y[-2]] == BUBBLES:
                fill.speed(50)
                fill.penup()
                fill.goto(grid_to_pixel(animal.x[-2]), grid_to_pixel(animal.y[-2]))
                fill.pendown()
    if animal in team_w:
        bubbles_here(animal)
        fill_bubbles_w()
    if animal in team_g:
        bubbles_here(animal)
        fill_bubbles_g()


skip = []
allowed_to_escape = []

def eaten(animal, eaten_animal):
    if animal.turtle.pos() == eaten_animal.turtle.pos():
        eaten_animal.turtle.hideturtle()
        eaten_animal.grid[eaten_animal.x[-1]][eaten_animal.y[-1]] == BUBBLES
        skip.append(eaten_animal)
        allowed_to_escape.append(animal)
        if eaten_animal in list_of_animals:
            list_of_animals.remove(eaten_animal)
        fill.penup()
        fill.goto(eaten_animal.turtle.pos())
        if eaten_animal in team_w:
            team_w.remove(eaten_animal)
            fill_bubbles_w()
        elif eaten_animal in team_g:
            team_g.remove(eaten_animal)
            fill_bubbles_g()
    elif eaten_animal in escaped:
        allowed_to_escape.append(animal)
    elif eaten_animal in trapped_animals:
        allowed_to_escape.append(animal)

def shrimp_w_tickles_shark_g():
    eaten(shrimp_w, shark_g)

def shark_w_eats_fish_g():
    eaten(shark_w, fish_g)

def fish_w_eats_shrimp_g():
    eaten(fish_w, shrimp_g)

def shrimp_g_tickles_shark_w():
    eaten(shrimp_g, shark_w)

def shark_g_eats_fish_w():
    eaten(shark_g, fish_w)

def fish_g_eats_shrimp_w():
    eaten(fish_g, shrimp_w)

def if_eaten():
    shrimp_w_tickles_shark_g()
    shark_w_eats_fish_g()
    fish_w_eats_shrimp_g()
    shrimp_g_tickles_shark_w()
    shark_g_eats_fish_w()
    fish_g_eats_shrimp_w()





trapped_animals = []
def is_trapped(animal):
    animal.grid[animal.x[-1]][animal.y[-1]] == BUBBLES
    trapped_animals.append(animal)
    skip.append(animal)
    if animal in list_of_animals:
        list_of_animals.remove(animal)
    
    animal.turtle.hideturtle()
    fill.penup()
    fill.goto(animal.turtle.pos())
    if animal in team_w:
        team_w.remove(animal)
        fill_bubbles_w()
    elif animal in team_g:
        team_g.remove(animal)
        fill_bubbles_g()
    next_go.set(1)

                                                        


list_of_animals = [shark_w, shark_g, fish_w, fish_g, shrimp_w, shrimp_g]


next_go = tkinter.IntVar()
next_button = tkinter.Button(text="next", command= lambda: next_go.set(1))
next_button.place(x=300, y=75)


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

def go():
    while True:
        for animal in list_of_animals:
            if animal not in skip:
                print(f"{animal.animal_type} {animal.team} go")
                the_button(animal)
                if_eaten()
                edges_and_bubbles(animal)
                
            next_button.wait_variable(next_go)
            wins()

def goooo():
    turn_w = 0
    turn_g = 0
    while True:
        if len(team_w) <1:
            print("w done")
        else:
            if turn_w >= len(team_w):
                turn_w = 0
            print(f"{team_w[turn_w].animal_type} {team_w[turn_w].team} go")
            edges_and_bubbles(team_w[turn_w])
            the_button(team_w[turn_w])
        
            
            next_button.wait_variable(next_go)
            if_eaten()
            if turn_w < len(team_w):
                turn_w = turn_w + (len(team_w) - (len(team_w)-1))
            wins()
        if len(team_g) <1:
            print("g done")
        else:
            if turn_g >= len(team_g):
                turn_g = 0
            print(f"{team_g[turn_g].animal_type} {team_g[turn_g].team} go")
            edges_and_bubbles(team_g[turn_g])
            if len(team_g) > turn_g:
                the_button(team_g[turn_g])
            else:
                next_go.set(1)
        
            
            next_button.wait_variable(next_go)
            if_eaten()
            if turn_g < len(team_g):
                turn_g = turn_g + (len(team_g) - (len(team_g)-1))
            wins()

goooo()

turtle.done()