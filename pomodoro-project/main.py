from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 7 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Dynamic typing to change data type from int to
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato image
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)  # for tomato.png
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(104, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130,
                                text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # variable for count_down
canvas.grid(row=1, column=1)

# Timer text
timer_label = Label(text="Timer", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Start button
start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

# Reset button
reset = Button(text="Reset")
reset.grid(row=2, column=2)

# Checkmark image
checkmarks = Canvas(width=24, height=24, bg=YELLOW, highlightthickness=0)
checkmark_img = PhotoImage(file="checkmark.png")
checkmarks.create_image(12, 12, image=checkmark_img)
checkmarks.grid(row=3, column=1)

window.mainloop()
