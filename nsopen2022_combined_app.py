from tkinter import *
from tkinter import ttk
import random
from datetime import datetime

# tab 1
patvar = 0
window_width = 1918
window_height = 1030

# tab 2
counter = 0
running = False
red_warnings = 0
red_fouls = 0
blue_warnings = 0
blue_fouls = 0
round_counter = 0

# tab 3
counter3 = 0
running3 = False
red_score = 0
blue_score = 0
tie_score = 0

# tab 4
counter4 = 0
running4 = False
red_score4 = 0
blue_score4 = 0


gui = Tk()
gui.geometry('1918x1030')
gui.title("Performance Taekwon-Do | NS Open")

nb = ttk.Notebook(gui, width=window_width, height=window_height)
nb.pack()
tab1 = Frame(nb)
nb.add(tab1, text='Black Belt Patterns')
tab2 = Frame(nb)
nb.add(tab2, text='Sparring - Time, Warnings, Fouls')
tab3 = Frame(nb)
nb.add(tab3, text='Team Sparring - Time, Tally')
tab4 = Frame(nb)
nb.add(tab4, text='Flag Sparring - Time, Tally')


##
## TAB 1
##


C1 = Canvas(tab1, bg="white", height=window_width, width=window_width)
img_filename1 = PhotoImage(file=r'C:\\Users\\saone\\Documents\\Python Stuff\\basic_tkd_scoreboards\\bg_image.png')
background_label1 = Label(tab1, image=img_filename1)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)
C1.pack()
C2 = Canvas(tab2, bg="white", height=window_width, width=window_width)
img_filename2 = PhotoImage(file=r'C:\\Users\\saone\\Documents\\Python Stuff\\basic_tkd_scoreboards\\bg_image.png')
background_label2 = Label(tab2, image=img_filename2)
background_label2.place(x=0, y=0, relwidth=1, relheight=1)
C2.pack()
C3 = Canvas(tab3, bg="white", height=window_width, width=window_width)
img_filename3 = PhotoImage(file=r'C:\\Users\\saone\\Documents\\Python Stuff\\basic_tkd_scoreboards\\bg_image.png')
background_label3 = Label(tab3, image=img_filename3)
background_label3.place(x=0, y=0, relwidth=1, relheight=1)
C3.pack()
C4 = Canvas(tab4, bg="white", height=window_width, width=window_width)
img_filename4 = PhotoImage(file=r'C:\\Users\\saone\\Documents\\Python Stuff\\basic_tkd_scoreboards\\bg_image.png')
background_label4 = Label(tab4, image=img_filename4)
background_label4.place(x=0, y=0, relwidth=1, relheight=1)
C4.pack()


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
pattern_label = Label(tab1, text=pattern_string, font = "Verdana 180 bold", bg = "white")
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

firstdan1 = Button(tab1, text="1st Dan - Generate", command = firstdan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan1.place(relx=0.05, rely=0.90, anchor='center')
firstdan2 = Button(tab1, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan2.place(relx=0.05, rely=0.95, anchor='center')
seconddan1 = Button(tab1, text="2nd Dan - Generate", command = seconddan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
seconddan1.place(relx=0.35, rely=0.90, anchor='center')
seconddan2 = Button(tab1, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
seconddan2.place(relx=0.35, rely=0.95, anchor='center')
thirddan1 = Button(tab1, text="3rd Dan - Generate", command = thirddan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
thirddan1.place(relx=0.65, rely=0.90, anchor='center')
thirddan2 = Button(tab1, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
thirddan2.place(relx=0.65, rely=0.95, anchor='center')
fourthdan1 = Button(tab1, text="4th-6th Dan - Generate", command = fourthdan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
fourthdan1.place(relx=0.95, rely=0.90, anchor='center')
fourthdan2 = Button(tab1, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
fourthdan2.place(relx=0.95, rely=0.95, anchor='center')
patternreset = Button(tab1, text="Reset", command = pattern_reset, width=10, height=1, fg='white', bg='black', font="Verdana 8")
patternreset.place(relx=0.5, rely=0.01, anchor='center')


##
## TAB 2
##


tab2.grid_columnconfigure(1,weight=1)
tab2.grid_columnconfigure(2,weight=1)
tab2.grid_columnconfigure(3,weight=1)
tab2.grid_columnconfigure(4,weight=1)
tab2.grid_columnconfigure(5,weight=1)
tab2.grid_rowconfigure(0,weight=1)
tab2.grid_rowconfigure(1,weight=1)
tab2.grid_rowconfigure(2,weight=1)
tab2.grid_rowconfigure(3,weight=1)
tab2.grid_rowconfigure(4,weight=1)
tab2.grid_rowconfigure(5,weight=1)
tab2.grid_rowconfigure(6,weight=1)
tab2.grid_rowconfigure(7,weight=1)
tab2.grid_rowconfigure(8,weight=1)

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
def warn_red_inc():
    global red_warnings
    red_warnings += 1
    label_red_warnings.config(text=red_warnings)
def warn_red_dec():
    global red_warnings
    red_warnings -= 1
    label_red_warnings.config(text=red_warnings)
def warn_blue_inc():
    global blue_warnings
    blue_warnings += 1
    label_blue_warnings.config(text=blue_warnings)
def warn_blue_dec():
    global blue_warnings
    blue_warnings -= 1
    label_blue_warnings.config(text=blue_warnings)
def round_counter_inc():
    global round_counter
    round_counter += 1
    label_round_counter.config(text=round_counter)
def round_counter_dec():
    global round_counter
    round_counter -= 1
    label_round_counter.config(text=round_counter)
def red_foul_inc():
    global red_fouls
    red_fouls += 1
    label_red_fouls .config(text=red_fouls)
def red_foul_dec():
    global red_fouls
    red_fouls -= 1
    label_red_fouls .config(text=red_fouls)
def blue_foul_inc():
    global blue_fouls
    blue_fouls += 1
    label_blue_fouls .config(text=blue_fouls)
def blue_foul_dec():
    global blue_fouls
    blue_fouls -= 1
    label_blue_fouls .config(text=blue_fouls)
def reset_all():
    global red_warnings, blue_warnings, round_counter, red_fouls, blue_fouls, time_label
    red_warnings = 0
    blue_warnings = 0
    round_counter = 0
    red_fouls = 0
    blue_fouls = 0
    label_red_warnings.config(text=red_warnings)
    label_blue_warnings.config(text=blue_warnings)
    label_round_counter.config(text=round_counter)
    label_red_fouls.config(text=red_fouls)
    label_blue_fouls.config(text=blue_fouls)
    Stop()
    Reset(time_label)

time_label = Label(tab2, text="Ready", bg='black', fg="white", font="Verdana 130 bold")
start = Button(tab2, text='Start Time', font="Verdana 10 bold", width=10, height=2, command=lambda: Start(time_label))
stop = Button(tab2, text='Stop Time', font="Verdana 10 bold", width=10, height=2, state='disabled', command=Stop)
reset = Button(tab2, text='Reset Time', font="Verdana 10 bold", width=10, height=2, state='disabled', command=lambda: Reset(time_label))

label_red_warnings = Label(tab2, text=red_warnings, font='Verdana 200 bold', bg='black', fg='white')
label_red_fouls = Label(tab2, text=red_fouls, font='Verdana 150 bold', bg='black', fg='white')
label_blue_warnings = Label(tab2, text=blue_warnings, font='Verdana 200 bold', bg='black', fg='white')
label_blue_fouls = Label(tab2, text=blue_fouls, font='Verdana 150 bold', bg='black', fg='white')
label_round_counter = Label(tab2, text=round_counter, font='Verdana 100 bold', bg='black', fg='white')
rw = Label(tab2, text="Warnings", font='Verdana 10 bold', bg='black', fg='white')
bw = Label(tab2, text="Warnings", font='Verdana 10 bold', bg='black', fg='white')
rf = Label(tab2, text="Fouls", font='Verdana 10 bold', bg='black', fg='white')
bf = Label(tab2, text="Fouls", font='Verdana 10 bold', bg='black', fg='white')
round = Label(tab2, text="Round", font='Verdana 10 bold', bg='black', fg='white')

redwarninc = Button(tab2, text="redwarning+", font='Verdana 5 bold', command=warn_red_inc, width=15, height=4)
redwarndec = Button(tab2, text="redwarning-", font='Verdana 5 bold', command=warn_red_dec, width=15, height=4)
redfoulinc = Button(tab2, text="redfoul+", font='Verdana 5 bold', command=red_foul_inc, width=15, height=4)
redfouldec = Button(tab2, text="redfoul-", font='Verdana 5 bold', command=red_foul_dec, width=15, height=4)
bluewarninc = Button(tab2, text="bluewarning+", font='Verdana 5 bold', command=warn_blue_inc, width=15, height=4)
bluewarndec = Button(tab2, text="bluewarning-", font='Verdana 5 bold', command=warn_blue_dec, width=15, height=4)
bluefoulinc = Button(tab2, text="bluefoul+", font='Verdana 5 bold', command=blue_foul_inc, width=15, height=4)
bluefouldec = Button(tab2, text="bluefoul-", font='Verdana 5 bold', command=blue_foul_dec, width=15, height=4)
roundcounterinc = Button(tab2, text="round+", font='Verdana 5 bold', command=round_counter_inc, width=15, height=4)
roundcounterdec = Button(tab2, text="round-", font='Verdana 5 bold', command=round_counter_dec, width=15, height=4)
reset_all = Button(tab2, text='Reset All', command=reset_all, width=15)

time_label.place(relx=0.5, rely=0.1, anchor='center')
start.place(relx=0.5, rely=0.75, anchor='center')
stop.place(relx=0.5, rely=0.85, anchor='center')
reset.place(relx=0.5, rely=0.94, anchor='center')
reset_all.place(relx=0.5, rely=0.98, anchor='center')

label_red_warnings.place(relx=0.305, rely=0.5105, anchor='center')
label_red_fouls.place(relx=0.095, rely=0.5105, anchor='center')
label_blue_warnings.place(relx=0.695, rely=0.5105, anchor='center')
label_blue_fouls.place(relx=0.905, rely=0.5105, anchor='center')
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

def counter_label3(label3):
    def count3():
        if running3:
            global counter3
            tt = datetime.fromtimestamp(counter3)
            string3 = tt.strftime("%M:%S")
            display = string3
            label3.config(text=display)
            label3.after(1000, count3)
            counter3 += 1
    count3()
def Start3(label3):
    global running3
    running3 = True
    counter_label3(label3)
    start3['state'] = 'disabled'
    stop3['state'] = 'normal'
    reset3['state'] = 'normal'
def Stop3():
    global running3
    start3['state'] = 'normal'
    stop3['state'] = 'disabled'
    reset3['state'] = 'normal'
    running3 = False
def Reset3(label3):
    global counter3
    counter3 = 0
    if running3 == False:
        reset3['state'] = 'disabled'
        label3['text'] = 'Ready'
    else:
        label3['text'] = 'Starting...'
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
    global red_score, blue_score, tie_score, time_label3
    red_score = 0
    blue_score = 0
    tie_score = 0
    label_red_score.config(text=red_score)
    label_blue_score.config(text=blue_score)
    label_tie_score.config(text=tie_score)
    Stop3()
    Reset3(time_label3)

time_label3 = Label(tab3, text="Ready", bg='black', fg="white", font="Verdana 150 bold")
start3 = Button(tab3, text='Start Time', font="Verdana 10 bold", width=10, height=2, command=lambda: Start3(time_label3))
stop3 = Button(tab3, text='Stop Time', font="Verdana 10 bold", width=10, height=2, state='disabled', command=Stop3)
reset3 = Button(tab3, text='Reset Time', font="Verdana 10 bold", width=10, height=2, state='disabled', command=lambda: Reset3(time_label3))

label_red_score = Label(tab3, text=red_score, font='Verdana 250 bold', bg='black', fg='white')
label_blue_score = Label(tab3, text=blue_score, font='Verdana 250 bold', bg='black', fg='white')
label_tie_score = Label(tab3, text=tie_score, font='Verdana 160 bold', bg='black', fg='white')
redscoreinc = Button(tab3, text="+1 point", font='Verdana 10 bold', command=score_red_inc, width=7, height=1)
redscoredec = Button(tab3, text="-1 point", font='Verdana 10 bold', command=score_red_dec, width=7, height=1)
bluescoreinc = Button(tab3, text="+1 point", font='Verdana 10 bold', command=score_blue_inc, width=7, height=1)
bluescoredec = Button(tab3, text="-1 point", font='Verdana 10 bold', command=score_blue_dec, width=7, height=1)
tiescoreinc = Button(tab3, text="+1 point", font='Verdana 10 bold', command=score_tie_inc, width=7, height=1)
tiescoredec = Button(tab3, text="-1 point", font='Verdana 10 bold', command=score_tie_dec, width=7, height=1)
reset_all = Button(tab3, text='Reset All', command=reset_all, width=15)


time_label3.place(relx=0.5, rely=0.1, anchor='center')
start3.place(relx=0.5, rely=0.75, anchor='center')
stop3.place(relx=0.5, rely=0.85, anchor='center')
reset3.place(relx=0.5, rely=0.94, anchor='center')
reset_all.place(relx=0.5, rely=0.98, anchor='center')

label_red_score.place(relx=0.18, rely=0.496, anchor='center')
label_blue_score.place(relx=0.82, rely=0.496, anchor='center')
label_tie_score.place(relx=0.5, rely=0.496, anchor='center')

redscoreinc.place(relx=0.18, rely=0.283, anchor='center')
redscoredec.place(relx=0.18, rely=0.712, anchor='center')
bluescoreinc.place(relx=0.82, rely=0.283, anchor='center')
bluescoredec.place(relx=0.82, rely=0.712, anchor='center')
tiescoreinc.place(relx=0.5, rely=0.353, anchor='center')
tiescoredec.place(relx=0.5, rely=0.64, anchor='center')


##
## TAB 4
##


tab4.grid_columnconfigure(1,weight=1)
tab4.grid_columnconfigure(2,weight=1)
tab4.grid_columnconfigure(3,weight=1)
tab4.grid_columnconfigure(4,weight=1)
tab4.grid_columnconfigure(5,weight=1)
tab4.grid_rowconfigure(0,weight=1)
tab4.grid_rowconfigure(1,weight=1)
tab4.grid_rowconfigure(2,weight=1)
tab4.grid_rowconfigure(3,weight=1)
tab4.grid_rowconfigure(4,weight=1)
tab4.grid_rowconfigure(5,weight=1)
tab4.grid_rowconfigure(6,weight=1)
tab4.grid_rowconfigure(7,weight=1)
tab4.grid_rowconfigure(8,weight=1)

def counter_label4(label4):
    def count4():
        if running4:
            global counter4
            tt4 = datetime.fromtimestamp(counter4)
            string4 = tt4.strftime("%M:%S")
            display4 = string4
            label4.config(text=display4)
            label4.after(1000, count4)
            counter4 += 1
    count4()
def Start4(label4):
    global running4
    running4 = True
    counter_label4(label4)
    start4['state'] = 'disabled'
    stop4['state'] = 'normal'
    reset4['state'] = 'normal'
def Stop4():
    global running4
    start4['state'] = 'normal'
    stop4['state'] = 'disabled'
    reset4['state'] = 'normal'
    running4 = False
def Reset4(label4):
    global counter4
    counter4 = 0
    if running4 == False:
        reset4['state'] = 'disabled'
        label4['text'] = 'Ready'
    else:
        label4['text'] = 'Starting...'
def score_red_inc4():
    global red_score4
    red_score4 += 1
    label_red_score4.config(text=red_score4)
def score_red_dec4():
    global red_score4
    red_score4 -= 1
    label_red_score4.config(text=red_score4)
def score_blue_inc4():
    global blue_score4
    blue_score4 += 1
    label_blue_score4.config(text=blue_score4)
def score_blue_dec4():
    global blue_score4
    blue_score4 -= 1
    label_blue_score4.config(text=blue_score4)
def reset_all4():
    global red_score4, blue_score4, time_label4
    red_score4 = 0
    blue_score4 = 0
    label_red_score4.config(text=red_score4)
    label_blue_score4.config(text=blue_score4)
    Stop4()
    Reset4(time_label4)

time_label4 = Label(tab4, text="Ready", bg='black', fg="white", font="Verdana 150 bold")
start4 = Button(tab4, text='Start Time', font="Verdana 10 bold", width=10, height=2, command=lambda: Start4(time_label4))
stop4 = Button(tab4, text='Stop Time', font="Verdana 10 bold", width=10, height=2, state='disabled', command=Stop4)
reset4 = Button(tab4, text='Reset Time', font="Verdana 10 bold", width=10, height=2, state='disabled', command=lambda: Reset4(time_label4))

label_red_score4 = Label(tab4, text=red_score4, font='Verdana 250 bold', bg='black', fg='white')
label_blue_score4 = Label(tab4, text=blue_score4, font='Verdana 250 bold', bg='black', fg='white')
redscoreinc4 = Button(tab4, text="+1 point", font='Verdana 10 bold', command=score_red_inc4, width=7, height=1)
redscoredec4 = Button(tab4, text="-1 point", font='Verdana 10 bold', command=score_red_dec4, width=7, height=1)
bluescoreinc4 = Button(tab4, text="+1 point", font='Verdana 10 bold', command=score_blue_inc4, width=7, height=1)
bluescoredec4 = Button(tab4, text="-1 point", font='Verdana 10 bold', command=score_blue_dec4, width=7, height=1)
reset_all4 = Button(tab4, text='Reset All', command=reset_all4, width=15)


time_label4.place(relx=0.5, rely=0.1, anchor='center')
start4.place(relx=0.5, rely=0.75, anchor='center')
stop4.place(relx=0.5, rely=0.85, anchor='center')
reset4.place(relx=0.5, rely=0.94, anchor='center')
reset_all4.place(relx=0.5, rely=0.98, anchor='center')

label_red_score4.place(relx=0.18, rely=0.496, anchor='center')
label_blue_score4.place(relx=0.82, rely=0.496, anchor='center')

redscoreinc4.place(relx=0.18, rely=0.283, anchor='center')
redscoredec4.place(relx=0.18, rely=0.712, anchor='center')
bluescoreinc4.place(relx=0.82, rely=0.283, anchor='center')
bluescoredec4.place(relx=0.82, rely=0.712, anchor='center')


gui.mainloop()