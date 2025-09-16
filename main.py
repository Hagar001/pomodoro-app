from tkinter import *
import math
import pygame

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
paused = False
resume = False
counter = 0

# ---------------------------- SOUND EFFECTS ------------------------------- # 
def play_sound():
    sound.play()
    window.after(5000, stop_sound)

def stop_sound():
    sound.stop()

# ---------------------------- TIMER RESET ------------------------------- # 
def pause_resume():
    global paused, reps, resume

    if not paused: # Pause
        window.after_cancel(timer)
        paused = True
        pause_resume_button.config(text="Resume")
    else: # Resume
        paused = False
        pause_resume_button.config(text="Pause")
        resume = True
        start()

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN, padx=60)
    check_marks.config(text="")
    start_button.config(state=NORMAL)
    pause_resume_button.config(text="Pause" ,state=DISABLED)
    global reps, paused, resume
    reps = 0
    paused = False
    resume = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    start_button.config(state=DISABLED)
    pause_resume_button.config(state=NORMAL)
    global reps, resume, counter

    if resume:
        count_down(counter)
        resume = False
    else:
        reps += 1
        if reps % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            title_label.config(text="Break 🥳", fg=RED, padx=1)
            play_sound()
        elif reps % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
            title_label.config(text="Break ☕", fg=PINK, padx=1)
            play_sound()
        else:
            count_down(WORK_MIN * 60)
            title_label.config(text="POMO", fg=GREEN, padx=78)
            if reps != 1:
                play_sound()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer, counter
    counter = count

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=20, bg=YELLOW)
pygame.mixer.init()
sound = pygame.mixer.Sound("music.mp3")

# The tomato image, and the timer
canvas = Canvas(width=220, height=244, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) # I want it in the middel of the canva, so it takes half its x and y
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer text
title_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW, padx=60, pady=10)
title_label.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0 ,command=start)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0,command=reset)
reset_button.grid(column=2, row=2)

# Pause/ Resume Button
pause_resume_button = Button(text="Pause", font=(FONT_NAME, 10, "bold"), highlightthickness=0,command=pause_resume, state=DISABLED)
pause_resume_button.grid(column=1, row=2)

# Check Marks
check_marks = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW, padx=10, pady=15)
check_marks.grid(column=1, row=3)


window.mainloop()