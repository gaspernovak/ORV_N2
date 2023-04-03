import cv2 as cv
import numpy as np
import detektorji as det
import matplotlib.pyplot as plt
import matplotlib.image as img

def show_one(title, img1):
    fig = plt.figure(figsize=(12, 7))
    plt.title(title)
    plt.imshow(img1, cmap="gray")
    plt.show()

def show_compare(title1, title2, img1, img2):
    fig = plt.figure(figsize=(12, 4))
    fig.add_subplot(1, 2, 1)
    plt.title(title1)
    plt.imshow(img1, cmap="gray")
    fig.add_subplot(1, 2, 2)
    plt.title(title2)
    plt.imshow(img2, cmap="gray")
    plt.show()
    

image = cv.imread("./images/Bikesgray.jpg")
image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
image = cv.GaussianBlur(image, (5, 5), 5)

image_contrast = det.spremeni_kontrast(image, 0, -80)
cv.imwrite("./images/image_contrast.jpg", image_contrast)

image_roberts = det.my_roberts(det.spremeni_kontrast(image, 1, 0))
cv.imwrite("./images/image_roberts.jpg", det.spremeni_kontrast(image_roberts, 1, 0)) # povečamo kontrast za boljšo vidljivost robov
show_one("roberts", image_roberts)
#show_compare("Base", "Roberts cross", image, image_roberts)

image_prewitt = det.my_prewitt(det.spremeni_kontrast(image, 2, -120))
cv.imwrite("./images/image_prewitt.jpg", image_prewitt)
#show_one("prewitt", image_prewitt)
# show_compare("Base", "Prewitt operator", image, image_prewitt)

image_sobel = det.my_sobel(det.spremeni_kontrast(image, 2, -100))
cv.imwrite("./images/image_sobel.jpg", image_sobel)
#show_one("sobel", image_sobel)
# show_compare("Base", "Sobel operator", image, image_prewitt)

image_blurred = cv.GaussianBlur(image, (5, 5), 5)
image_canny = det.my_canny(image, 50, 80)
image_canny_2 = det.my_canny(image, 120, 200)
cv.imwrite("./images/image_canny.jpg", image_canny)

#show_compare("bottom = 50, top = 80", "bottom = 120, top = 200", image_canny, image_canny_2)
#show_one("canny, bottom = 100, top = 200", image_canny)


