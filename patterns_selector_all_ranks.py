import random
import tkinter as tk

window = tk.Tk()
window.minsize(width=720, height=360)

patterns_list = ["Chon-Ji", #0
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
            "Moon-Moo"] #20
rank_list = ["whitebelt", #0
            "yellowstripe",#1
            "yellowbelt", #2
            "greenstripe", #3
            "greenbelt", #4
            "bluestripe", #5
            "bluebelt", #6
            "redstripe", #7
            "redbelt", #8
            "blackstripe", #9
            "1st", #10
            "2nd", #11
            "3rd", #12
            "4th"] #13

pattern_string = "Press Button"
pattern_label = tk.Label(window, text=pattern_string, font = "Verdana 100 bold", bg = "white")
pattern_label.place(relx=0.5, rely=0.2, anchor='center')

class colorbelt_pattern_select():
    def yellowstripe():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 0
        rank_index = 1
        if num == 0 or num == 1 :#or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def yellowbelt():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 1
        rank_index = 2
        if num == 0 or num == 1 or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def greenstripe():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 2
        rank_index = 3
        if num == 0 or num == 1 or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def greenbelt():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 3
        rank_index = 4
        if num == 0 or num == 1 or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def bluestripe():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 4
        rank_index = 5
        if num == 0 or num == 1 or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def bluebelt():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 5
        rank_index = 6
        if num == 0 or num == 1 or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def redstripe():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 6
        rank_index = 7
        if num == 0 or num == 1 or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def redbelt():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 7
        rank_index = 8
        if num == 0 or num == 1 or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def blackstripe():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 8
        rank_index = 9
        if num == 0 or num == 1 or num == 2: 
            pattern_string = patterns_list[pattern_index]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
class blackbelt_pattern_select():
    def firstdan():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 11
        rank_index = 10
        if num == 0 or num == 1 or num == 2: 
            temp_num = random.randint(0,2)
            if temp_num == 0:
                pattern_string = patterns_list[9]
            elif temp_num == 1:
                pattern_string = patterns_list[10]
            elif temp_num == 2:
                pattern_string = patterns_list[11]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)   
    def seconddan():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 14
        rank_index = 11
        if num == 0 or num == 1 or num == 2: 
            temp_num = random.randint(0,2)
            if temp_num == 0:
                pattern_string = patterns_list[12]
            elif temp_num == 1:
                pattern_string = patterns_list[13]
            elif temp_num == 2:
                pattern_string = patterns_list[14]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)  
    def thirddan():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 17
        rank_index = 12
        if num == 0 or num == 1 or num == 2: 
            temp_num = random.randint(0,2)
            if temp_num == 0:
                pattern_string = patterns_list[15]
            elif temp_num == 1:
                pattern_string = patterns_list[16]
            elif temp_num == 2:
                pattern_string = patterns_list[17]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)
    def fourthdan():
        global pattern_string
        num = random.randint(0,3)
        pattern_index = 20
        rank_index = 13
        if num == 0 or num == 1 or num == 2: 
            temp_num = random.randint(0,2)
            if temp_num == 0:
                pattern_string = patterns_list[18]
            elif temp_num == 1:
                pattern_string = patterns_list[19]
            elif temp_num == 2:
                pattern_string = patterns_list[20]
        else:
            pattern_string = patterns_list[random.randint(0,pattern_index)]
        pattern_label.config(text=pattern_string)

#color belt buttons
yellowstripe = tk.Button(window, text="Yellow Stripe", command = colorbelt_pattern_select.yellowstripe, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
yellowstripe.place(relx=0.25, rely=0.5, anchor='center')
yellowbelt = tk.Button(window, text="Yellow Belt", command = colorbelt_pattern_select.yellowbelt, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
yellowbelt.place(relx=0.25, rely=0.6, anchor='center')
greenstripe = tk.Button(window, text="Green Stripe", command = colorbelt_pattern_select.greenstripe, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
greenstripe.place(relx=0.25, rely=0.7, anchor='center')

greenbelt = tk.Button(window, text="Green Belt", command = colorbelt_pattern_select.greenbelt, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
greenbelt.place(relx=0.40, rely=0.5, anchor='center')
bluestripe = tk.Button(window, text="Blue Stripe", command = colorbelt_pattern_select.bluestripe, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
bluestripe.place(relx=0.40, rely=0.6, anchor='center')
bluebelt = tk.Button(window, text="Blue Belt", command = colorbelt_pattern_select.bluebelt, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
bluebelt.place(relx=0.40, rely=0.7, anchor='center')

redstripe = tk.Button(window, text="Red Stripe", command = colorbelt_pattern_select.redstripe, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
redstripe.place(relx=0.55, rely=0.5, anchor='center')
redbelt = tk.Button(window, text="Red Belt", command = colorbelt_pattern_select.redbelt, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
redbelt.place(relx=0.55, rely=0.6, anchor='center')
blackstripe = tk.Button(window, text="Black Stripe", command = colorbelt_pattern_select.blackstripe, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
blackstripe.place(relx=0.55, rely=0.7, anchor='center')

#black belt buttons
firstdan = tk.Button(window, text="1st Dan", command = blackbelt_pattern_select.firstdan, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan.place(relx=0.70, rely=0.5, anchor='center')
seconddan = tk.Button(window, text="2nd Dan", command = blackbelt_pattern_select.seconddan, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
seconddan.place(relx=0.70, rely=0.6, anchor='center')
thirddan = tk.Button(window, text="3rd Dan", command = blackbelt_pattern_select.thirddan, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
thirddan.place(relx=0.70, rely=0.7, anchor='center')
fourthdan = tk.Button(window, text="4th-6th Dan", command = blackbelt_pattern_select.fourthdan, width=12, height=2, fg="white", bg = "black", font="Verdana 10 bold")
fourthdan.place(relx=0.70, rely=0.8, anchor='center')



window.mainloop()