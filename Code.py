import turtle
turtle.setup(800,600,10,10)
tt = turtle.Turtle()  # 导入模块


tt.pensize(1)
tt.speed(10)  # 设置笔大小和速度

tt.pencolor('red')
tt.fillcolor('red')
tt.penup()
tt.goto(-300,-200)
tt.pendown()

tt.begin_fill()
tt.goto(300,-200)
tt.goto(300,200)
tt.goto(-300,200)
tt.goto(-300,-200)
tt.end_fill()  # 正方形

tt.penup()
tt.pencolor('yellow')
tt.fillcolor('yellow')
tt.goto(-260,130)
tt.pendown()
tt.begin_fill()

for i in range(5):
    tt.forward(40)
    tt.left(72)
    tt.forward(40)
    tt.right(144)  # 大五角星

tt.end_fill()
tt.penup()
tt.goto(-120,170)
tt.pendown()
tt.begin_fill()
tt.right(20)

for i in range(5):
    tt.forward(10)
    tt.left(72)
    tt.forward(10)
    tt.right(144)  # 小五角星1

tt.end_fill()
tt.penup()
tt.goto(-90,130)
tt.left(30)
tt.pendown()
tt.begin_fill()

for i in range(5):
    tt.forward(10)
    tt.left(72)
    tt.forward(10)
    tt.right(144)  # 小五角星2

tt.end_fill()
tt.penup()
tt.goto(-94,90)
tt.right(10)
tt.pendown()
tt.begin_fill()

for i in range(5):
    tt.forward(10)
    tt.left(72)
    tt.forward(10)
    tt.right(144)  # 小五角星3

tt.end_fill()
tt.penup()
tt.goto(-120,60)
tt.right(15)
tt.pendown()
tt.begin_fill()

for i in range(5):
    tt.forward(10)
    tt.left(72)
    tt.forward(10)
    tt.right(144)  # 小五角星4

tt.end_fill()
tt.penup()
tt.goto(400,400)
turtle.done()
