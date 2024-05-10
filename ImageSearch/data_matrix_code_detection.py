import numpy as np
import cv2
import imutils
from matplotlib import pyplot as plt


def detect(image):
    kernel = np.ones((2, 2), np.uint8)

    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # convert the image to greyscale
    grey = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    # calculate and plot histogram of an image
    hist = cv2.calcHist(grey, [0], None, [256], [0, 256])

    # blur and threshold the image

    thresh = cv2.adaptiveThreshold(grey, 200, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
    (_, thresholdImage) = cv2.threshold(grey, 160,255, cv2.THRESH_BINARY)

    # compute the Sobel gradient magnitude representation of the image
    # in both the x and y direction
    gradX = cv2.Sobel(grey, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=1)
    gradY = cv2.Sobel(grey, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=1)

    # subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    opening = cv2.morphologyEx(thresholdImage, cv2.MORPH_CLOSE, kernel)

    # contours, hierarchy = cv2.findContours(thresholdImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    return opening

