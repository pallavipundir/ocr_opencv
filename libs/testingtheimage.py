import PIL
from PIL import Image
import pytesseract
import cv2
import os , re, regex
import numpy as np
from datetime import datetime
import dateutil
import subprocess
#from PIL import ImageEnhance
#from scipy import misc
#from pathlib import Path

# Load image, resize width and height & then convert to grayscale
img_file="/home/pallavi/Desktop/adh1.jpg"
image = cv2.imread(img_file)
#crop_img = image[130:800, 35:210]

height, width = image.shape[:2]
#print height
#print width
image = cv2.resize(image, (width*2, height*2), interpolation = cv2.INTER_CUBIC)

print height
print width
#height, width, _ = img.shape  
#resized_image = cv2.resize(image, (, 100))
#rows,cols = image.shape
#print rows,cols
#M = cv2.getRotationMatrix2D((width/2,height/2),360,1)
#dst = cv2.warpAffine(image,M,(width,height))
#equ = cv2.equalizeHist(image)
#cv2.imwrite("E:/licence/10.jpg",image)
#th, im_th = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY_INV)
thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] 
cv2.imwrite("/home/pallavi/E/licence/threshing.jpg",thresh)
#cv2.imwrite("E:/licence/width.txt",width)


#thresh=image.fill(255)
#cv2.imwrite("E:/licence/tt.jpg",thresh)
# edge detection
#edges = cv2.Canny(thresh,2,100, apertureSize = 3)
#cv2.imwrite("E:/licence/2.jpg",edges)
# fill the holes from detected edges

# 
#dilate = cv2.dilate(thresh, kernel, iterations=1)
#cv2.imwrite("E:/licence/3.jpg",dilate)

#enh = ImageEnhance.Contrast(image)
#cv2.imwrite("E:/licence/img7.jpg",enh)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the image #
#if preprocess == "thresh":
#gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


# make a check to see if median blurring should be done to remove noise #
#elif preprocess == "blur":
#   gray = cv2.medianBlur(gray, 3)
#kernel = np.ones((2,2),np.uint8)
#dilation = cv2.erode(image,kernel,iterations =1)
#cv2.imwrite("E:/licence/1.jpg",dilation)
#blur = cv2.GaussianBlur(img,(5,5),0)


dst = cv2.fastNlMeansDenoising(image,None,10,7,21)
dst1 = cv2.fastNlMeansDenoising(dst,None,7,5,17)
dst2 = cv2.fastNlMeansDenoising(dst1,None,7,5,17)
b,g,r = cv2.split(dst2)           # get b,g,r
rgb_dst = cv2.merge([r,g,b])     # switch it to rgb
#cv2.imwrite("E:/licence/2.jpg",dilation)
kernel=np.zeros((5,5),np.float32)#Create the identity filter, but with the 1 shifted to the right!
kernel[3,3]=2.0   #Identity, times two! 
boxFilter=np.ones((5,5),np.float32)/91.0 # default is 81.0 Blurs an image using the box filter.
kernel=kernel-boxFilter
custom=cv2.filter2D(rgb_dst,-1,kernel)
#kernel1 = np.ones((2,2),np.uint8)
#dilation = cv2.erode(custom,kernel1,iterations =1)
#cv2.imwrite("E:/licence/test8.jpg",dilation)

#equ = cv2.equalizeHist(custom)
#cv2.imwrite("E:/licence/6.jpg",custom)

# write the grayscale image to disk as a temporary file so we can apply OCR to it #

# generating the kernels

#kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])


# applying different kernels to the input image
#output_1 = cv2.filter2D(dilation, -1, kernel_sharpen_1)
#cv2.imwrite("E:/licence/test9.jpg",output_1)
#  filename = "E:/OCR_Work/ocr_opencv/storage/files/{}.png".format(os.getpid())
#bilateral = cv2.bilateralFilter(custom,15,75,75)
#
# cv2.imwrite("E:/licence/test10.jpg",bilateral)
# write the grayscale image to disk as a temporary file so we can apply OCR to it #
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, custom)
cv2.imwrite("E:/licence/2.png",custom)

# load the image as a PIL/P5illow image, apply OCR, and then delete the temporary file #
text = pytesseract.image_to_string(Image.open(filename)).upper()


text = regex.sub('[^a-zA-Z0-9\s\d\w\b\t\n:/\-\'^.,*\/]*','', text)
#return text
text1=text.split() 
newtest = " ".join(str(x) for x in text1)
print newtest