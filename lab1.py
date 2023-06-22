import turtle
import random
def turtle_2_tri(turtle_input):
     #   turtle_input.color("hotpink")
        turtle_input.forward(80)                 # Let tess draw an equilateral triangle
        turtle_input.left(120)
        turtle_input.forward(80)
        turtle_input.left(120)
        turtle_input.forward(80)
        turtle_input.left(120)   
def screen_1():
    wn = turtle.Screen()
    thomasH = turtle.Turtle()
    thomasB = turtle.Turtle()
    for i in range(8):
        thomasH.forward(150)
        thomasH.left(45)
        turtle_2_tri(thomasB)
    wn.exitonclick()
def create_box():
    turtle_box = turtle.Turtle()
    turtle_box.width(0.5)
    turtle_box.speed(0)
    turtle_box.penup()
    turtle_box.goto(-350,350)
    turtle_box.pendown()
    turtle_box.goto(350,350)
    turtle_box.goto(350,-350)
    turtle_box.goto(-350,-350)
    turtle_box.goto(-350,350)
def create_x(size):
    grid_size = size
    new_line = 0
    x_cord = -350
    y_cord = 330
    while y_cord >= -310:
       
       if(new_line == 0):
            x = turtle.Turtle()
            x.width(2)
          #  x.color("hotpink")
            x.speed(0)
            x.penup()
            #left
            x.goto(x_cord,y_cord)
            x.pendown()
            #right
            x.goto(350, 330)
            new_line+=1
       else:
            y_cord = 330 - (grid_size*new_line)
            x.penup()
            x.goto(x_cord,y_cord)
            x.pendown()
            x.goto(-x_cord,y_cord)
            new_line+=1            
def create_y(size):
    
    grid_size = size
    new_line = 0
    x_cord = -350
    y_cord = 330
    while x_cord <= 330:
       if(new_line == 0):
            y = turtle.Turtle()
            y.speed(0)
            y.width(2)
            #y.color("green")
            y.speed(0)
            y.penup()
            #left
            y.goto(x_cord,y_cord)
            y.pendown()
            #right
            y.goto(350, 330)
            new_line+=1
       else:
            x_cord = -350 + (grid_size*new_line)
            y.penup()
            y.goto(x_cord,y_cord)
            y.pendown()
            y.goto(x_cord,-y_cord)
            new_line+=1            
def random_stock(size):
     grid_size = size
     arrow = turtle.Turtle()
     arrow.width(5)
     #sets the stock to price 0
     start_x = -350
     start_y = -350
     arrow.speed(0)
     #arrow.color("red") 
     arrow.penup()
     arrow.goto(start_x,start_y)

     random_outcome = [0,1,0,1,0,0,0,0,1]
     random_increment = [1,2,3,4]
     rebound = [-300, -320, -290,-250,-100,-310,-270]
     
     flag = False
     
     # 0 - up 1- down
     prices = []
     while start_x <= 350-size:
        up_down = random.choice(random_outcome)
        random_inc = random.choice(random_increment)
       # print(str(up_down) + " =  " + str(i))
        print("x " + str(start_x))
        print("y " + str(start_y))
        print("------------------------")
        random_inc =  random.choice(random_increment)
        
        if(up_down == 0 and  start_x == -350 and  start_y == -330):
            start_x = start_x + (grid_size * random_inc)
            start_y = start_y +  (grid_size *random_inc)
            arrow.pendown()
            arrow.color("green")
            arrow.goto(start_x,start_y)
            flag = True
        elif(start_y <= -330):
            start_y = random.choice(rebound)
            arrow.goto(start_x,start_y)
            arrow.color("green")
        elif up_down== 1 :
            start_x = start_x + ( grid_size * random_inc)
            start_y = start_y -  (grid_size *random_inc)
            arrow.pendown()
            arrow.color("red")
            arrow.goto(start_x,start_y)
        else:
            start_x = start_x + (grid_size * random_inc)
            start_y = start_y +  (grid_size *random_inc)
            arrow.pendown()
            arrow.color("green")
            arrow.goto(start_x,start_y)
        prices.append(start_y)
     print(prices)

          

        
     
     


def screen_2(): 
    wn = turtle.Screen()
    size = 10
    create_box()
    create_x(size)
    create_y(size)
    random_stock(size)

    wn.exitonclick()

    
 

  
#user_input =input("What screen you want? [1] or [2] ?")
screen_2()  

              

