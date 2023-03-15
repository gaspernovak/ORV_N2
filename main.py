import cv2 as cv
import numpy as np

def my_roberts(image):
    kernel = np.array([[1.0, 0.0],  #robert's cross
                       [0.0, -1.0]])
    kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)
    edge_image = cv.filter2D(image, -1, kernel)
    return edge_image

def my_prewitt(image):
    pass
    return edge_image

def my_sobel(image):
    pass
    return edge_image

def canny(slika, bottom, top):
    pass
    return edge_image

def spremeni_kontrast(image, alpha, beta):
    image = cv.multiply(image, alpha)
    image = cv.add(image, beta)
    return image

image = cv.imread("./images/image.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

image_contrast = spremeni_kontrast(image, 3, -80)
cv.imwrite("./images/image_contrast.jpg", image_contrast)

image_roberts = my_roberts(image)
cv.imwrite("./images/image_robers.jpg", image_roberts)