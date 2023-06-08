import sys
import cv2
import numpy as np

from tkinter import *
from PIL import ImageTk, Image
window = Tk()
window.title("kevin is better ")
window.geometry("700x500")

image = cv2.imread('./download.jpeg', cv2.IMREAD_ANYCOLOR)
blurred_img = cv2.GaussianBlur(image, (21, 21), 0)
mask = np.zeros(image.shape, np.uint8)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[2]
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(mask, contours, -1, (255,255,255),5)
output = np.where(mask==np.array([255, 255, 255]), blurred_img, image)


top = Toplevel()
label = Label(top,


