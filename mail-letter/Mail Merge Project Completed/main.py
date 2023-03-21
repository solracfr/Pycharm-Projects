PLACEHOLDER = "[name]"

# Grab invited names from the text file
with open("./Input/Names/invited_names.txt", "r") as names_file:  # open contents of letter
    list_of_names = names_file.readlines()  # get each line returned as a list

with open("./Input/Letters/starting_letter.txt") as letter_file:  # open the contents of letter
    letter_contents = letter_file.read()  # record all the contents to a variable
    for name in list_of_names:
        name = name.strip()  # gets rid of new line
        new_letter = letter_contents.replace(PLACEHOLDER, name)  # gets contents of letter, and makes a replaced copy
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:  # makes a new file
            completed_letter.write(new_letter)  # is able to write because we put "w" in mode


    # # remove \n string from each name
    # for name in list_of_names:
    #     new_name = name.strip(r"\n")  # strip each new line from each name (does not affect Toph)
    #     print(new_name)


