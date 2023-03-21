import detektorji as det
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack()

img = Image.open("./images/image.jpg")
img = det.resize(img)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=tk.NW)

window.mainloop()