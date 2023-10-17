import tkinter as tk
from tkinter import messagebox as mb
import tkinter.ttk as win
from tkinter.constants import DISABLED, NORMAL
from tkinter import filedialog as fd

from PIL import Image, ImageTk
import slate3k
import os
from PIL.ImageTk import PhotoImage
from PyPDF2 import PdfFileMerger


class PdfEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Editor")
        self.geometry("700x300")
        photo = PhotoImage(file = "Images/icon.png")
        self.iconphoto(False,photo)
        self.maxsize(width=700,height=300)
        self.config(background="#f0f0f0")
        self.imglist = []
        self.fimgl = []
        self.png = True
        # Labels
        self.merger_img = tk.PhotoImage(file="Images/Merger.png")
        merger_img_lbl = win.Label(image=self.merger_img)
        merger_img_lbl.place(x=40, y=40)

        self.image_to_pdf = tk.PhotoImage(file="Images/Image_to_pdf.png")
        pdf_img_lbl = win.Label(image=self.image_to_pdf)
        pdf_img_lbl.place(x=490, y=40)

        self.pdf_to_text = tk.PhotoImage(file="Images/PDF-to-Text.png")
        pdf_img_lbl = win.Label(image=self.pdf_to_text)
        pdf_img_lbl.place(x=265, y=40)

        # Buttons
        Merge_btn = win.Button(text="Merge PDF", command=self.Merge_PDF)
        Merge_btn.place(x=80, y=200)

        extract_text_btn = win.Button(text="Text Extractor", command=self.Extract_text)
        extract_text_btn.place(x=300, y=200)

        self.image_to_pdf_btn = win.Button(text="Image To PDF", command=self.convert_pdf)
        self.image_to_pdf_btn.place(x=520, y=200)

    def Merge_PDF(self):
        filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
        open_PDF_files = fd.askopenfilenames(title="Select PDF Files", filetypes=filetypes)
        merger = PdfFileMerger()
        for pdf in open_PDF_files:
            merger.append(open(pdf, 'rb'))
        merger.write("result.pdf")
        merger.close()

    def convert_pdf(self):
        global files, fimg, order, imglist, tm, png
        files = fd.askopenfilenames(title="Choose images",
                                    filetypes=(("PNGs", "*.png"), ("JPGs", "*.jpg"), ("All Files", "*.*")))
        for i in files:
            self.fimgl.append(i)
        if files:
            for j in self.fimgl:
                if j.endswith(".png"):
                    png = True
                img = Image.open(j)
                fimg = img.convert('RGB')
                self.imglist.append(fimg)
                self.image_to_pdf_btn.config(state=NORMAL)

        try:
            if png:
                self.imglist.pop()
            saveloc = fd.asksaveasfilename(title="Save the PDF file")
            if saveloc:
                if saveloc.endswith(".pdf"):
                    pass
                else:
                    saveloc = saveloc + ".pdf"
                if os.path.exists(saveloc):
                    yn = mb.askyesno("Confirm Save As",
                                     f"{os.path.basename(saveloc)} already exists.\nDo you want to replace it?")
                    if yn:
                        os.remove(saveloc)
                    else:
                        self.convert_pdf()
                fimg.save(saveloc, save_all=True, append_images=self.imglist)
                mb.showinfo("Done!", "PDF file saved! Click 'OK' to open it")
                os.startfile(saveloc)
        except Exception as err:
            mb.showerror("Error", err)

    def Extract_text(self):
        filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
        open_PDF_files = fd.askopenfilename(title="Select PDF Files", filetypes=filetypes)
        with open(os.path.abspath(open_PDF_files), 'rb') as f:
            doc = slate3k.PDF(f)

        saveloc = fd.asksaveasfilename(title="Save the text file")
        if saveloc:
            if saveloc.endswith(".txt"):
                pass
            else:
                saveloc = saveloc + ".txt"
            if os.path.exists(saveloc):
                yn = mb.askyesno("Confirm Save As",
                                 f"{os.path.basename(saveloc)} already exists.\nDo you want to replace it?")
                if yn:
                    os.remove(saveloc)
                else:
                    pass
            myfile = open(saveloc, 'w+')
            myfile.write(str(doc))
            mb.showinfo("Done!", "PDF file saved! Click 'OK' to open it")


app = PdfEditor()
app.mainloop()
