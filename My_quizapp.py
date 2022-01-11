from tkinter import *
from tkinter import messagebox as mb
import json
import random

root = Tk()
root.geometry("1100x700")
root.title("Quiz")
with open('quiz1.json') as f:
    obj = json.load(f)
q = (obj['ques1'])
options1 = (obj['options1'])
a = (obj['ans'])
z = zip(q,options1,a)
l = list(z)
random.shuffle(l)
q,options1,a=zip(*l)

random.shuffle(options1[0])
random.shuffle(options1[1])
random.shuffle(options1[2])
random.shuffle(options1[3])

class Quiz:
    def __init__(self):
        self.qn = 0
        self.qno = 1
        self.quest = StringVar()
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.Checkbuttons()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Quiz in Python Programming", width=110, bg="blue", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        self.quest.set(str(self.qno)+". "+q[qn])
        qn = Label(root, textvariable = self.quest, width=130, font=("times", 16, "bold"), anchor="w")
        qn.place(x=100, y=100)
        return qn
    
    def Checkbuttons(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Checkbutton(root, text=" ", variable=self.opt_selected, onvalue=val + 1, offvalue= 0, font=("times", 14))
            btn2 = Checkbutton(root, text=" ", variable=self.opt_selected, onvalue=val + 1, offvalue= 0, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options1[qn]:
              self.opts[val]['text'] = op
              val += 1

    def buttons(self):
        nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.place(x=380,y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
             return True
        
    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        self.qno += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.quest.set(str(self.qno)+". "+q[self.qn])
            self.display_options(self.qn)      
        

    def display_result(self):
        top = Toplevel()
        top.geometry("1100x700")
        top.title('My Second Windows')
        lbl = Lable1(top, score = int(self.correct / len(q) * 100)).pack()

        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

       

quiz1=Quiz()
root.mainloop()
