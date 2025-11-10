import turtle
import pandas


screen = turtle.Screen()
screen.title("USA States Game")

screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")


data = pandas.read_csv("50_states.csv")
states_list = data["state"]
states_list = states_list.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the name of the State?").title()
    if answer_state == "Exit":
        break
    if (answer_state in states_list) and ((answer_state in guessed_states) == False):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_state_row = data[data["state"]==answer_state]
        t.goto(int(answer_state_row["x"].iloc[0]), int(answer_state_row["y"].iloc[0]))
        t.write(answer_state)
        guessed_states.append(answer_state)

states_to_learn_csv = []
for n in states_list:
    if not n in guessed_states:
        states_to_learn_csv.append(n)

new_data = pandas.DataFrame(states_to_learn_csv)
new_data.to_csv("states_to_learn.csv")