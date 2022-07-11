import turtle
import pandas
from points_manager import Point
import time

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title('U.S. States Game')
image = './Quiz_game/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
points_manager = Point()

data = pandas.read_csv('./Quiz_game/50_states.csv')

states_list = data['state'].to_list()

for i in range(len(states_list)):
    states_list[i] = states_list[i].lower()

while len(points_manager.all_points) < 50:
    time.sleep(0.1)
    right_answers = len(points_manager.all_points)
    answer_state = screen.textinput(title=f'States correct [{right_answers}/50]', prompt='What\'s another state\'s name?').lower()
    if answer_state in states_list and right_answers < 50:
        if answer_state in points_manager.state_name:
            pass
        else:
            coor = (int(data[data.state.str.lower() == answer_state].x), int(data[data.state.str.lower() == answer_state].y))
            points_manager.add_point(coor=coor, state=data[data.state.str.lower() == answer_state].state.item())
    if answer_state == 'exit':
        missing_states = []
        how_many = len(states_list) - len(points_manager.all_points)
        print(how_many)
        for _ in range(how_many):
            if states_list[_] not in points_manager.all_points:
                missing_states.append(states_list[_])
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('./Quiz_game/states_to_learn')
        break
    screen.update()