
from datetime import datetime
from PIL import Image
import pytesseract
import cv2
import os , re
import numpy as np


# Load image, resize width and height & then convert to grayscale
image = cv2.imread("F:\\Softwares\\New Folder\\img7.jpg")
height, width = image.shape[:2]
image = cv2.resize(image, (width*4, height*4), interpolation = cv2.INTER_AREA) 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Denoising#

dst = cv2.fastNlMeansDenoising(gray,None)
#b,g,r = cv2.split(dst)           # get b,g,r
#rgb_dst = cv2.merge([r,g,b]) 
# check to see if we should apply thresholding to preprocess the image #
#if image == "thresh":

#Sharpening#
kernel=np.zeros((5,5),np.float32)#Create the identity filter, but with the 1 shifted to the right!
kernel[3,3]=2.0   #Identity, times two! 
boxFilter=np.ones((5,5),np.float32)/81.0 # default is 81.0 Blurs an image using the box filter.
kernel=kernel-boxFilter
custom=cv2.filter2D(dst,-1,kernel)

#gray = cv2.threshold(gray, 0, 255,
#cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove noise #
#elif image == "blur":
	#gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can apply OCR to it #
#filename = "F:\\Softwares\\New folder\\gray.png".format()
cv2.imwrite("F:\\Softwares\\New folder\\gray.png",custom)

# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file #
text=pytesseract.image_to_string(Image.open("F:\\Softwares\\New folder\\gray.png"),lang="eng").upper()

text = re.sub('[^a-zA-Z0-9\s\n/-]+','', text)
text=text.replace("/")
#if text=='DD/MM/YYYY':
    	#print "date of birth",text
#print text
#os.remove(filename)

#finaltext = strip_non_ascii(text)

# show the output images
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
cv2.waitKey(0)
print text
#print finaltext
