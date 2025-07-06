
from tkinter import *
from tkinter.font import *
from tkinter import messagebox
from tkinter import filedialog
import os
import csv
root = Tk()
root.iconbitmap("C:/Users/gurup/OneDrive/Desktop/quiz_/maghs_icon.ico")
root.title("quiz_writer")
root.geometry("700x500")
root.resizable(False, False)
root.configure(background="#8d99ae")
class c:
    def check(self):
        if self.question.get() and self.option1.get() and self.option2.get() and self.option3.get() and self.option4.get():
            self.con.configure(state=NORMAL,background="#95d5b2",activebackground="#d8f3dc")
        else:
            self.con.configure(state="disabled",background="#ffb3c1")
    conform : Tk
    csv.register_dialect(
        "my",
        delimiter="|",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True
    )
    def file_create(self):
        self.path.insert(0,self.current)
    def conform(self):
        f= open(self.path.get(),"a")
        self.write=csv.writer(f,dialect="my")
        self.conform1.config(state="disabled")
    def get_ans_option(self):
        self.ans=int(self.ans_ch.get())
    def conform_qsans(self):
        self.answer_option={
            0:self.option1.get(),
            1:self.option2.get(),
            2:self.option3.get(),
            3:self.option4.get()
        }
        try :
            self.write.writerow([
                self.question.get(),
                self.answer_option[0],
                self.answer_option[1],
                self.answer_option[2],
                self.answer_option[3],
                self.answer_option[self.ans]
            ])
            self.question.delete(0,END)
            self.option1.delete(0,END)
            self.option2.delete(0, END)
            self.option3.delete(0, END)
            self.option4.delete(0, END)
        except :
            self.msg=messagebox.showerror("Error","conform the path")
    def browse(self):

        file_path = filedialog.asksaveasfilename(
            title="Create CSV File",
            defaultextension=".csv",  # Default extension
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile="untitled.csv"  # Default filename
        )
        self.path.insert(0,END)
    def __init__(self):
        self.ans=0
        self.current = os.getcwd() + "\\" + "untitled.csv"
        self.write : str =""
        self.answer_option : dict ={}
        fnt=Font(size=12,family="JetBrainsMono NF Medium")
        self.frame1=Frame(root,width=100,bg="#8d99ae")
        self.frame1.grid(row=0,column=0)
        Label(self.frame1,text="File Path",font=fnt,bg="#8d99ae").grid(row=0,column=0)
        self.path=Entry(
            self.frame1,
            width=50,
            font=fnt,
            background="#d7e3fc",
            foreground="#006d77",
            selectbackground="#ccff33"
        )
        self.path.grid(row=0,column=1)
        self.file_create()
        Button(self.frame1,text="Browse",font=fnt,command=self.browse).grid(padx=20,row=0,column=3)
        self.frame2 = Frame(root,bg="#8d99ae")
        self.frame2.grid(row=1,column=0)
        self.conform1=Button(
            self.frame2,
            text="conform",
            font=fnt,
            width=8,
            command=self.conform
        )
        c.conform=self.conform1
        self.conform1.pack(pady=20)
        self.frame3=Frame(root,bg="#8d99ae")
        self.frame3.grid(row=2,column=0)
        Label(self.frame3,text="Question",font=fnt,bg="#8d99ae").grid(row=1,column=0)
        self.question=Entry(
            self.frame3,
            width=50,
            font=fnt,
            background="#d7e3fc",
            selectbackground="#ccff33",
            foreground="#006d77"
        )
        self.question.bind("<KeyRelease>", lambda event: self.check())
        self.question.grid(row=1,column=1,columnspan=3)
        self.ans_ch=IntVar()
        self.r1=Radiobutton(
            self.frame3,
            bg="#8d99ae",
            width=10,
            variable=self.ans_ch,
            value=0,
            command=self.get_ans_option
        )
        self.r1.grid(row=3,column=0,pady=20)
        Label(self.frame3,text="Option 1",font=fnt,bg="#8d99ae").grid(row=3,column=1)
        self.option1=Entry(
            self.frame3,
            font=fnt,
            selectbackground="#ccff33",
            background="#d7e3fc",
            foreground="#006d77"
        )
        self.option1.grid(row=3,column=2)
        self.option1.bind("<KeyRelease>", lambda event: self.check())
        self.r2=Radiobutton(
            self.frame3,
            bg="#8d99ae",
            width=10,
            variable=self.ans_ch,
            value=1,
            command=self.get_ans_option
        )
        self.r2.grid(row=4,column=0,pady=20)
        Label(self.frame3,text="Option 2",font=fnt,bg="#8d99ae").grid(row=4,column=1)
        self.option2=Entry(
            self.frame3,
            font=fnt,
            selectbackground="#ccff33",
            background="#d7e3fc",
            foreground="#006d77"
        )
        self.option2.grid(row=4,column=2)
        self.option2.bind("<KeyRelease>", lambda event: self.check())
        self.r3=Radiobutton(
            self.frame3,
            width=6,
            bg="#8d99ae",
            variable=self.ans_ch,
            value=2,
            command=self.get_ans_option
        )
        self.r3.grid(row=5,column=0,pady=20)
        Label(self.frame3,text="Option 3",font=fnt,bg="#8d99ae").grid(row=5,column=1)
        self.option3=Entry(
            self.frame3,
            font=fnt,
            selectbackground="#ccff33",
            background="#d7e3fc",
            foreground="#006d77"
        )
        self.option3.grid(row=5,column=2)
        self.option3.bind("<KeyRelease>", lambda event: self.check())
        self.r4=Radiobutton(
            self.frame3,
            bg="#8d99ae",
            width=10,
            variable=self.ans_ch,
            value=3,
            command=self.get_ans_option
        )
        self.r4.grid(row=6,column=0,pady=20)
        Label(self.frame3,text="Option 4",font=fnt,bg="#8d99ae").grid(row=6,column=1)
        self.option4=Entry(
            self.frame3,
            font=fnt,
            selectbackground="#ccff33",
            background="#d7e3fc",
            foreground="#006d77")
        self.option4.grid(row=6,column=2)
        self.option4.bind("<KeyRelease>", lambda event: self.check())
        self.frame4=Frame(root,bg="#8d99ae")
        self.frame4.grid(row=7,column=0)
        self.con=Button(self.frame4,state="disabled",text="Conform",font=fnt,background="#ffb3c1",command=self.conform_qsans)
        self.con.pack()
c=c()
mainloop()
