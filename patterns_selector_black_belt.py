import random
import tkinter as tk

window = tk.Tk()
window.minsize(width=720, height=360)

patterns_list = [
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
            "Moon-Moo"] #20
rank_list = [
            "1st", #0
            "2nd", #1
            "3rd", #2
            "4th"] #3

pattern_string = "          "
pattern_label = tk.Label(window, text=pattern_string, font = "Verdana 100 bold", bg = "white")
pattern_label.place(relx=0.5, rely=0.2, anchor='center')

class blackbelt_pattern_select():
    def firstdan1():
        global pattern_string
        num = random.randint(0,3)
    def firstdan2():
        print("second pattern")
    def seconddan1():
        global pattern_string
        num = random.randint(0,3)
    def seconddan2():
        print("second pattern")
    def thirddan1():
        global pattern_string
        num = random.randint(0,3)
    def thirddan2():
        print("second pattern")
    def fourthdan1():
        global pattern_string
        num = random.randint(0,3)
    def fourthdan2():
        print("second pattern")
 

#black belt buttons
firstdan1 = tk.Button(window, text="1st Dan - Pattern 1", command = blackbelt_pattern_select.firstdan1, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan1.place(relx=0.05, rely=0.90, anchor='center')
firstdan2 = tk.Button(window, text="1st Dan - Pattern 2", command = blackbelt_pattern_select.firstdan2, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan2.place(relx=0.05, rely=0.95, anchor='center')
# seconddan1 = tk.Button(window, text="2nd Dan - Pattern 1", command = blackbelt_pattern_select.seconddan1, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
# seconddan1.place(relx=0.35, rely=0.90, anchor='center')
# seconddan2 = tk.Button(window, text="2nd Dan - Pattern 2", command = blackbelt_pattern_select.seconddan2, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
# seconddan2.place(relx=0.35, rely=0.95, anchor='center')
# thirddan1 = tk.Button(window, text="3rd Dan - Pattern 1", command = blackbelt_pattern_select.thirddan1, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
# thirddan1.place(relx=0.65, rely=0.90, anchor='center')
# thirddan2 = tk.Button(window, text="3rd Dan - Pattern 2", command = blackbelt_pattern_select.thirddan2, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
# thirddan2.place(relx=0.65, rely=0.95, anchor='center')
# fourthdan1 = tk.Button(window, text="4th-6th Dan - Pattern 1", command = blackbelt_pattern_select.fourthdan1, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
# fourthdan1.place(relx=0.95, rely=0.90, anchor='center')
# fourthdan2 = tk.Button(window, text="4th-6th Dan - Pattern 2", command = blackbelt_pattern_select.fourthdan2, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
# fourthdan2.place(relx=0.95, rely=0.95, anchor='center')



window.mainloop()