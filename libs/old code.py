#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def ocr_default(img_file,preprocess) :
    from PIL import Image
    import pytesseract
    import cv2
    import os , re
    import numpy as np
    from datetime import datetime
    import dateutil
    import subprocess

    # Load image, resize width and height & then convert to grayscale
    image = cv2.imread(img_file,0)
    height, width = image.shape[:2]
    image = cv2.resize(image, (width*1, height*1), interpolation = cv2.INTER_AREA) 
    
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the image #
    #if preprocess == "thresh":
    
    

    # make a check to see if median blurring should be done to remove noise #
    #elif preprocess == "blur":
     #   gray = cv2.medianBlur(gray, 3)

    dst = cv2.fastNlMeansDenoising(image,None,10,7,21)
    dst1 = cv2.fastNlMeansDenoising(dst,None,7,5,17)
    dst2 = cv2.fastNlMeansDenoising(dst1,None,7,5,17)
    #b,g,r = cv2.split(dst2)           # get b,g,r
    #rgb_dst = cv2.merge([r,g,b])     # switch it to rgb

    #gray = cv2.threshold(dst2, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    kernel=np.zeros((5,5),np.float32)#Create the identity filter, but with the 1 shifted to the right!
    kernel[4,4]=2.0   #Identity, times two! 
    boxFilter=np.ones((5,5),np.float32)/81.0 # default is 81.0 Blurs an image using the box filter.
    kernel=kernel-boxFilter
    custom=cv2.filter2D(dst2,-1,kernel)
    #cv2.imwrite("E:/licence/img.jpg",custom)
    #kernel=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    custom=cv2.filter2D(dst2,-1,kernel)
    cv2.imwrite("E:/licence/img.jpg",custom)
    equ = cv2.equalizeHist(custom)
    #boxFilter=np.ones((5,5),np.float32)/81.0
    #kernel=kernel-boxFilter
    # write the grayscale image to disk as a temporary file so we can apply OCR to it #
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, equ)
    cv2.imwrite("E:/licence/img1.png",custom )

    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file #
    text = pytesseract.image_to_string(Image.open(filename)).upper()
  
    #if text=="%d/%m/%Y":
     #   text=text.replace("/","-")
    #text=text.replace("/","-")
    text = re.sub('[^a-zA-Z0-9\s\d\w\b\t\n:/\-\'^.,*\/]*','', text)
    
    #text = re.sub('[a-zA-Z\s0-9\s]+\s*DL\s*\K[0-9]{8,10}(?=\s*[0-9]{1,}\s*.*)','',text)
    text=text.replace("-","/")
    text=text.replace('\n\n','\n')
    
    #format(text, '<20')
    #text=re.sub('[0-9]+/[0-9]+/[0-9]','',text)
    #re.match('^[A-Za-z0-9.,:;!?()\s]+$', str)
    #text = re.sub("[/]","-", text)
    #if text=='%d/%m/%Y':
    
    
    #text=text.split("/")
    #text.join(text)
    #print datetime.strptime(text,text)
    #print text
    #if text=="%d/%m%Y":
       # text=text.replace("/","-")
    #os.remove(filename)

    finaltext = strip_non_ascii(text)
    print finaltext
    
    
    # show the output images
    # cv2.imshow("Image", image)
     
    #cv2.waitKey(0)
    cv2.imshow("E:/licence/img1.png", img_file)
    return finaltext.ljust(50," ")