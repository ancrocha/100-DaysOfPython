import turtle
import pandas
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.title(f"U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
scoreboard = Scoreboard()


score = 0
guessed_states = []
all_states = data.state.to_list()

while len(guessed_states) < 50:

    anwer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 - Guess the State", prompt="What's another state's name?").title()

    if anwer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if data['state'].eq(anwer_state).any():
        guessed_states.append(anwer_state)
        x_cor = int(data.x[data.state == anwer_state])
        y_cor = int(data.y[data.state == anwer_state])

        # use .item() bellow to get only the row value
        state_name = anwer_state
        scoreboard.update_scoreboard(x_cor, y_cor, state_name)
