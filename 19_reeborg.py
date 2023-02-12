
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def goal_p():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
goal_p()
goal_p()
goal_p()
goal_p()
goal_p()
goal_p()
"""
# or
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def goal_p():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    goal_p()


"""