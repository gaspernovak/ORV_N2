import detektorji as det
import tkinter as tk
import cv2 as cv
import numpy as np
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("400x400")


img_cv = cv.imread("./images/image.jpg")
img_cv = cv.cvtColor(img_cv, cv.COLOR_BGR2GRAY) # PIL uporablja RGB kot default color space
img_cv = det.resize(img_cv, 400, 300)

def slider_changed(event):
    new_image = det.spremeni_kontrast(img_cv, slider_alpha.get(), slider_beta.get())
    new_image = Image.fromarray(new_image)
    new_image = ImageTk.PhotoImage(new_image)
    label.configure(image=new_image)
    label.image = new_image

image = Image.fromarray(img_cv)
image = ImageTk.PhotoImage(image)

label = tk.Label(window, image=image)
label.grid(row=0)

alpha_value = tk.DoubleVar()
beta_value = tk.DoubleVar()

slider_alpha = tk.Scale(
    window, 
    from_=0.0, 
    to_=255.0, 
    orient="horizontal",
    command=slider_changed,
    variable=alpha_value)

slider_beta = tk.Scale(
    window, 
    from_=0.0, 
    to_=255.0, 
    orient="horizontal",
    command=slider_changed,
    variable=beta_value)

slider_alpha.grid(row=1, sticky="we")
slider_beta.grid(row=2, sticky="we")

window.mainloop()