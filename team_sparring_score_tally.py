import tkinter as tk
from datetime import datetime
from pynput import keyboard


def quit_me():
    print('quit')
    root.quit()
    root.destroy()
    quit()

root = tk.Tk()
root.title("Performance Taekwon-Do | Team Sparring")
root.protocol("WM_DELETE_WINDOW", quit_me)

bg = tk.PhotoImage(file="bg_image.png")
main_title = tk.Label(root, image=bg)
main_title.place(x=0, y=0, relwidth=1, relheight=1)

root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_columnconfigure(4,weight=1)
root.grid_columnconfigure(5,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_rowconfigure(4,weight=1)
root.grid_rowconfigure(5,weight=1)
root.grid_rowconfigure(6,weight=1)
root.grid_rowconfigure(7,weight=1)
root.grid_rowconfigure(8,weight=1)

counter = 0
running = False
red_score = 0
blue_score = 0
tie_score = 0

def counter_label(label):
    def count():
        if running:
            global counter
            tt = datetime.fromtimestamp(counter)
            string = tt.strftime("%M:%S")
            display = string
            label.config(text=display)
            label.after(1000, count)
            counter += 1
    count()
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False
def Reset(label):
    global counter
    counter = 0
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Ready'
    else:
        label['text'] = 'Starting...'
def score_red_inc():
    global red_score
    red_score += 1
    label_red_score.config(text=red_score)
def score_red_dec():
    global red_score
    red_score -= 1
    label_red_score.config(text=red_score)
def score_blue_inc():
    global blue_score
    blue_score += 1
    label_blue_score.config(text=blue_score)
def score_blue_dec():
    global blue_score
    blue_score -= 1
    label_blue_score.config(text=blue_score)
def score_tie_inc():
    global tie_score
    tie_score += 1
    label_tie_score.config(text=tie_score)
def score_tie_dec():
    global tie_score
    tie_score -= 1
    label_tie_score.config(text=tie_score)
def reset_all():
    global red_score, blue_score, tie_score
    red_score = 0
    blue_score = 0
    tie_score = 0
    label_red_score.config(text=red_score)
    label_blue_score.config(text=blue_score)
    label_tie_score.config(text=tie_score)

time_label = tk.Label(root, text="Ready", bg='black', fg="white", font="Verdana 150 bold")
start = tk.Button(root, text='Start', font="Verdana 10 bold", width=10, height=2, command=lambda: Start(time_label))
stop = tk.Button(root, text='Stop', font="Verdana 10 bold", width=10, height=2, state='disabled', command=Stop)
reset = tk.Button(root, text='Reset', font="Verdana 10 bold", width=10, height=2, state='disabled', command=lambda: Reset(time_label))
label_red_score = tk.Label(root, text=red_score, font='Verdana 250 bold', bg='black', fg='white')
label_blue_score = tk.Label(root, text=blue_score, font='Verdana 250 bold', bg='black', fg='white')
label_tie_score = tk.Label(root, text=tie_score, font='Verdana 160 bold', bg='black', fg='white')
redscoreinc = tk.Button(root, text="+1 point", font='Verdana 10 bold', command=score_red_inc, width=7, height=1)
redscoredec = tk.Button(root, text="-1 point", font='Verdana 10 bold', command=score_red_dec, width=7, height=1)
bluescoreinc = tk.Button(root, text="+1 point", font='Verdana 10 bold', command=score_blue_inc, width=7, height=1)
bluescoredec = tk.Button(root, text="-1 point", font='Verdana 10 bold', command=score_blue_dec, width=7, height=1)
tiescoreinc = tk.Button(root, text="+1 point", font='Verdana 10 bold', command=score_tie_inc, width=7, height=1)
tiescoredec = tk.Button(root, text="-1 point", font='Verdana 10 bold', command=score_tie_dec, width=7, height=1)
reset_all = tk.Button(root, text='Reset Scores', command=reset_all, width=15)


time_label.grid(row=1, column=3)
start.grid(row=6, column=3)
stop.grid(row=7, column=3)
reset.grid(row=8, column=3)
reset_all.grid(row=9, column=3)
label_red_score.grid(row=2, column=2)
label_blue_score.grid(row=2, column=4)
label_tie_score.grid(row=2, column=3)

redscoreinc.place(relx=0.18, rely=0.283, anchor='center')
redscoredec.place(relx=0.18, rely=0.698, anchor='center')
bluescoreinc.place(relx=0.82, rely=0.283, anchor='center')
bluescoredec.place(relx=0.82, rely=0.698, anchor='center')
tiescoreinc.place(relx=0.5, rely=0.353, anchor='center')
tiescoredec.place(relx=0.5, rely=0.628, anchor='center')


COMBINATIONS = []
red_inc = [{keyboard.KeyCode(char='r')}]
blue_inc = [{keyboard.KeyCode(char='b')}]
red_dec = [{keyboard.KeyCode(char='t')}]
blue_dec = [{keyboard.KeyCode(char='n')}]
tie_inc = [{keyboard.KeyCode(char='d')}]
tie_dec = [{keyboard.KeyCode(char='f')}]
timestart = [{keyboard.KeyCode(char='q')}]
timepause = [{keyboard.KeyCode(char='a')}]
timerestart = [{keyboard.KeyCode(char='z')}]
current = set()

def on_press(key):
    if any([key in COMBO for COMBO in red_inc]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in red_inc):
            score_red_inc()
    elif any([key in COMBO for COMBO in blue_inc]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in blue_inc):
            score_blue_inc()
    elif any([key in COMBO for COMBO in red_dec]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in red_dec):
            score_red_dec()
    elif any([key in COMBO for COMBO in blue_dec]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in blue_dec):
            score_blue_dec()
    elif any([key in COMBO for COMBO in tie_inc]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in tie_inc):
            score_tie_inc()
    elif any([key in COMBO for COMBO in tie_dec]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in tie_dec):
            score_tie_dec()
    elif any([key in COMBO for COMBO in timestart]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in timestart):
            Start(time_label)
    elif any([key in COMBO for COMBO in timepause]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in timepause):
            Stop()
    elif any([key in COMBO for COMBO in timerestart]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in timerestart):
            Reset(time_label)
def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    root.mainloop()
    listener.join()


root.mainloop()