import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import PyPDF2
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.filedialog import asksaveasfile
from pathlib import Path

root = Tk()
root.title("File Converter")


class Application:

    def __init__(self):
        self.browse_txt = None
        canvas = tk.Canvas(root, width=600, height=300)
        canvas.grid(columnspan=3, rowspan=3)

        root.columnconfigure(index=1, weight=1)
        root.rowconfigure(index=1, weight=1)

    def winLogo(self):
        logo = Image.open("File converter.jpg")
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

    def instruction(self):
        self.instruct = tk.Label(root, text="Select files to get converted", font="Calibri")
        self.instruct.grid(columnspan=3, column=1, rows=2)

    def browseButton(self):
        self.browse_txt = tk.StringVar()
        browse_btn = Button(root, textvariable=self.browse_txt, command=lambda: self.open_file(),
                            font="Calibri",
                            bg="#4D8FFE",
                            fg="white", height=1, width=10, borderwidth=5, border=5)
        self.browse_txt.set("Browse")
        browse_btn.grid(columnspan=3, column=1, row=7)

        canvas = tk.Canvas(root, width=600, height=250)
        canvas.grid(columnspan=3, rowspan=3)

    def open_file(self):
        self.browse_txt.set("Loading")
        self.filecollection = [("Pdf file", "*.pdf"),("txt files", "*.txt"),("Python files", "*.py"),("all files", "*.*")]
        self.file = askopenfilename(parent=root, title="Choose a file", filetypes=self.filecollection)

        ext = str(Path(self.file)).partition(".")[2]
        if ext == "pdf":
            self.ConvertandSavePDFfile()
        if ext == "py":
            print("Working on it")

        try:
            if self.file:
                self.new_path = Path(self.file).stem
                self.newLabel = Label(root, text="{} has been added".format(self.new_path), font="Calibri")
                self.instruct.destroy()
                self.newLabel.grid(column=1, row=3)

                print("File selected")

                self.browse_txt.set("Browse")
                self.instruct.destroy()
                self.instruct = tk.Label(root, text=" File has been selected", font="Calibri")
                self.instruct.grid(columnspan=3, column=1, row=2)
            else:
                self.browse_txt.set("Browse")
        except:
            pass

    def MergeButton(self):
        self.convert_txt = tk.StringVar()
        convert_btn = Button(root, textvariable=self.convert_txt, command=lambda: self.ConvertandSavePDFfile(),
                             font="Calibri",
                             bg="#4D8FFE",
                             fg="white", height=1, width=10, borderwidth=5, border=5)
        self.convert_txt.set("Convert")
        convert_btn.grid(columnspan=3, column=1, row=8)

        canvas = tk.Canvas(root, width=600, height=250)
        canvas.grid(columnspan=3, rowspan=3)


    # def ConvertandSavePyFile(self):
    #     file = asksaveasfilename(
    #         filetypes=[("text file", ".txt")],
    #         defaultextension=".txt")
    #     py_read = open(file)
    #     for i in py_read:
    #         fob = open(file, 'a+', encoding="utf-8")
    #         fob.write(i)
    #         fob.close()


    def ConvertandSavePDFfile(self):
        file = asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
        self.pdf_reader = PyPDF2.PdfReader(self.file)

        for i in range(1, self.pdf_reader.numPages):
            fob = open(file, 'a+', encoding="utf-8")
            self.extract_pages = self.pdf_reader.getPage(i)
            self.extracted_texts = self.extract_pages.extractText()
            print(self.extracted_texts)
            fob.write(str(self.extracted_texts))
            fob.close()

    def pdfWriteToText(self):
        print("PDF Fun working")

    def overall_fun(self):
        self.winLogo()
        self.instruction()
        self.browseButton()
        # self.pdfconverterButton()

        self.MergeButton()
        self.pdfWriteToText()


app = Application()
app.overall_fun()
root.mainloop()
