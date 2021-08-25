import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()

states_list = data.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 states guessed", prompt="Guess a state:").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in correct_guesses]
        # for state in states_list:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        final_data = pandas.DataFrame(missing_states)
        final_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state_row = data[data.state == answer_state]
        state_name.goto(int(state_row.x), int(state_row.y))
        state_name.write(answer_state)
