from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from pathlib import Path
import time, os
import pygame

# tab 1
pygame.mixer.init()
kumite_counter = 0
kumite_running = False
kumite_red_score = 0
kumite_red_warnings_count = 0
kumite_senshu_aka = 0
kumite_blue_score = 0
kumite_blue_warnings_count = 0
kumite_senshu_ao = 0

# tab 2
patvar = 0
window_width = 1918
window_height = 1030

# tab 3
sparring_counter = 0
sparring_running = False
sparring_red_warnings = 0
sparring_red_fouls = 0
sparring_blue_warnings = 0
sparring_blue_fouls = 0
sparring_round_counter = 0

gui = Tk()
gui.geometry('1000x500')
gui.title("King of PMA II")

nb = ttk.Notebook(gui, width=window_width, height=window_height)
nb.pack()
tab1 = Frame(nb)
nb.add(tab1, text='Kumite')
tab2 = Frame(nb)
nb.add(tab2, text='Patterns')
tab3 = Frame(nb)
nb.add(tab3, text='Sparring')


C1 = Canvas(tab1, bg="white", height=window_width, width=window_width)
img_filename1 = PhotoImage(file=Path(__file__).resolve().parent / "bg_image - kumite.png")
background_label1 = Label(tab1, image=img_filename1)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)
C1.pack()
C2 = Canvas(tab2, bg="white", height=window_width, width=window_width)
img_filename2 = PhotoImage(file=Path(__file__).resolve().parent / "bg_image.png")
background_label2 = Label(tab2, image=img_filename2)
background_label2.place(x=0, y=0, relwidth=1, relheight=1)
C2.pack()
C3 = Canvas(tab3, bg="white", height=window_width, width=window_width)
img_filename3 = PhotoImage(file=Path(__file__).resolve().parent / "bg_image.png")
background_label3 = Label(tab3, image=img_filename3)
background_label3.place(x=0, y=0, relwidth=1, relheight=1)
C3.pack()


##
## TAB 1
##

def kumite_play_sound(sound_type):
    root_dir = Path(__file__).resolve().parent
    if sound_type == "short_beep":
        pygame.mixer.music.load(root_dir / "short_beep.mp3")
        pygame.mixer.music.play()
    elif sound_type == "long_beep":
        pygame.mixer.music.load(root_dir / "long_beep.mp3")
        pygame.mixer.music.play()
def kumite_update_counter(*args):
    selected_time = kumite_time_var.get()
    kumite_time_label.config(text=str(selected_time))
    hours, minutes = map(int, selected_time.split(':'))
    global kumite_counter
    kumite_counter = hours * 60 + minutes
def kumite_counter_label(kumite_label):
    def kumite_count():
        global kumite_counter
        if kumite_running:
            tt = datetime.fromtimestamp(kumite_counter)
            string = tt.strftime("%M:%S")
            print(string)
            display = string
            kumite_label.config(text=display)
            kumite_label.after(1000, kumite_count)
            kumite_counter -= 1
            if kumite_counter == 14:
                kumite_play_sound("short_beep")
                time.sleep(0.3)
                kumite_play_sound("short_beep")
            if kumite_counter == -1:
                kumite_Stop()
                kumite_play_sound("long_beep")
    kumite_count()
def kumite_Start(kumite_label):
    global kumite_running
    kumite_running = True
    kumite_counter_label(kumite_label)
    kumite_start['state'] = 'disabled'
    kumite_stop['state'] = 'normal'
    kumite_reset['state'] = 'normal'
def kumite_Stop():
    global kumite_running
    kumite_start['state'] = 'normal'
    kumite_stop['state'] = 'disabled'
    kumite_reset['state'] = 'normal'
    kumite_running = False
def kumite_Reset(kumite_label):
    kumite_update_counter()
    if kumite_running == False:
        kumite_reset['state'] = 'disabled'
        kumite_label['text'] = kumite_time_var.get()
    else:
        kumite_label['text'] = 'Starting...'
def kumite_single_point_score_red():
    global kumite_red_score
    kumite_red_score += 1
    label_red_score.config(text=kumite_red_score)
def kumite_remove_single_point_red():
    global kumite_red_score
    kumite_red_score -= 1
    label_red_score.config(text=kumite_red_score)
def kumite_single_point_score_blue():
    global kumite_blue_score
    kumite_blue_score += 1
    label_blue_score.config(text=kumite_blue_score)
def kumite_remove_single_point_blue():
    global kumite_blue_score
    kumite_blue_score -= 1
    label_blue_score.config(text=kumite_blue_score)
def kumite_reset_all():
    global kumite_red_score, kumite_red_warnings_count
    global kumite_blue_score, kumite_blue_warnings_count
    global kumite_senshu_aka, kumite_senshu_ao
    kumite_red_score, kumite_red_warnings_count = 0, 0
    kumite_blue_score, kumite_blue_warnings_count = 0, 0
    kumite_senshu_aka, kumite_senshu_ao = 0, 0
    label_red_score.config(text=kumite_red_score)
    label_red_chui.config(text=kumite_red_warnings_count*"* ")
    label_red_senshu.config(text=kumite_senshu_aka*"⧆")
    label_blue_score.config(text=kumite_blue_score)
    label_blue_chui.config(text=kumite_blue_warnings_count*"* ")
    label_blue_senshu.config(text=kumite_senshu_ao*"⧆")
def kumite_warn_red():
    global kumite_red_warnings_count
    kumite_red_warnings_count += 1
    label_red_chui.config(text=kumite_red_warnings_count*"* ")
def kumite_remove_red_warn():
    global kumite_red_warnings_count
    kumite_red_warnings_count -= 1
    label_red_chui.config(text=kumite_red_warnings_count*"* ")
def kumite_warn_blue():
    global kumite_blue_warnings_count
    kumite_blue_warnings_count += 1
    label_blue_chui.config(text=kumite_blue_warnings_count*"* ")
def kumite_remove_blue_warn():
    global kumite_blue_warnings_count
    kumite_blue_warnings_count -= 1
    label_blue_chui.config(text=kumite_blue_warnings_count*"* ")
def kumite_award_seshu_aka():
    global kumite_senshu_aka
    kumite_senshu_aka = (kumite_senshu_aka + 1) % 2
    label_red_senshu.config(text=kumite_senshu_aka*"⧆")
def kumite_award_senshu_ao():
    global kumite_senshu_ao
    kumite_senshu_ao = (kumite_senshu_ao + 1) % 2
    label_blue_senshu.config(text=kumite_senshu_ao*"⧆")

kumite_time_var = StringVar(tab1)
kumite_time_var.set("Select Timer")
option_list = ["03:00", 
               "02:30", 
               "02:00", 
               "01:00", 
               "00:30", 
               "00:20", 
               "00:18",
               "00:16",
               "00:14",
               "00:12",
               "00:10",
               "00:09",
               "00:08",
               "00:07",
               "00:06",
               "00:05",
               "00:04",
               "00:03",
               "00:02",
               "00:01",
               ]
kumite_timer_select = OptionMenu(tab1, kumite_time_var, *option_list)
kumite_timer_select.place(relx=0.5, rely=0.45, anchor="center")
kumite_counter = IntVar(tab1)
kumite_time_var.trace('w', kumite_update_counter)

kumite_time_label = Label(tab1, text="00:00", fg="white", font="Verdana 100 bold", bg="black", width=50)
kumite_time_label.place(relx=0.5, rely=0.55, anchor='center')

kumite_start = Button(tab1, text='Start', font="Verdana 10 bold", command=lambda: kumite_Start(kumite_time_label))
kumite_start.place(relx=0.5, rely=0.89, anchor='center')
kumite_stop = Button(tab1, text='Stop', font="Verdana 10 bold", state='disabled', command=kumite_Stop)
kumite_stop.place(relx=0.5, rely=0.92, anchor='center')
kumite_reset = Button(tab1, text='Reset', font="Verdana 10 bold", state='disabled', command=lambda: kumite_Reset(kumite_time_label))
kumite_reset.place(relx=0.5, rely=0.95, anchor='center')
kumite_reset_all_button = Button(tab1, text='Reset Scores', font='verdana 10 bold', command=kumite_reset_all)
kumite_reset_all_button.place(relx=0.5, rely=0.98, anchor='center')

label_red_score = Label(tab1, text=kumite_red_score, font='Verdana 275 bold', bg='#ed1c24', fg='white')
label_red_score.place(relx=0.25, rely=0.02, anchor='n')
senshu_aka_button = Button(tab1, text="AKA", font="verdana 35 bold", command=kumite_award_seshu_aka)
senshu_aka_button.place(relx=0.25, rely=0.05, anchor='center')
button_red_warn = Button(tab1, text="Penalty:", font="verdana 25 bold", command=kumite_warn_red)
button_red_warn.place(relx=0.05, rely=0.67, anchor='w')
label_red_chui = Label(tab1, text=kumite_red_warnings_count*"* ", font="verdana 100 bold", bg='#ed1c24', fg='yellow')
label_red_chui.place(relx=0.05, rely=0.8, anchor='w')
label_red_senshu = Label(tab1, text=kumite_senshu_aka*"⧆", fg="yellow", font="versana 50 bold", bg="#ed1c24")
label_red_senshu.place(relx=0.40, rely=0.12, anchor='w')

label_blue_score = Label(tab1, text=kumite_blue_score, font='Verdana 275 bold', bg='#2744a0', fg='white')
label_blue_score.place(relx=0.75, rely=0.02, anchor='n')
senshu_ao_button = Button(tab1, text="AO", font="verdana 35 bold", command=kumite_award_senshu_ao)
senshu_ao_button.place(relx=0.75, rely=0.05, anchor='center')
button_blue_warn = Button(tab1, text="Penalty:", font="verdana 25 bold", command=kumite_warn_blue)
button_blue_warn.place(relx=0.55, rely=0.67, anchor='w')
label_blue_chui = Label(tab1, text=kumite_blue_warnings_count*"* ", font="verdana 100 bold", bg='#2744a0', fg='yellow')
label_blue_chui.place(relx=0.55, rely=0.8, anchor='w')
label_blue_senshu = Label(tab1, text=kumite_senshu_ao*"⧆", fg="yellow", font="versana 50 bold", bg="#2744a0")
label_blue_senshu.place(relx=0.90, rely=0.12, anchor='w')

red_dec_score = Button(tab1, text="-", font="verdana 10 bold", command=kumite_remove_single_point_red)
red_dec_score.place(relx=0.207, rely=0.07)
red_inc_score = Button(tab1, text="+", font="verdana 10 bold", command=kumite_single_point_score_red)
red_inc_score.place(relx=0.279, rely=0.07)
blue_dec_score = Button(tab1, text="-", font="verdana 10 bold", command=kumite_remove_single_point_blue)
blue_dec_score.place(relx=0.716, rely=0.07)
blue_inc_score = Button(tab1, text="+", font="verdana 10 bold", command=kumite_single_point_score_blue)
blue_inc_score.place(relx=0.77, rely=0.07)

red_dec_warn = Button(tab1, text="-", font="verdana 10 bold", command=kumite_remove_red_warn)
red_dec_warn.place(relx=0.05, rely=0.68)
blue_dec_warn = Button(tab1, text="-", font="verdana 10 bold", command=kumite_remove_blue_warn)
blue_dec_warn.place(relx=0.55, rely=0.68)


##
## TAB 2
##

firstdanlist = [
                    'Chon-Ji', #0
                    'Dan-Gun', #1
                    'Do-San', #2
                    'Won-Hyo', #3
                    'Yul-Gok', #4
                    'Joong-Gun', #5
                    'Toi-Gye', #6
                    'Hwa-Rang', #7
                    'Choong-Moo', #8
                    'Kwang-Gae', #9
                    'Po-Eun', #10
                    'Gae-Baek', #11
        ]
seconddanlist = [
            "Chon-Ji", #0
            "Dan-Gun", #1
            "Do-San", #2
            "Won-Hyo", #3
            "Yul-Gok", #4
            "Joong-Gun", #5
            "Toi-Gye", #6
            "Hwa-Rang", #7
            "Choong-Moo", #8
            "Kwang-Gae", #9
            "Po-Eun", #10
            "Gae-Baek", #11
            "Eui-Am", #12 
            "Choong-Jang", #13
            "Juche", #14
]
thirddanlist = [
            "Chon-Ji", #0
            "Dan-Gun", #1
            "Do-San", #2
            "Won-Hyo", #3
            "Yul-Gok", #4
            "Joong-Gun", #5
            "Toi-Gye", #6
            "Hwa-Rang", #7
            "Choong-Moo", #8
            "Kwang-Gae", #9
            "Po-Eun", #10
            "Gae-Baek", #11
            "Eui-Am", #12 
            "Choong-Jang", #13
            "Juche", #14
            "Sam-Il", #15
            "Yoo-Sin", #16
            "Choi-Yong", #17
]
fourthdanlist = [
                    "Chon-Ji", #0
                    "Dan-Gun", #1
                    "Do-San", #2
                    "Won-Hyo", #3
                    "Yul-Gok", #4
                    "Joong-Gun", #5
                    "Toi-Gye", #6
                    "Hwa-Rang", #7
                    "Choong-Moo", #8
                    "Kwang-Gae", #9
                    "Po-Eun", #10
                    "Gae-Baek", #11
                    "Eui-Am", #12 
                    "Choong-Jang", #13
                    "Juche", #14
                    "Sam-Il", #15
                    "Yoo-Sin", #16
                    "Choi-Yong", #17
                    "Yong-Gae", #18
                    "Ul-Ji", #19
                    "Moon-Moo" #20
        ]

pattern_string = ""
pattern_label = Label(tab2, text=pattern_string, font = "Verdana 180 bold", bg = "white")
pattern_label.place(relx=0.5, rely=0.2, anchor='center')

def firstdan():
    global pattern1, pattern2, patvar
    copylist = firstdanlist.copy()
    num1 = random.randint(9,11)
    pattern1 = copylist[num1]
    print(copylist[num1])
    copylist.remove(copylist[num1])
    num2 = random.randint(0, 10)
    pattern2 = copylist[num2]
    print(copylist[num2])
def seconddan():
    global pattern1, pattern2, patvar
    copylist = seconddanlist.copy()
    num1 = random.randint(12,14)
    pattern1 = copylist[num1]
    print(copylist[num1])
    copylist.remove(copylist[num1])
    num2 = random.randint(0, 13)
    pattern2 = copylist[num2]
    print(copylist[num2])
def thirddan():
    global pattern1, pattern2, patvar
    copylist = thirddanlist.copy()
    num1 = random.randint(15,17)
    pattern1 = copylist[num1]
    print(copylist[num1])
    copylist.remove(copylist[num1])
    num2 = random.randint(0, 16)
    pattern2 = copylist[num2]
    print(copylist[num2])
def fourthdan():
    global pattern1, pattern2, patvar
    copylist = fourthdanlist.copy()
    num1 = random.randint(18,20)
    pattern1 = copylist[num1]
    print(copylist[num1])
    copylist.remove(copylist[num1])
    num2 = random.randint(0, 19)
    pattern2 = copylist[num2]
    print(copylist[num2])
def display():
    global patvar
    if patvar == 0:
        pattern_label.config(text=pattern1)
        patvar = 1
    elif patvar == 1:
        pattern_label.config(text=pattern2)
        patvar = 0
def pattern_reset():
    global patvar
    pattern_label.config(text="")
    patvar = 0

firstdan1 = Button(tab2, text="1st Dan - Generate", command = firstdan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan1.place(relx=0.05, rely=0.90, anchor='center')
firstdan2 = Button(tab2, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan2.place(relx=0.05, rely=0.95, anchor='center')
seconddan1 = Button(tab2, text="2nd Dan - Generate", command = seconddan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
seconddan1.place(relx=0.35, rely=0.90, anchor='center')
seconddan2 = Button(tab2, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
seconddan2.place(relx=0.35, rely=0.95, anchor='center')
thirddan1 = Button(tab2, text="3rd Dan - Generate", command = thirddan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
thirddan1.place(relx=0.65, rely=0.90, anchor='center')
thirddan2 = Button(tab2, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
thirddan2.place(relx=0.65, rely=0.95, anchor='center')
fourthdan1 = Button(tab2, text="4th-6th Dan - Generate", command = fourthdan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
fourthdan1.place(relx=0.95, rely=0.90, anchor='center')
fourthdan2 = Button(tab2, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
fourthdan2.place(relx=0.95, rely=0.95, anchor='center')
patternreset = Button(tab2, text="Reset", command = pattern_reset, width=10, height=1, fg='white', bg='black', font="Verdana 8")
patternreset.place(relx=0.5, rely=0.01, anchor='center')


##
## TAB 3
##

tab3.grid_columnconfigure(1,weight=1)
tab3.grid_columnconfigure(2,weight=1)
tab3.grid_columnconfigure(3,weight=1)
tab3.grid_columnconfigure(4,weight=1)
tab3.grid_columnconfigure(5,weight=1)
tab3.grid_rowconfigure(0,weight=1)
tab3.grid_rowconfigure(1,weight=1)
tab3.grid_rowconfigure(2,weight=1)
tab3.grid_rowconfigure(3,weight=1)
tab3.grid_rowconfigure(4,weight=1)
tab3.grid_rowconfigure(5,weight=1)
tab3.grid_rowconfigure(6,weight=1)
tab3.grid_rowconfigure(7,weight=1)
tab3.grid_rowconfigure(8,weight=1)

def sparring_counter_label(label):
    def sparring_count():
        if sparring_running:
            global sparring_counter
            tt = datetime.fromtimestamp(sparring_counter)
            string = tt.strftime("%M:%S")
            display = string
            label.config(text=display)
            label.after(1000, sparring_count)
            sparring_counter += 1
    sparring_count()
def sparring_Start(label):
    global sparring_running
    sparring_running = True
    sparring_counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
def sparring_Stop():
    global sparring_running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    sparring_running = False
def sparring_Reset(label):
    global sparring_counter
    sparring_counter = 0
    if sparring_running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Ready'
    else:
        label['text'] = 'Starting...'
def sparring_warn_red_inc():
    global sparring_red_warnings
    sparring_red_warnings += 1
    label_red_warnings.config(text=sparring_red_warnings)
def sparring_warn_red_dec():
    global sparring_red_warnings
    sparring_red_warnings -= 1
    label_red_warnings.config(text=sparring_red_warnings)
def sparring_warn_blue_inc():
    global sparring_blue_warnings
    sparring_blue_warnings += 1
    label_blue_warnings.config(text=sparring_blue_warnings)
def sparring_warn_blue_dec():
    global sparring_blue_warnings
    sparring_blue_warnings -= 1
    label_blue_warnings.config(text=sparring_blue_warnings)
def sparring_round_counter_inc():
    global sparring_round_counter
    sparring_round_counter += 1
    label_round_counter.config(text=sparring_round_counter)
def sparring_round_counter_dec():
    global sparring_round_counter
    sparring_round_counter -= 1
    label_round_counter.config(text=sparring_round_counter)
def sparring_red_foul_inc():
    global sparring_red_fouls
    sparring_red_fouls += 1
    label_red_fouls.config(text=sparring_red_fouls)
def sparring_red_foul_dec():
    global sparring_red_fouls
    sparring_red_fouls -= 1
    label_red_fouls.config(text=sparring_red_fouls)
def sparring_blue_foul_inc():
    global sparring_blue_fouls
    sparring_blue_fouls += 1
    label_blue_fouls.config(text=sparring_blue_fouls)
def sparring_blue_foul_dec():
    global sparring_blue_fouls
    sparring_blue_fouls -= 1
    label_blue_fouls.config(text=sparring_blue_fouls)
def sparring_reset_all():
    global sparring_red_warnings, sparring_blue_warnings, sparring_round_counter, sparring_red_fouls, sparring_blue_fouls, time_label
    sparring_red_warnings = 0
    sparring_blue_warnings = 0
    sparring_round_counter = 0
    sparring_red_fouls = 0
    sparring_blue_fouls = 0
    label_red_warnings.config(text=sparring_red_warnings)
    label_blue_warnings.config(text=sparring_blue_warnings)
    label_round_counter.config(text=sparring_round_counter)
    label_red_fouls.config(text=sparring_red_fouls)
    label_blue_fouls.config(text=sparring_blue_fouls)
    sparring_Stop()
    sparring_Reset(time_label)

time_label = Label(tab3, text="Ready", bg='black', fg="white", font="Verdana 130 bold")
start = Button(tab3, text='Start Time', font="Verdana 10 bold", width=10, height=2, command=lambda: sparring_Start(time_label))
stop = Button(tab3, text='Stop Time', font="Verdana 10 bold", width=10, height=2, state='disabled', command=sparring_Stop)
reset = Button(tab3, text='Reset Time', font="Verdana 10 bold", width=10, height=2, state='disabled', command=lambda: sparring_Reset(time_label))

label_red_warnings = Label(tab3, text=sparring_red_warnings, font='Verdana 300 bold', bg='#2744a0', fg='white')
label_red_fouls = Label(tab3, text=sparring_red_fouls, font='Verdana 200 bold', bg='#2744a0', fg='white')
label_blue_warnings = Label(tab3, text=sparring_blue_warnings, font='Verdana 300 bold', bg='#ed1c24', fg='white')
label_blue_fouls = Label(tab3, text=sparring_blue_fouls, font='Verdana 200 bold', bg='#ed1c24', fg='white')
label_round_counter = Label(tab3, text=sparring_round_counter, font='Verdana 100 bold', bg='black', fg='white')
rw = Label(tab3, text="Warnings", font='Verdana 10 bold', bg='#2744a0', fg='white')
bw = Label(tab3, text="Warnings", font='Verdana 10 bold', bg='#ed1c24', fg='white')
rf = Label(tab3, text="Fouls", font='Verdana 10 bold', bg='#2744a0', fg='white')
bf = Label(tab3, text="Fouls", font='Verdana 10 bold', bg='#ed1c24', fg='white')
round = Label(tab3, text="Round", font='Verdana 10 bold', bg='black', fg='white')

redwarninc = Button(tab3, text="redwarning+", font='Verdana 5 bold', command=sparring_warn_red_inc, width=15, height=4)
redwarndec = Button(tab3, text="redwarning-", font='Verdana 5 bold', command=sparring_warn_red_dec, width=15, height=4)
redfoulinc = Button(tab3, text="redfoul+", font='Verdana 5 bold', command=sparring_red_foul_inc, width=15, height=4)
redfouldec = Button(tab3, text="redfoul-", font='Verdana 5 bold', command=sparring_red_foul_dec, width=15, height=4)
bluewarninc = Button(tab3, text="bluewarning+", font='Verdana 5 bold', command=sparring_warn_blue_inc, width=15, height=4)
bluewarndec = Button(tab3, text="bluewarning-", font='Verdana 5 bold', command=sparring_warn_blue_dec, width=15, height=4)
bluefoulinc = Button(tab3, text="bluefoul+", font='Verdana 5 bold', command=sparring_blue_foul_inc, width=15, height=4)
bluefouldec = Button(tab3, text="bluefoul-", font='Verdana 5 bold', command=sparring_blue_foul_dec, width=15, height=4)
roundcounterinc = Button(tab3, text="round+", font='Verdana 5 bold', command=sparring_round_counter_inc, width=15, height=4)
roundcounterdec = Button(tab3, text="round-", font='Verdana 5 bold', command=sparring_round_counter_dec, width=15, height=4)
reset_all = Button(tab3, text='Reset All', command=sparring_reset_all, width=15)

time_label.place(relx=0.5, rely=0.1, anchor='center')
start.place(relx=0.5, rely=0.75, anchor='center')
stop.place(relx=0.5, rely=0.85, anchor='center')
reset.place(relx=0.5, rely=0.94, anchor='center')
reset_all.place(relx=0.5, rely=0.98, anchor='center')

label_red_warnings.place(relx=0.305, rely=0.50, anchor='center')
label_red_fouls.place(relx=0.095, rely=0.50, anchor='center')
label_blue_warnings.place(relx=0.695, rely=0.50, anchor='center')
label_blue_fouls.place(relx=0.905, rely=0.50, anchor='center')
label_round_counter.place(relx=0.5, rely=0.5105, anchor='center')

rw.place(relx=0.305, rely=0.30, anchor='center')
rf.place(relx=0.095, rely=0.339, anchor='center')
bw.place(relx=0.695, rely=0.30, anchor='center')
bf.place(relx=0.905, rely=0.339, anchor='center')
round.place(relx=0.50, rely=0.379, anchor='center')

redwarninc.place(relx=0.305, rely=0.332, anchor='center')
redwarndec.place(relx=0.305, rely=0.69, anchor='center')
redfoulinc.place(relx=0.095, rely=0.372, anchor='center')
redfouldec.place(relx=0.095, rely=0.65, anchor='center')
bluewarninc.place(relx=0.695, rely=0.332, anchor='center')
bluewarndec.place(relx=0.695, rely=0.69, anchor='center')
bluefoulinc.place(relx=0.905, rely=0.372, anchor='center')
bluefouldec.place(relx=0.905, rely=0.65, anchor='center')
roundcounterinc.place(relx=0.50, rely=0.411, anchor='center')
roundcounterdec.place(relx=0.50, rely=0.613, anchor='center')




gui.mainloop()