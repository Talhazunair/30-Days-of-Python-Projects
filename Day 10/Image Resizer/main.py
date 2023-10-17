import tkinter as tk
import tkinter.ttk as win
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import os
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Resizer")
        self.geometry("400x500")
        self.maxsize(height=500,width=400)

        self.image = Image.open("background.jpg")
        self.background_image = ImageTk.PhotoImage(self.image)
        canvas1 = tk.Canvas(width=400,height=500)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=self.background_image,anchor="nw")

        # ------------lables--------------
        height_lbl=win.Label(text="Height")
        height_lbl.place(x=50,y=400)
        height_lbl.configure(background="#0d0d0d",foreground="white")
        
        width_lbl=win.Label(text="Width")
        width_lbl.place(x=230,y=400)
        width_lbl.configure(background="#282828",foreground="white")
        # -------------Label_End---------
        # --------------Butons---------
        save_btn=win.Button(text="Save",command=self.Resize_Image)
        save_btn.place(x=275,y=440)

        open_btn = win.Button(text="Open",command=self.Open_Image)
        open_btn.place(x=95, y=440)
        # --------------Buttons_End---------
        # --------------Entry_Boxes----------
        self.height_entry=win.Entry(width=10)
        self.height_entry.place(x=100,y=400)

        self.width_entry = win.Entry(width=10)
        self.width_entry.place(x=280, y=400)
        # ---------------------Entry_Boxes End----------

    def Open_Image_func(self):
        filetypes = (('PNG File', '*.png'),('JPG File', '*.jpg'),('JPEG','*.jpeg'))
        self.open_img=fd.askopenfilename(title="Open Image File",filetypes=filetypes)
        return self.open_img
    def Open_Image(self):
        self.x=self.Open_Image_func()
        img=Image.open(self.x)
        img = img.resize((370, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = win.Label(image=img)
        panel.image = img
        panel.place(x=14,y=60)

    def Resize_Image(self):
        if (self.height_entry.get() == "" or  self.width_entry.get() == ""):
            mb.showerror("Field Error", "Please Enter Height and Width")
        my_img=Image.open(self.x)
        my_img=my_img.resize((int(self.height_entry.get()),int(self.width_entry.get())))
        my_img.save(self.Save_Image())

    def Save_Image(self):
        filetypes = (('PNG File', '*.png'), ('JPG File', '*.jpg'), ('JPEG', '*.jpeg'))
        save_img = fd.asksaveasfilename(title="Choose Save Path", filetypes=filetypes)
        return save_img

app=MainWindow()
app.mainloop()