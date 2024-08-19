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
def reset_timer():
    global reps
    window.after_cancel(time)
    timer_label.config(text="Timer")
    tick_label.config(text="")
    canvas.itemconfig(time_text,text="0:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0 and  reps != 0:
        timer(long_break)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        timer(short_break)
        timer_label.config(text="Break",fg=PINK)
    else:
        timer(work_sec)
        timer_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(count):
    time_min = math.floor(count/60)
    time_sec = count % 60
    if time_sec < 10:
        time_sec = f'0{time_sec}'
    canvas.itemconfig(time_text,text=f"{time_min}:{time_sec}")
    if count > 0:
        global time
        time = window.after(1000,timer,count - 1)
    else:
        start()
        mark= ""
        for _ in range(math.floor(reps/2)):
            mark += "/"
        tick_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100,pady=50,bg=YELLOW)
window.title("pomodoro-timer")

timer_label = Label(text="Timer",fg='green',width=10,height=2,font=(FONT_NAME,35,'bold'),bg=YELLOW)
timer_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image_tomato)
time_text = canvas.create_text(103,130,text="00:00",fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",command= start,highlightthickness=0)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)


tick_label = Label(fg='green')
tick_label.grid(row=3,column=1)
# canvas.create_text(103,130,text="Timer",fill='green',)
# canvas.grid(row=0,column=1)










window.mainloop()