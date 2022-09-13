from tkinter import *
from tkcalendar import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sys
from database import DataBase

pink = [255, 192, 203]  # สีปุ่มvisitpage1
deeppink = [255, 105, 180]  # สีปุ่มvisitpage2
lavender = [230, 230, 250]
peachpuff = [255, 218, 185]
lightsalmon = [255, 160, 122]

done_task = []
all_task = []
db = DataBase("users.txt")


class BasePage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "To do list", )
        container = tk.Frame(self)
        self.geometry("500x500")
        container.pack(side="top", fill="both", expand=True, )
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, Mylist, Graph, LoginPage, RegPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#574361")
        label = tk.Label(self, text="TO DAY'S\nTO-DO LIST",
                         font=("FC Palette", 50),
                         height=4, width=15,
                         anchor=N,bg="#574361",fg="white")
        label.place(y=70)
        button = tk.Button(self, text="Log in", relief="raised",
                           font=('Montserrat Alternates', 12),
                           bg="#9fd079",fg="white",
                           command=lambda: controller.show_frame(LoginPage))
        button.place(x=220,y=300)
        btn2 = tk.Button(self, text="Register",
                         relief="raised",
                         bg="white",
                         font=('Montserrat Alternates', 12),
                         command=lambda: controller.show_frame(RegPage))
        btn2.place(x=210,y=350)
        btn3 = tk.Button(self, text="Quit",
                         relief="raised",
                         bg="white",
                         font=('Montserrat Alternates', 10),
                         command=sys.exit)
        btn3.place(x=420,y=450)


class RegPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.username = StringVar()
        self.password = StringVar()
        self.confirmpassword = StringVar()

        frame = tk.Frame(self, bg="#967da1")
        frame.pack(side="bottom", fill="both", expand="True")

        lb1 = tk.Label(frame, text="Registration form",
                       width=20,
                       font=("Montserrat Alternates", 18),
                       bg="#967da1",fg="white")
        lb1.place(x=100, y=53)
        lb2 = tk.Label(frame, text="username", width=20,
                       font=("Montserrat Alternates", 11),
                       bg="#967da1",fg="white")
        lb2.place(x=70, y=130)
        self.usernamee = tk.Entry(frame)
        self.usernamee.place(x=240, y=130)
        lb3 = tk.Label(frame, text="Password", width=20,
                       font=("Montserrat Alternates", 11),
                       bg="#967da1",fg="white")
        lb3.place(x=70, y=180)
        self.passworden = tk.Entry(frame)
        self.passworden.place(x=240, y=180)
        lb4 = tk.Label(frame, text="Confirm Password", width=20,
                       font=("Montserrat Alternates", 11),
                       bg="#967da1",fg="white")
        lb4.place(x=50, y=230)
        self.conpassen = tk.Entry(frame)
        self.conpassen.place(x=240, y=230)
        bt1 = tk.Button(frame, text="Submit", width=7, command=self.submit,
                        font=('Montserrat Alternates', 10),
                        bg="white")
        bt1.place(x=220, y=280)
        bt2 = tk.Button(frame, text="Back",
                        font=('Montserrat Alternates', 10),
                        bg="white",
                        command=lambda: controller.show_frame(StartPage))
        bt2.place(x=50, y=330)

    def submit(self):
        self.username = self.usernamee.get()
        self.password = self.passworden.get()
        self.confirmpassword = self.conpassen.get()

        if self.username != "" and self.password != "" and self.confirmpassword != "":
            if self.password == self.confirmpassword:
                db.add_user(self.username, self.password, self.confirmpassword)
            else:
                self.checkpassword()

        self.reset()

    def checkpassword(self):
        if self.password != self.confirmpassword:
            tk.messagebox.showerror(title="Invalid Error", message="Confirm Password Not Math")

    def reset(self):
        self.usernamee.delete(0, END)
        self.passworden.delete(0, END)
        self.conpassen.delete(0, END)


class LoginPage(RegPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        frame = tk.Frame(self, bg="#967da1")
        frame.pack(side="bottom", fill="both", expand="True")
        lb1 = tk.Label(frame, text="Login", width=15,
                       font=("Montserrat Alternates", 18),
                       bg="#967da1",fg="white")
        lb1.place(x=140, y=53)
        lb2 = tk.Label(frame, text="username", width=20,
                       font=("Montserrat Alternates", 11),
                       bg="#967da1",fg="white")
        lb2.place(x=70, y=130)
        self.user = tk.Entry(frame)
        self.user.place(x=240, y=130)
        lb3 = tk.Label(frame, text="Password", width=20,
                       font=("Montserrat Alternates", 11),
                       bg="#967da1",fg="white")
        lb3.place(x=70, y=180)
        self.passw = tk.Entry(frame)
        self.passw.place(x=240, y=180)
        bt1 = tk.Button(frame, text="Login", width=10,
                        command=self.login,
                        font=('Montserrat Alternates', 10),
                        bg="white")
        bt1.place(x=200, y=280)
        bt2 = tk.Button(frame, text="Back",
                        font=('Montserrat Alternates', 10),
                        bg="white",
                        command=lambda: controller.show_frame(StartPage))
        bt2.place(x=40, y=330)


    def login(self):
        self.username = self.user.get()
        self.password = self.passw.get()
        if db.validate(self.username, self.password):
            self.controller.show_frame(PageOne)
        else:
            tk.messagebox.showerror(title="Invalid Error", message="Invalid username or password")

        self.reset()

    def reset(self):
        self.user.delete(0, END)
        self.passw.delete(0, END)



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#f0f0f0")
        Label1 = tk.Label(self, text="Calendar",width=10,
                          font=("Montserrat Alternates", 18),
                          fg="#967da1")
        Label1.pack(padx=10, pady=10)

        self.cale = Calendar(self, selectmode="day", year=2021, month=1)
        self.cale.configure(background="#f0f0f0", bordercolor="black", headersbackground="#f0f0f0",
                            normalbackground="white", weekendbackground="white", foreground="black",
                            headersforeground="black", othermonthbackground="white",
                            othermonthforeground="white", othermonthweforeground="white"
                            ,othermonthwebackground="white", font=('Montserrat Alternates', 10))
        self.cale.pack()
        self.cale.place(height=350, width=350, x=60, y=60)
        btn3 = tk.Button(self, text="Get Date"
                         ,font=('Montserrat Alternates', 10),
                         bg="#967da1",fg="white"
                         ,command=self.PickerDate)
        btn3.place(y=450, x=210)

    def PickerDate(self):
        Date = self.cale.get_date()
        if Date != "":
            self.controller.show_frame(Mylist)
        else:
            tk.messagebox.showwarning(title="Warning!", message="You must select a Date")


class Mylist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frame = tk.Frame(self, bg="#967da1")
        frame.pack(side="bottom", fill="both", expand="True")

        list_frame = tk.Frame(frame, bg="#967da1")
        list_frame.pack(side='top', fill="both", expand="True")

        label = tk.Label(list_frame,
                         text="My list",
                         font=("Montserrat Alternates", 15),
                         bg="#967da1", fg="white")
        label.pack(side="top", pady=10)

        my_font = Font(family="Montserrat Alternates",
                       size=13)

        self.my_list = Listbox(list_frame, font=my_font,
                               width=30, height=10,
                               bg="#967da1", fg="black",
                               bd=0, highlightthickness=0,
                               selectbackground="#a6a6a6",
                               activestyle=None)
        self.my_list.pack(side=LEFT, fill="both", pady=20)
        self.my_list.place(x=50, y=45)

        self.stuff = []
        for item in self.stuff:
            self.my_list.insert(END, item)

        my_scrollar = Scrollbar(list_frame)
        my_scrollar.pack(padx=50, side=RIGHT, fill=BOTH)

        self.my_list.config(yscrollcommand=my_scrollar.set)
        my_scrollar.config(command=self.my_list.yview)

        self.my_entry = tk.Entry(frame, width=30,
                                 font=('Montserrat Alternates', 10))
        self.my_entry.pack(side="top")

        button_frame = tk.Frame(frame, bg="#967da1")
        button_frame.pack(pady=5, side='top')

        button_page = tk.Frame(frame, bg="#967da1")
        button_page.pack(pady=10, padx=20, side="right")

        done_button = Button(button_frame, text="Done!",
                             font=('Montserrat Alternates', 10),
                             command=self.done_item,bg="white")
        add_button = Button(button_frame, text="Add",
                            font=('Montserrat Alternates', 10),
                            command=self.add_item,bg="white")
        calendar_button = Button(frame, text="Calendar",
                                 font=('Montserrat Alternates', 10),
                                 command=lambda: controller.show_frame(PageOne),
                                 bg="white")
        graph_button = Button(frame, text="Graph",
                              font=('Montserrat Alternates', 10),
                              command=self.check_item,
                              bg="white")
        calendar_button.place(x=30, y=450)
        graph_button.place(x=420, y=450)
        add_button.grid(row=0, column=0, padx=10)
        done_button.grid(row=0, column=1)

    def done_item(self):
        global done_task
        global task_index
        global done

        try:
            task_index = self.my_list.curselection()
            self.my_list.itemconfig(task_index,
                                    fg="#dedede", )
        except:
            tk.messagebox.showwarning(title="Warning!", message="You must select a task")

        done = self.my_list.get(ANCHOR)
        if done not in done_task:
            done_task.append(done)
        else:
            tk.messagebox.showwarning(title="Warning!", message="Task in Completed")
            done_task = list(dict.fromkeys(done_task))

        for task in done_task:
            if task == "":
                done_task.remove(task)

        return done_task

    def add_item(self):
        global all_task
        task = self.my_entry.get()
        if task != "":
            self.my_list.insert(END, task)
            self.my_entry.delete(0, END)
            if task not in all_task:
                all_task.append(task)
        else:
            tk.messagebox.showwarning(title="Warning!", message="You must enter a task")

        return all_task

    def check_item(self):
        if all_task == []:
            tk.messagebox.showwarning(title="Warning!", message="You must enter a task")
        else:
            self.controller.show_frame(Graph)



class Graph(Mylist):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = tk.Frame(self, bg="white")
        frame.pack(side="bottom", fill="both", expand="True")
        button = tk.Button(frame, text='Create Charts',
                           command=self.create_charts, bg='#574361', fg="white",
                           font=('Montserrat Alternates', 10))
        button.pack(side='top', pady=50)

        button1 = Button(frame, text="Back",
                         font=('Montserrat Alternates', 10),
                         command=lambda: controller.show_frame(Mylist))
        button1.place(x=50, y=430)
        button2 = Button(frame, text="Back to start",
                         font=('Montserrat Alternates', 10),
                         command=lambda: controller.show_frame(StartPage))
        button2.place(x=350, y=430)

    def create_charts(self):
        global x1
        global x2
        global pie2

        x1 = float(len(done_task))
        x2 = float(len(all_task) - len(done_task))

        figure = Figure(figsize=(4, 3), dpi=100)
        subplot = figure.add_subplot(111)
        labels = 'Completed', 'On Going'
        pieSizes = [float(x1), float(x2)]
        my_colors = ['#ff844B', '#9fd079']
        explode = (0, 0.1)
        subplot.pie(pieSizes, colors=my_colors, explode=explode,
                         labels=labels, autopct='%1.1f%%', shadow=True,
                         startangle=90)
        subplot.axis('equal')
        pie = FigureCanvasTkAgg(figure, self)
        pie.get_tk_widget().place(x=50, y=100)






app = BasePage()
app.mainloop()

