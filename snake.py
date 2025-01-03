import turtle
import time
import random

delay = 0.1  # Time delay between screen updates
score = 0  # Initialize score
high_score = 0  # Initialize high score

# Screen setup
win = turtle.Screen()
win.title("Snake Game")  # Set window title
win.bgcolor("black")  # Set background color
win.setup(width=600, height=600)  # Set window size
win.tracer(0)  # Disable automatic screen updates for manual control

# Snake head
head = turtle.Turtle()
head.shape("square")  # Set shape of snake head
head.color("green")  # Set color of snake head
head.penup()  # Prevent drawing when moving
head.goto(0, 0)  # Start position of the snake head
head.direction = "stop"  # Initial movement direction

# Food
food = turtle.Turtle()
food.shape("circle")  # Set shape of food
food.color("red")  # Set color of food
food.penup()  # Prevent drawing when moving
food.goto(0, 100)  # Start position of food

# Snake body segments
segments = []  # List to hold the body segments of the snake

# Score display
score_display = turtle.Turtle()
score_display.speed(0)  # No animation
score_display.color("white")  # Set color of score display
score_display.penup()  # Prevent drawing when moving
score_display.hideturtle()  # Hide the cursor turtle
score_display.goto(0, 260)  # Position score display
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))  # Initial score display

# Functions to move the snake
def go_up():
    if head.direction != "down":  # Prevent snake from moving in the opposite direction
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    # Move the snake's head based on its current direction
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings to control snake's direction
win.listen()
win.onkey(go_up, "w")  # Move up when 'W' is pressed
win.onkey(go_down, "s")  # Move down when 'S' is pressed
win.onkey(go_left, "a")  # Move left when 'A' is pressed
win.onkey(go_right, "d")  # Move right when 'D' is pressed

# Main game loop
while True:
    win.update()  # Update the screen

    # Check for collision with border
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1)  # Pause for 1 second after collision
        head.goto(0, 0)  # Reset snake head position
        head.direction = "stop"  # Stop the snake

        # Reset the segments
        for segment in segments:
            segment.goto(1000, 1000)  # Move body segments off-screen
        segments.clear()  # Clear the segments list

        # Reset score
        score = 0
        score_display.clear()  # Clear previous score display
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check for collision with food
    if head.distance(food) < 20:  # Check if the snake is close enough to the food
        # Move food to a random spot on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment to the snake's body
        new_segment = turtle.Turtle()
        new_segment.shape("square")  # Set shape of new body segment
        new_segment.color("grey")  # Set color of new body segment
        new_segment.penup()  # Prevent drawing when moving
        segments.append(new_segment)  # Add new segment to the list

        # Increase score
        score += 10
        if score > high_score:  # Update high score if necessary
            high_score = score
        score_display.clear()  # Clear previous score display
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the segments in reverse order (following the head)
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())

    # Move the first segment to the head's position
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()  # Move the snake head

    # Check for collision with body (self-collision)
    for segment in segments:
        if segment.distance(head) < 20:  # Check if any segment is too close to the head
            time.sleep(1)  # Pause for 1 second after collision
            head.goto(0, 0)  # Reset snake head position
            head.direction = "stop"  # Stop the snake

            # Reset the body segments
            for segment in segments:
                segment.goto(1000, 1000)  # Move body segments off-screen
            segments.clear()  # Clear the segments list

            # Reset score
            score = 0
            score_display.clear()  # Clear previous score display
            score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)  # Delay to control game speed

win.mainloop()  # Keep the window open
