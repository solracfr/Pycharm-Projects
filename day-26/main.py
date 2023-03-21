from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Entry
text_input = Entry()
text_input.grid(row=0, column=1)

# Label for "miles"
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# Label for "is equal to"
equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

# Label for km number
km_num_label = Label(text="0", font=("Arial", 24, "bold"))
km_num_label.grid(row=1, column=1)  # places label on the window, without it the label will not show up

# Label for "Km"
km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(row=1, column=2)  # places label on the window, without it the label will not show up


# Button
def button_clicked():
    number_input = float(text_input.get())
    km = round(number_input * 1.609344, 2)  # round it by 2 decimal places
    km_num_label.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)


window.mainloop()
