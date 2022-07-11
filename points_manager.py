from turtle import Turtle

FONT = ('Courier', 8, 'bold')

class Point():

    def __init__(self):
        self.all_points = []
        self.state_name = []
    
    def add_point(self, coor, state):
        new_point = Turtle()
        new_point.hideturtle()
        new_point.penup()
        new_point.goto(coor)
        new_point.write(f'{state}', align='center', font=FONT)
        self.all_points.append(new_point)
        self.state_name.append(state)
