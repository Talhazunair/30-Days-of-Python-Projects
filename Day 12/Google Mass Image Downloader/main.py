import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk as win
from pygoogle_image import image as pi
from PIL import ImageTk, Image
import threading
from tkinter import messagebox as mb
class ImageDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mass Image Downloader")
        self.maxsize(height=400, width=500)
        self.geometry("500x400")
        # self.iconphoto(self.PhotoImage(file="Photos/photo-camera.png"))
        # --------------Main_Background--------------
        self.filename = ImageTk.PhotoImage(file="Photos/Background.jpg")
        self.background_label = win.Label(image=self.filename)
        self.background_label.place(x=-2, y=0)
        # --------------Main_Background_End-------------
        # --------Buttons-------
        download_btn = win.Button(text="Download", command=self.Downloading_in_Background)
        download_btn.place(x=242, y=300)

        save_btn = win.Button(text="Save", command=self.save_Images_to)
        save_btn.place(x=80, y=300)
        # --------Buttons_End---
        # ------------Entry_Points-------------
        self.image_keyword = win.Entry()
        self.image_keyword.place(x=220, y=190)
        self.limit_Entry = win.Entry()
        self.limit_Entry.place(x=220, y=240)

        self.download_progress_bar = win.Progressbar()
        self.download_progress_bar.configure(length=410, mode='determinate')
        self.download_progress_bar.place(x=50, y=350)
        # --------------------------------------------------


    def download_mass_images(self):
        pi.download(keywords=self.image_keyword.get(), limit=int(self.limit_Entry.get()),
                directory=self.save_location + '\\')

    def Downloading_in_Background(self):
        if(self.image_keyword.get() !="" and self.limit_Entry.get() !=""):
            thread = threading.Thread(target=self.download_mass_images)
            self.download_progress_bar.start(4)
            print(self.img_extensions.get())
            thread.start()
            # threading.current_thread()
        else:
            mb.showwarning("Invalid Input", "Please Write Something in Empty Fileds")
            self.download_progress_bar.stop()



    # self.download_progress_bar.start()
    def save_Images_to(self):
        self.save_location = fd.askdirectory()
        print(self.save_location)

    def track_with_Progress_bar(self):
        pass


app = ImageDownloader()
app.mainloop()
