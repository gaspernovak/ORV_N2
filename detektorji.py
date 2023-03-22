import cv2 as cv
import numpy as np

def resize(image, width, height):
    return cv.resize(image, (width, height))

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
    kernel = np.array([[1.0, 0.0, -1.0],
                       [2.0, 0.0, -2.0],
                       [1.0, 0.0, -1.0]])
    kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)
    kernel_t = np.transpose(kernel)
    
    image = cv.filter2D(image, -1, kernel)
    edge_image = cv.filter2D(image, -1, kernel_t)
    return edge_image

def my_canny(image, threshold_bottom=0, threshold_top=0):
    edge_image = cv.Canny(image, threshold_bottom, threshold_top)
    return edge_image

def spremeni_kontrast(image, alpha, beta):
    image = cv.multiply(image, alpha)
    image = cv.add(image, beta)
    return image
