import detektorji as det
import tkinter as tk
import cv2 as cv
import numpy as np
from PIL import ImageTk, Image

def generate_edge_images(ksize):
    image = np.asarray(current_img)
    image = cv.GaussianBlur(image, ksize, 5)

    image_contrast = det.spremeni_kontrast(image, 3, -80)
    cv.imwrite("./images/image_contrast.jpg", image_contrast)

    image_roberts = det.my_roberts(image)
    cv.imwrite("./images/image_roberts.jpg", image_roberts)

    image_prewitt = det.my_prewitt(image)
    cv.imwrite("./images/image_prewitt.jpg", image_prewitt)

    image_sobel = det.my_sobel(image)
    cv.imwrite("./images/image_sobel.jpg", image_sobel)

    image_canny = det.my_canny(image, 100, 150)
    cv.imwrite("./images/image_canny.jpg", image_canny)

    print("Successfully generated images.")

def slider_changed(event):
    global current_img
    image = det.spremeni_kontrast(img_cv, slider_alpha.get(), slider_beta.get())
    current_img = image 
    pil_image = Image.fromarray(image)
    pil_image = ImageTk.PhotoImage(pil_image)
    label.configure(image=pil_image)
    label.image = pil_image


window = tk.Tk()
window.geometry("700x720")

img_cv = cv.imread("./images/lenna.png")
img_cv = cv.cvtColor(img_cv, cv.COLOR_BGR2GRAY)
img_cv = det.resize(img_cv, 700, 600)

image = Image.fromarray(img_cv)
image = ImageTk.PhotoImage(image)
label = tk.Label(window, image=image)
label.grid(row=0)

alpha_value = tk.DoubleVar()
beta_value = tk.DoubleVar()

slider_alpha = tk.Scale(
    window, 
    from_=-20.0, 
    to_=20.0, 
    orient="horizontal",
    command=slider_changed,
    variable=alpha_value)

slider_beta = tk.Scale(
    window, 
    from_=-255.0, 
    to_=255.0, 
    orient="horizontal",
    command=slider_changed,
    variable=beta_value)

button = tk.Button(
    window, 
    text="Generate edge images", 
    command=lambda : generate_edge_images((9, 9))
    )

slider_alpha.grid(row=1, sticky="we")
slider_beta.grid(row=2, sticky="we")
button.grid(row=3, sticky="we")

window.mainloop()