import numpy as np
import cv2 as cv
import detektorji as det
import tkinter as tk

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    ret, frame = cap.read()
    frame = det.resize(frame, 800, 500)
    if not ret:
        print("Can't receive frame. Exiting ...")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
    edge_image = det.my_canny(gray, 50, 150)
    inverted_edge_image = cv.bitwise_not(edge_image)
    masked = cv.bitwise_and(gray, inverted_edge_image)
    cv.imshow('frame', masked)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

