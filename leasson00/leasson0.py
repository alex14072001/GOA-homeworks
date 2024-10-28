from turtle import*

#we want to point a house

#step 1: draw a square
speed(30)
width(7)
color("red")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#and of square

#drawin a door

forward(70)
color("grey")
begin_fill()
left(90)
forward(80)   #hight of the door
right(90)
forward(40)
right(90)
forward(80)
end_fill()

penup()
goto(200,200)
pendown()

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
penup()
goto(180,180)
pendown()

color("yellow")
begin_fill()

left(30)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(20, 180)
pendown()

color("yellow")
begin_fill()

left(30)
right(210)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(180, 160)
pendown()

color("black")

forward(40)
left(180)
forward(40)



penup()
goto(20, 160)
pendown()
forward(40)

penup()
goto(160, 180)
pendown()

right(90)
forward(40)

penup()
goto(40, 180)
pendown()

forward(40)





exitonclick()

