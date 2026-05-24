import turtle

# =========================
# Screen Setup
# =========================
window = turtle.Screen()
window.bgcolor("purple")
window.title("Cute Cat Drawing")

# =========================
# Turtle Setup
# =========================
t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.speed(8)
t.pensize(5)

# =========================
# Helper Move
# =========================
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# =========================
# HEAD
# =========================
move(0, -100)
t.setheading(0)
t.circle(100)

# =========================
# EARS (closed triangles on head edge)
# =========================
# Left ear
move(-60, 80)
t.goto(-30, 90)
t.goto(-45, 140)
t.goto(-60, 80)

# Right ear
move(60, 80)
t.goto(30, 90)
t.goto(45, 140)
t.goto(60, 80)

# =========================
# EYES (upward arcs ∩)
# =========================
move(-47, 50)
t.setheading(270)
t.circle(12, 180)

move(23, 50)
t.setheading(270)
t.circle(12, 180)

# =========================
# NOSE (small filled circle)
# =========================
move(0, 18)
t.setheading(0)
t.begin_fill()
t.circle(8)
t.end_fill()

# =========================
# MOUTH (W shape — two U bumps)
# =========================
move(-16, -5)
t.setheading(270)
t.circle(8, 180)

move(0, -5)
t.setheading(270)
t.circle(8, 180)

# =========================
# WHISKERS (long, nearly horizontal)
# =========================
def whisker(x, y, angle):
    move(x, y)
    t.setheading(angle)
    t.forward(80)

# Right whiskers
whisker(35, 15, 5)
whisker(35, 5, 0)
whisker(35, -5, -5)

# Left whiskers
whisker(-35, 15, 175)
whisker(-35, 5, 180)
whisker(-35, -5, 185)

# =========================
# FINISH
# =========================
t.hideturtle()
window.exitonclick()
