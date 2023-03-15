import cv2 as cv
import numpy as np

def my_roberts(image):
    kernel = np.array([[1.0, 0.0],  #roberts cross
                       [0.0, -1.0]])
    kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)
    edge_image = cv.filter2D(image, -1, kernel)
    return edge_image

def my_prewitt(image):
    kernel = np.array([[1.0, 0.0, -1.0],
                       [1.0, 0.0, -1.0],
                       [1.0, 0.0, -1.0]])
    
    kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)
    kernel_t = np.transpose(kernel)
    
    image = cv.filter2D(image, -1, kernel)
    edge_image = cv.filter2D(image, -1, kernel_t)
    
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
cv.imwrite("./images/image_roberts.jpg", image_roberts)

image_prewitt = my_prewitt(image)
cv.imwrite("./images/image_prewitt.jpg", image_prewitt)