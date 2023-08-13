import tkinter as tk
import tkinter.ttk as win
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("280x300")
        self.maxsize(height=300,width=280)
        # -------------labels-------------------
        name_title=tk.Label(text="CalcMaster",font=("Helvetica", 20))
        name_title.place(x=70,y=1)
        # -----------------Buttons---------------------
        one_btn=win.Button(text='1',command=lambda text='1':self.on_button_click(text))
        one_btn.place(x=20,y=90)

        two_btn = win.Button(text='2',command=lambda text='2':self.on_button_click(text))
        two_btn.place(x=100, y=90)

        three_btn = win.Button(text='3',command=lambda text='3':self.on_button_click(text))
        three_btn.place(x=180, y=90)

        four_btn = win.Button(text='4',command=lambda text='4':self.on_button_click(text))
        four_btn.place(x=20, y=120)

        five_btn = win.Button(text='5',command=lambda text='5':self.on_button_click(text))
        five_btn.place(x=100, y=120)

        six_btn = win.Button(text='6',command=lambda text='6':self.on_button_click(text))
        six_btn.place(x=180, y=120)

        seven_btn = win.Button(text='7',command=lambda text='7':self.on_button_click(text))
        seven_btn.place(x=20, y=150)

        eight_btn = win.Button(text='8',command=lambda text='8':self.on_button_click(text))
        eight_btn.place(x=100, y=150)

        nine_btn = win.Button(text='9',command=lambda text='9':self.on_button_click(text))
        nine_btn.place(x=180, y=150)

        zero_btn = win.Button(text='0',command=lambda text='0':self.on_button_click(text))
        zero_btn.place(x=20, y=180)

        add_btn = win.Button(text="+",command=lambda text='+':self.on_button_click(text))
        add_btn.place(x=100, y=180)

        minus_btn = win.Button(text="-",command=lambda text='-':self.on_button_click(text))
        minus_btn.place(x=180, y=180)

        multiply_btn = win.Button(text="*",command=lambda text='*':self.on_button_click(text))
        multiply_btn.place(x=20, y=210)

        divide_btn = win.Button(text="/",command=lambda text='/':self.on_button_click(text))
        divide_btn.place(x=100, y=210)

        remainder_btn = win.Button(text="%",command=lambda text='%':self.on_button_click(text))
        remainder_btn.place(x=180, y=210)

        equal_btn = win.Button(text="=",command=lambda text='=':self.on_button_click(text))
        equal_btn.place(x=20, y=240)

        clear_btn = win.Button(text="Clear", command=lambda text='Clear': self.on_button_click(text))
        clear_btn.place(x=100, y=240)
        # ------------Buttons_End---------------
        # ---------------TextBox--------------
        self.entry_var=tk.StringVar()
        self.entry_var.set("")
        text_box=win.Entry(width=26,font=('bold',12),textvariable=self.entry_var)
        text_box.place(x=18,y=50)


    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.entry_var.get())
                print(result)
                self.entry_var.set(result)
            except:
                self.entry_var.set("Syntax Error")
        elif text == 'Clear':
            self.entry_var.set("")
        else:
            self.entry_var.set(self.entry_var.get() + text)
app=Calculator()
app.mainloop()
