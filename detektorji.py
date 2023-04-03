import cv2 as cv
import numpy as np
from scipy import signal
def resize(image, width, height):
    return cv.resize(image, (width, height))

def convolute(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2
    
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')
    convoluted_image = np.zeros_like(image)
    for i in range(image_height):
        for j in range(image_width):
            patch = padded_image[i:i+kernel_height, j:j+kernel_width]
            convoluted_image[i, j] = np.sum(patch * kernel)    
    
    return convoluted_image

def my_roberts(image):
    image = np.uint8(image)
    kernel = np.array([[1.0, 0.0],  #roberts cross
                       [0.0, -1.0]])
    kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)
    kernel_t = np.transpose(kernel)
    # image = cv.filter2D(image, -1, kernel)
    # edge_image = cv.filter2D(image, -1, kernel_t)
    image = convolute(image, kernel)
    edge_image = convolute(image, kernel_t)
    return edge_image

def my_prewitt(image):
    kernel = np.array([[1.0, 0.0, -1.0],
                       [1.0, 0.0, -1.0],
                       [1.0, 0.0, -1.0]])
    kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)
    kernel_t = np.transpose(kernel)

    #image = cv.filter2D(image, -1, kernel)
    #edge_image = cv.filter2D(image, -1, kernel_t)
    
    image = convolute(image, kernel)
    edge_image = convolute(image, kernel_t)
    # edge_image *= 255
    return edge_image

def my_sobel(image):
    kernel = np.array([[1.0, 0.0, -1.0],
                       [2.0, 0.0, -2.0],
                       [1.0, 0.0, -1.0]])
    kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)
    kernel_t = np.transpose(kernel)
    
    #image = cv.filter2D(image, -1, kernel)
    #edge_image = cv.filter2D(image, -1, kernel_t)
    
    image = convolute(image, kernel)
    edge_image = convolute(image, kernel_t)
    return edge_image

def my_canny(image, threshold_bottom=0, threshold_top=0):
    edge_image = cv.Canny(image, threshold_bottom, threshold_top)
    return edge_image

def spremeni_kontrast(image, alpha, beta):
    image = cv.multiply(image, alpha)
    image = cv.add(image, beta)
    return image
