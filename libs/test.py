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

    # Load image, resize width and height & then convert to grayscale
    image = cv2.imread(img_file)
    height, width = image.shape[:2]
    image = cv2.resize(image, (width*2, height*2), interpolation = cv2.INTER_AREA) 

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the image #
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove noise #
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    dst = cv2.fastNlMeansDenoisingColored(image,None,5,5,3,14)

    b,g,r = cv2.split(dst)           # get b,g,r
    rgb_dst = cv2.merge([r,g,b])     # switch it to rgb

    
    kernel=np.zeros((5,5),np.float32)#Create the identity filter, but with the 1 shifted to the right!
    kernel[3,3]=2.0   #Identity, times two! 
    boxFilter=np.ones((5,5),np.float32)/81.0 # default is 81.0 Blurs an image using the box filter.
    kernel=kernel-boxFilter
    custom=cv2.filter2D(rgb_dst,-1,kernel)
    cv2.imwrite("F:/Softwares/pan and dl/dl/img.jpg",custom)
    # write the grayscale image to disk as a temporary file so we can apply OCR to it #
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, custom)

    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file #
    text = pytesseract.image_to_string(Image.open(filename)).upper()

    text = re.sub('[^a-zA-Z0-9,\s\n:/-]+', ' ', text)
    #print text
    os.remove(filename)

    finaltext = strip_non_ascii(text)
    # print finaltext
    # show the output images
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    #cv2.waitKey(0)

    return finaltext