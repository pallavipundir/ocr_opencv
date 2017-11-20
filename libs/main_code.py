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
    #from PIL import ImageEnhance
    #from scipy import misc

    # Load image, resize width and height & then convert to grayscale
    image = cv2.imread(img_file)
    height, width = image.shape[:2]
    image = cv2.resize(image, (width*2, height*2), interpolation = cv2.INTER_CUBIC) 
    #resized_image = cv2.resize(image, (, 100))
    #rows,cols = image.shape
    #M = cv2.getRotationMatrix2D((width/2,height/2),360,1)
    #dst = cv2.warpAffine(image,M,(width,height))
    #equ = cv2.equalizeHist(image)
    #cv2.imwrite("E:/licence/10.jpg",image)
    #thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] 
    #cv2.imwrite("E:/licence/1.jpg",thresh)
   
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
    
    
    #equ = cv2.equalizeHist(custom)
    #cv2.imwrite("E:/licence/6.jpg",custom)
    
    # write the grayscale image to disk as a temporary file so we can apply OCR to it #


  #  filename = "E:/OCR_Work/ocr_opencv/storage/files/{}.png".format(os.getpid())

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, custom)
    cv2.imwrite("E:/licence/2.png",custom)

    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file #
    text = pytesseract.image_to_string(Image.open(filename)).upper()
   
    
    text = re.sub('[^a-zA-Z0-9\s\d\w\b\t\n:/\-\'^.,*\/]*','', text)

    text=text.replace("/","-")
    text=text.replace('\n\n','\n')
    #text=text.replace('\n\n','\n')
    #print " ".join(text)
   # text1="7AN DRIVER LICENSE MDL 14728398 9 CLASSC 4A ISS 06-03-2014 2 EXP 05-27-2018 3 DOB 05-27-1974 1 HERNANDEZ 2 ERMINDA LYNN 8 220 MAUDE ST. WHARTON TX 77488"
        
    #return text
    #print np.array(list(text))
   # regexArray = {}
   # regexArray['DL'] = r'DL\s+[0-9]{8,12}\s+[0-9]{1,2}'
   # regexArray['CLASS']=r'[0-9 ]+CLASS+[a-zA-Z]'
   # regexArray['ISS']=r'[0-9]+[a-zA-Z ]+[0-9]{1,2}\-[0-9]{1,2}\-[0-9]{1,4}'
   # regexArray['EXP']=r'EXP\s+[0-9]{2}\-[0-9]{2}\-[0-9]{4}'
   # regexArray['DOB']=r'DOB\s+[0-9]{2}\-[0-9]{2}\-[0-9]{4}'
    #regexArray['NAME']=r'[a-zA-Z ]'
    #regexArray['FATHER NAME']=r'[a-zA-Z ]'
    #regexArray['ADDRESS']=r'[0-9 ]+\s*+[a-zA-Z ]+\.\n[a-zA-Z 0-9]+'
    #regexArray['INFO']=r'[0-9a-zA-Z ]+HGT\s+[0-9]+\-[0-9]{2}\s+[0-9 ]+SEX\s+(M|F)\s[0-9]+\.\s+EYES\s+[a-zA-Z]+'
    #newarray = []
    #regex =  r"DL\s+[0-9]{8,12}\s+[0-9]{1,2}"    
    #if re.search(regex,text):
     #   m = re.search(regex,text)
      #  print m.group(0)
        #regexArray[key] = m.group()
    #else : 
     #   print 'No match'


    #for key, value in regexArray.iteritems():
        #print '{}: {}'.format(key, value)
       
    #for key,value in regexArray.items:
       # m = re.search(value,text1)
       # if m:
         #  print m.group(0)
            #regexArray[key] = m.group()
        #else : 
         #   regexArray[key] = 'No match'

        

        #m = re.search(regexArray[key],text)
        #if m:
         #   newarray[key] = m.group(0)
        #else :
         #   newarray[key] = 'No match'

    
    #regexArray.append(regexArray)
    
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
    #finaltext=" \n".join(text1)
    
    #data = finaltext.split("\n")
    #print finaltext
    #words = finaltext.split(" ") 
   # print words
    
    
    # show the output images
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    #cv2.waitKey(0)
    
    #return " ".join(text) #.strip('"\'')
    return finaltext
