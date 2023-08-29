import tkinter as tk
import tkinter.ttk as win
import tkinter.filedialog as fd
from tkinter import PhotoImage
from PIL import Image, ImageTk
from pygame import mixer
from mutagen import File
import io
from tkinter import messagebox as mb
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MusicPlayer")
        self.geometry("490x250")
        self.maxsize(height=250,width=490)
        # -----------MainImage
        logo_img=Image.open("Images/Logo.png")
        logo_img_photo=ImageTk.PhotoImage(logo_img)
        logo_img_lbl=win.Label(image=logo_img_photo)
        logo_img_lbl.photo=logo_img_photo
        logo_img_lbl.place(x=12,y=12)
        # -------------------------
        # Load images
        self.play_btn_image = tk.PhotoImage(file="Images/PlayBtn.png")
        self.pause_btn_image = tk.PhotoImage(file="Images/PauseBtn.png")

        # Btn-----------------
        self.play_btn_image=tk.PhotoImage(file="Images/PlayBtn.png")
        self.play_Pause_btn=win.Button(image=self.play_btn_image,style="NoBorder.TButton",command=self.Play_Audio_and_Pause_Audio)
        self.play_Pause_btn.image=self.play_btn_image
        self.play_Pause_btn.place(x=310,y=200)

        # Initial State
        self.playing=False

        # Custom Style for Progress Bar
        style = win.Style()
        style.theme_use('default')  # Use the default theme as a base
        style.configure("Custom.Horizontal.TProgressbar",
                        troughcolor='gray',  # Background color
                        background='blue',  # Progress color
                        lightcolor='blue',  # Gradient light color
                        darkcolor='blue'  # Gradient dark color
                        )

    #     Add Progress_Bar
        self.progress_bar=win.Progressbar(self,orient='horizontal', mode='determinate',style="Custom.Horizontal.TProgressbar",length=220)
        self.progress_bar.place(x=240,y=175)


        self.thumbnail_label = tk.Label(self)
        self.thumbnail_label.pack(pady=10)
        # -------------------Volume Slider
        self.volume_slider=win.Scale(self,orient='horizontal',command=self.update_volume)
        self.volume_slider.place(x=360,y=210)
        self.volume_slider.set(10)
        # -------------------------------
        # file_menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # create the file_menu
        file_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        # add menu items to the File menu
        file_menu.add_command(label='Load File',command=self.loadSong)
        file_menu.add_separator()

        # add Exit menu item
        file_menu.add_command(
            label='Exit',
            command=self.destroy
        )

        # add the File menu to the menubar
        menubar.add_cascade(
            label="File",
            menu=file_menu
        )

        default_thumbnail=ImageTk.PhotoImage(Image.open('Images/Default.png'))
        lbl=win.Label(self,image=default_thumbnail,borderwidth=0)
        lbl.place(x=270,y=12)

    def Play_Audio_and_Pause_Audio(self):
        try:
            if self.playing:
                self.play_Pause_btn.config(image=self.play_btn_image)
                mixer.music.pause()
                self.thumbnail_label.pack_forget()

            else:
                self.play_Pause_btn.config(image=self.pause_btn_image)
                mixer.init()
                self.update_volume(50 / 100)
                self.audiofile=self.open_song
                mixer.music.load(self.audiofile)
                mixer.music.play()
                self.thumbnail_image = self.get_thumbnail()
                if self.thumbnail_image:
                    self.thumbnail_label = tk.Label(self, image=self.thumbnail_image)
                    self.thumbnail_label.place(x=270,y=20)
                # self.thumbnail_image = self.get_thumbnail()

                self.update_progress()
            self.playing=not self.playing
        except(AttributeError):
            self.play_Pause_btn.config(image=self.play_btn_image)
            mb.showinfo("Load an Audio File","Please Load an Audio File from File Menu")


    def update_progress(self):
        if mixer.music.get_busy():
            current_position=mixer.music.get_pos() / 1000
            self.progress_bar['value']=current_position
            self.after(100,self.update_progress)

    def change_position(self,event):
        x=event.x
        width=self.progress_bar.winfo_width()
        position=(x / width) * (mixer.music.get_pos() / 1000)
        mixer.music.set_pos(position/100)

    def get_thumbnail(self):
        audio=File(self.audiofile)
        if 'APIC:' in audio:
            apic=audio.tags['APIC:'].data
            thumbnail_image = Image.open(io.BytesIO(apic))
            thumbnail_image = thumbnail_image.resize((150, 150))
            return ImageTk.PhotoImage(thumbnail_image)
        else:
            return None

    def update_volume(self,volume):
        mixer.music.set_volume(float(volume))

    def loadSong(self):
        self.open_song=fd.askopenfilename(
            title=("Select an Audio File")
        )
        if self.open_song=="":
            mb.showinfo("Load Audio File","Audio File is not Loaded")
        # print(open_song)

if __name__ == '__main__':
    win=MainWindow()
    win.mainloop()
