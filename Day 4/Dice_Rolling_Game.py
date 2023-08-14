import os
import tkinter as tk
import tkinter.ttk as win
import random
from PIL import Image
from PIL import ImageTk
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Rolling")
        self.geometry("300x300")
        self.maxsize(height=300,width=300)
        # ----------Btn------------
        play_btn=win.Button(text="Play",command=self.show_random_image)
        play_btn.place(x=110,y=220)
        # ----------------------
        # Label
        self.Show_dice=win.Label(text="0")
        self.Show_dice.place(x=75,y=40)
        self.Show_dice.config(text="Dice Roling Game",font=('bold',14))

        # load Images
        self.image_paths = self.load_image_path("Images")  # image_paths is declared here
        self.images = [Image.open(path) for path in self.image_paths]  # path is used here
        self.photo_images = [ImageTk.PhotoImage(image) for image in self.images]

    def load_image_path(self,directory):
        image_paths=[]
        for filename in os.listdir(directory):
            if filename.lower().endswith((".png",".jpg",".jpeg",".gif")):
                image_paths.append(os.path.join(directory,filename))
        return image_paths

    def show_random_image(self):
        random_image_index = random.randint(0, len(self.photo_images) - 1)
        self.random_image = self.photo_images[random_image_index]
        self.Show_dice.config(image=self.random_image)
        self.Show_dice.place(x=110, y=40)

if __name__=="__main__":
    app=MainApplication()
    app.mainloop()