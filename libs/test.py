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
    #cv2.imwrite("E:/licence/img.jpg",custom)
    
    # write the grayscale image to disk as a temporary file so we can apply OCR to it #


  #  filename = "E:/OCR_Work/ocr_opencv/storage/files/{}.png".format(os.getpid())

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, custom)
    cv2.imwrite("E:/licence/2.png",custom)

    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file #
    text = pytesseract.image_to_string(Image.open(filename)).upper()
    
    #[a-zA-Z0-9-,'._ ]+\s*
    #text=re.match(r"[a-zA-Z\s*]",text)
    #text=re.match(r"[a-zA-Z\s*a-zA-Z\s*a-zA-Z\s*0-9a-zA-Z\s*(DOB|date\s*of\s*birth)\s*:?\s*[0-9]{2}\s*\/\s*[0-9]{1,2}\s*\/\s*[0-9]{4}a-zA-Z\s*a-zA-Z\s*a-zA-Z\s*[0-9]{1}\s*\-[0-9]{1}\s*[0-9]\s*a-zA-Z\s*[0-9]{2}\s*\-[0-9]{4}\s*a-zA-Z\s*[0-9]{2}\s*\-\s*[0-9]{1,2}\s*\-\s*[0-9]{4}",text)
    text = re.sub('[^a-zA-Z0-9\s\d\w\b\t\n:/\-\'^.,*\/]*','', text)
    #text1=text.split()
    #print text1
    #print("length is",len(text1))
    #For appending or store the results 
    
    #
        #print text1[i] 
    #network=[]   

    #while:
    #for i in text1:
   # print text1[0],text1[1]
    #print text1[2],text1[3]
    #print text1[5],":",text1[6]
    #print text1[8],text1[9]
    #print "Issue Date:",text1[12]
    #print "Expiry Date:",text1[15]
    #print "Date of Birth:",text1[18]
    #print "Name:",text1[20]
    #print "Father's Name:",text1[21],text1[22]
    #print "Address:",text1[24],text1[25],",",text1[26],text1[27],text1[28],text1[29]
    #network.append(text1)
        #print text1[26],text1[27],text1[28],text1[29]


    #output_join = [text1[0],"\n","Texas","\n ",text1[6],"NO. :",text1[7],text1[9],"\nIssue Date:",text1[12],"\nDate of Birth:",text1[24],"\nName:",text1[25],"\nFather's Name:",text1[26],text1[27],"\nAddress:",text1[29],text1[30],text1[31],",","\n",text1[32],text1[33],text1[34]]
    #output_join = [text1[0],"\n","Texas","\n ",text1[2],text1[3],",",text1[4]," ",text1[5],":",text1[6],"\n",text1[7]," ",text1[8],text1[9],"\nIssue Date:",text1[12],"\nExpiry Date:",text1[11]," ",text1[12]," ",text1[13]," ",text1[14]," ",text1[15],"\nDate of Birth:",text1[16]," ",text1[17]," ",text1[18],"\nName:",text1[20],"\nFather's Name:",text1[21],text1[22],"\nAddress:",text1[24],text1[25],",","\n",text1[26],text1[27],text1[28],text1[29]] 
    #output_join = [text1[0],"\n",text1[1],text1[2],"\nDL:",text1[5],"\n",text1[6],"\n",text1[7],text1[8],text1[9],text1[10],text1[11],text1[12],text1[13],text1[14],text1[15],text1[16],text1[17],text1[18]] 
    #for elem in output_join:
     #   print elem 
    #print "\n".join(output_join)
    #print output_join.split("\n")
    #output_join='\n '.join(output_join)
    #print "\n".join(output_join)
    #finalz = " ".join(repr(x.encode('ascii')) for x in output_join)

    #text1=text.split("  ")
    #print text1
    #print("length is",len(text1))
    
    #for i in range(len(text1)):
        #print text1[i] 
        #print("Driver's licence is",text1[0])  
     #   print text1[1]


    #text=text.split('\n')
    #text
    #text=re.search(re.compile(r"[^a-zA-Z$a-zA-Z$a-zA-Z$0-9a-zA-Z$a-zA-Z0-9$a-zA-Z0-9$a-zA-Z$a-zA-Z$a-zA-Z$0-9]",re.MULTILINE),text).group(1)
    #text = re.sub('[a-zA-Z\s0-9\s]+\s*DL\s*\K[0-9]{8,10}(?=\s*[0-9]{1,}\s*.*)','',text)
    #text=text.replace("/","-")
    #text=text.replace('\n\n','\n')
    #print np.array(list(text))
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
    
<<<<<<< HEAD
    #return " ".join(output_join) #.strip('"\'')
    return finaltext
=======
    return " ".join(output_join) #.strip('"\'')
    #return finaltext
>>>>>>> ca29ffed6c273a33aed317b66bf204126408b352
