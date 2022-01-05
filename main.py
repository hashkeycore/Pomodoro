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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    global reps
    checkmark['text'] = ""
    reps = 0
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text='Timer')
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global reps
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps == 0 or reps % 2 == 0:
        count_down(work_sec)
        label['text'] = 'WORK'
    elif (reps == 1 or reps % 2 != 0) and reps != 7:
        count_down(short_sec)
        label['text'] = 'SHR BREAK'
        label['fg'] = PINK
    else:
        count_down(long_sec)
        label['text'] = 'LNG BREAK'
        label['fg'] = RED


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(100, count_down, count - 1)
    elif reps <= 7:
        # ADD CHECKMARK IF WORK REP DONE
        if reps == 0 or reps % 2 == 0:
            checkmark['text'] = f'{checkmark["text"] + "✔"}'
        reps += 1
        start_pomodoro()


# ---------------------------- UI SETUP ------------------------------- #
# Crea Finestra
window = Tk()

# Dai un titolo
window.title("Pomodoro")

# Config Finestra
window.config(padx=100, pady=50, bg=YELLOW)

# Imposta Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Prepara immagine Pomodo per essere usata nel canvas
pomodoro_img = PhotoImage(file='tomato.png')

# Crea immagine nel canvas
canvas.create_image(100, 112, image=pomodoro_img)

# Crea Testo Nel canvas e assegnalo ad una variabile timertext
timer_text = canvas.create_text(103, 130, text='00:00', fill="white", font=(FONT_NAME, 35, 'bold'))

# Crea Label Timer
label = Label(text="Timer", fg="green", bg=YELLOW, font=(FONT_NAME, 40), highlightthickness=0)
label.grid(column=2, row=1)
# label.pack()

# Crea Bottoni


start_button = Button(text='Start', command=start_pomodoro)
start_button.grid(ipadx=10, ipady=5, row=3, column=1)

reset_button = Button(text='Reset', command=reset_pomodoro)
reset_button.grid(ipadx=10, ipady=5, row=3, column=3)

checkmark = Label(fg='green', bg=YELLOW)
checkmark.grid(column=2, row=4)

canvas.grid(column=2, row=2)

window.mainloop()
