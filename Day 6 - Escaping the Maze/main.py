# Day 6 - Escaping the Maze
# This program is a solution of this problem in the following site:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not wall_in_front():
    move()
turn_left()
    
while not at_goal():
    if not wall_in_front() and not right_is_clear():       
        move()
    elif not wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front() and not right_is_clear():
        turn_left()
    else:
        turn_right()
        move()
