import tkinter as tk
import tkinter.ttk as win
import subprocess
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import sys
import pyzipper
import threading
from tqdm import tqdm
class Zipcrack(tk.Tk):

    def __init__(self):
        super().__init__()
        self.maxsize(height=400,width=700)
        self.geometry("700x400")
        self.title("Zip Password Cracker")

        self.bg_img = tk.PhotoImage(file="Background.png")
        self.background_label = win.Label(image=self.bg_img)
        self.background_label.place(x=0, y=0)
        # ------------Buttons------------
        zip_file_path=win.Button(text="Browse",command=self.Path_zip_File)
        zip_file_path.place(x=420,y=198)

        wordlist_path = win.Button(text="Wordlist",command=self.Password_List)
        wordlist_path.place(x=60, y=230)

        crack_btn = win.Button(text="Start",command=threading.Thread(target=self.Crack_the_Password).start)
        crack_btn.place(x=420, y=230)

        # --------------Text_box-----------------
        self.my_string = tk.StringVar()
        self.path_text_box=win.Entry(width=60,textvariable=self.my_string)
        self.path_text_box['state']=("read")
        self.path_text_box.config(foreground="#05a620")
        self.path_text_box.place(x=50,y=200)
        self.password_tests_result=tk.Text(height=19,width=20)
        self.password_tests_result.place(x=520,y=70)
        # -------------------------Labels--------------------------
        self.password_found_lbl=win.Label(text="",font=("bold,30"))
        self.wordlist_loaded_lbl=win.Label(text="",font=("bold,30"))
        self.total_password_lbl=win.Label(text="",font=("bold,30"))
        # ----------------------Progress_bar-------------------------
        self.progresscount=win.Progressbar(orient="horizontal",mode="indeterminate",length=340)
        self.progresscount.place(x=50, y=350)
        # --------mainbg----------------


    def Password_List(self):
        self.password_file = fd.askopenfile(mode='r', filetypes=[('Text File', '*.txt'),])
        for words in self.password_file:
            self.my_list=(words.strip())
            self.password_tests_result.insert(tk.END,self.my_list+"\n")
            self.wordlist_loaded_lbl.configure(foreground="#038c0e",text="Wordlist Loaded Successfully",background="#282727")
            self.wordlist_loaded_lbl.place(x=150, y=230)
            # len(list(open(wordlist, "rb")))
            self.total_password_lbl.config(text=f"Total Password in List : {len(list(words))}",background="#282727",foreground="white")
            self.total_password_lbl.place(x=70, y=270)
            self.update()

    def Crack_the_Password(self):
        self.password_found_lbl.place(x=70, y=310)
        self.word_list_path=(str(self.password_file)[25:-29])
        read_file=open(f"{self.word_list_path}",encoding="utf8")
        for word in read_file:
            self.progresscount.start()
            password = word.rstrip('\n')
            with pyzipper.AESZipFile(self.path, 'r') as zip_file:
                try:
                    zip_file.pwd = password.encode()
                    zip_file.extractall()
                    self.password_found_lbl.config(foreground="#218f3e",text=f"Password Found : { zip_file.pwd}")
                    self.progresscount.stop()
                    sys.exit()
                except RuntimeError:
                    continue
        self.password_found_lbl.config(foreground="#a80311", text="Password Not Found")
        self.progresscount.stop()

    def Path_zip_File(self):
        self.file=fd.askopenfile(mode='r',filetypes=[('Zip File', '*.zip')])
        self.path=(str(self.file)[25:-29])
        print(self.path)
        self.my_string.set(str(self.file)[25:-29])

app=Zipcrack()
app.mainloop()