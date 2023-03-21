import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # grab the image from this directory
screen.addshape(image)  # add the image to the screen
turtle.shape(image)

# correct guesses
states_guessed = []

# get dataframe from states data
df = pandas.read_csv("50_states.csv")

while len(states_guessed) < 50:
    # prompt user again at the end of the loop
    answer_state = screen.textinput(title=f"{len(states_guessed)} / 50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break  # frees us from the tyranny of the while loop

    # check if your answer is in our dataframe and has not been guessed before
    # THIS RIGHT HERE IS THE FUCKING KEY OF THIS LOGIC
    # if you converted the states into a list, then you can just check within that list. no need for .values
    if answer_state in df.state.values and answer_state not in states_guessed:

        # get state coordinates and convert to ints
        x = int(df[df.state == answer_state].x)
        y = int(df[df.state == answer_state].y)

        # create a new thingy to write
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(x=x, y=y)
        state_name.write(arg=answer_state)

        # increase player stats and record status
        states_guessed.append(answer_state)
        print(f"your score is: {len(states_guessed)}")
        print("you have correctly guessed: ", states_guessed)
    elif answer_state in df.state.values and answer_state in states_guessed:
        print("you have already guessed this state! no repeats!")
    else:
        print("nah lmao")

states_missed = []
for state in df.state.values:
    if state not in states_guessed:
        states_missed.append(state)

new_data = pandas.DataFrame(states_missed)
new_data.to_csv("missed_states.csv")

print("Here are the states you missed:\n", states_missed)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)  # when the screen is clicked, the mouse's xy coordinates are recorded
turtle.mainloop()  # continue to run the turtle program even though main.py is technically done
