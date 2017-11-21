import PIL
from PIL import Image
import pytesseract
import cv2
import os , re, regex
import numpy as np
from datetime import datetime
import dateutil
import subprocess
import matplotlib
from matplotlib import pyplot as plt
#from PIL import ImageEnhance
# Load image, resize width and height & then convert to grayscale
img_file="/home/pallavi/Downloads/countries/alabama/dl(8).jpg"
img = cv2.imread(img_file, 0)
ret1,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur, 125, 355, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("/home/pallavi/E/licence/ret4.jpg", th3)
# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in xrange(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()