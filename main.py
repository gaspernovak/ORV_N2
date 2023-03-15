import cv2 as cv
import numpy as np

def my_robers(image):
    pass
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


cv.namedWindow("Image")
image = cv.imread("./images/image.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

kernel = np.array([1, 1, 1], 
                  [1, 1, 1],
                  [1, 1, 1])

print(kernel)

cv.imshow("Image", image)
cv.waitKey(0)