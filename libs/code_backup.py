#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def ocr_default(img_file, preprocess) :
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
    
    # Load image, resize width and height & then convert to grayscale
  
    image = cv2.imread(img_file)
    #crop_img = image[130:800, 35:210]
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
    blur = cv2.GaussianBlur(image,(5,5),0)
    #ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # generating the kernels
    kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])


    # applying different kernels to the input image
    output_1 = cv2.filter2D(blur, -1, kernel_sharpen_1)
    cv2.imwrite("F:/Softwares/PAn Card/p1.jpg",output_1)
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
   
    
    text = regex.sub('[^a-zA-Z0-9\s\d\w\b\t\n:/\-\'^.,*\/]*','', text)
    #return text
    text1=text.split() 
    newtest = " ".join(str(x) for x in text1)
    return newtest
    #print("length is",len(text1))
    #For appending or store the results 
    #return newtest

    
    #output_join = [text1[0],"Texas",text1[1],text1[2],text1[3],text1[4],text1[5],text1[6],text1[7],text1[8],text1[9],text1[10],text1[11],text1[12],text1[13],text1[14],text1[15],text1[16],text1[17],text1[18]] 
    #output_join = [text1[0],"\n","Texas","\n ",text1[2],text1[3],",",text1[4]," ",text1[5],":",text1[6],"\n",text1[7]," ",text1[8],text1[9],"\nIssue Date:",text1[12],"\nExpiry Date:",text1[11]," ",text1[12]," ",text1[13]," ",text1[14]," ",text1[15],"\nDate of Birth:",text1[16]," ",text1[17]," ",text1[18],"\nName:",text1[20],"\nFather's Name:",text1[21],text1[22],"\nAddress:",text1[24],text1[25],",","\n",text1[26],text1[27],text1[28],text1[29]] 
    #output_join = [text1[0],"\n",text1[1],text1[2],"\nDL:",text1[5],"\n",text1[6],"\n",text1[7],text1[8],text1[9],text1[10],text1[11],text1[12],text1[13],text1[14],text1[15],text1[16],text1[17],text1[18]] 
    #for elem in output_join:
     #   print elem 
    #print "  ".join(output_join)
    #print output_join.split("\n")
    #output_join='\n '.join(output_join)
    #print "\n".join(output_join)
    
    #finalz = " ".join(repr(x.encode('ascii')) for x in text1)

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
    text=text.replace('\n\n','\n')
    #text=text.replace('\n\n','\n')
    #print " ".join(text)
   # text1="7AN DRIVER LICENSE MDL 14728398 9 CLASSC 4A ISS 06-03-2014 2 EXP 05-27-2018 3 DOB 05-27-1974 1 HERNANDEZ 2 ERMINDA LYNN 8 220 MAUDE ST. WHARTON TX 77488"
    text1=str(text1) 
    #return text
    #print np.array(list(text))
    regexArray = {}
    regexArray['DL'] = r'(DL|[0-9]|[a-zA-Z])\s*\K[A-Za-z0-9]{8,10}\s*(?=[0-9]+\s*.*)|NUMBER\s*\K[A-Z0-9]{8,11}(?=\s*.*)'
    regexArray['CLASS']=r'C(I|L)ASS(:)?\s*\K[A-Z](?=.*)'
    regexArray['ISS']=r'(I|L)SS\s*\K[0-9]{2}(\-|\/)[0-9]{2}(\-|\/)[0-9]{4}|ISSUED\s*\K[0-9]{2}(\-|\/)[0-9]{2}(\-|\/)([0-9]{4}|[0-9\s]{4,5})'
    regexArray['EXP']=r'(EXP|EXP(IR|U)ES)\s*\K[0-9 ]{2,}(\-|\/|L)[0-9]{2}(\-|\/)[0-9]{4}'
    regexArray['DOB']=r'(DOB|DATE\s*OF\s*BIRTH|ONE|NOS)(:)?\s*\K[0-9]{2}(\-|\/|I)[0-9]{2}(\-|\/|I)[0-9]{4}'
    regexArray['NAME']=r'(DOB|ONE)\s*[0-9]{2}(\/|\-)[0-9]{2}(\/|\-)[0-9]{4}\s*([0-9]{1,2})?\s*\K[A-Z]+\s*([A-Z]+)?\s*([0-9]{1,2}|\'|_)?\s*[A-Z ]+(?=\s*[0-9]{1}\s*)|[0-9]{2}(\-|\/)[0-9]{2}(\-|\/)[0-9]{4}\s*[0-9]{0,2}\s*[A-Z]+\s*[0-9]{0,2}\s*[A-Z\s]+(?=\s*[0-9]{1,2}\s*[0-9]{2,5})|(ARIZONA|RIZON)\s*DRIVER\s*LICENSE\s*\K[A-Z\s]+(?=[0-9]{1,5})|(LN)\s*[a-zA-Z]+\s*(FN)\s*[a-zA-Z ]+'
    #regexArray['FATHER NAME']=r'[a-zA-Z ]'
    regexArray['ADDRESS']=r'(DOB|ONE|NOS|EXP)\s*[0-9]{2}(\/|\-)[0-9]{2}(\/|\-)[0-9]{4}\s*([0-9]{1,2})?\s*[A-Z]+\s*([A-Z]+)?\s*([0-9]{1,2}|\'|_)?\s*[A-Z ]+\s{1,2}([0-9]{1}\s{1,2})?\K[0-9]{3,6}\s*[A-Z]+(.*)TX\s*[0-9]{3,6}(\-[0-9]{4})?|((ARIZONA|RIZON)\s*DRIVER\s*LICENSE|ISSUED\s*[0-9]{2}\/[0-9]{2}\/[0-9]{4})\s*[A-Z\s]+\K[0-9]{3,6}.*AZ\s*[0-9]{3,6}(\s*\-[0-9]{2,4})?'
    regexArray['GENDER']=r'(SEX)(:)?\s*(M|F)'
   
   # regexArray['INFO']=r'RESTRICTIONS\s+[a-zA-Z]+\sUEND\s+[a-zA-Z]+\n[0-9a-zA-Z]+\s+HGT\s[0-9]\/[0-9]{2}\s[0-9]{2}\s+[a-zA-Z]+\s(M|F)\s+[0-9]\.\s+[a-zA-Z]+\s[a-zA-Z]+'



#For pan card   
    #regexArray['NAME']=r'(INDIA EH F|INCOME TAX DEPARTMENT CI GOVT(.)? OF INDIA TV |INCOME TAX DEPARTMENT|INCOMETAX DEPARTMENT|GOVT(.)? OF INDIA|INCOME TAX DEPARTMENT GOVT(.)? OF INDIA|INCOME TAX DEPARTMENT (_\')? GOVT(.)? OF INDIA|NZMRMNXR)\s*\K[A-Z]+\s[A-Z]+'
    #regexArray['DOB']=r'[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4}|[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9]\s*[0-9]{3}'
    #regexArray['PAN NUMBER']=r'(NUMBER|NUMHRAN|NU-OR)\s*\K[A-Z 0-9A-Z]{10,11}'
    #regexArray['FATHER NAME']=r'[A-Z]{3,15}\s*[A-Z]+\s*([0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4})|[A-Z]{3,15}\s*[A-Z]+\s*[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9]\s*[0-9]{3}'
    

# for aadhar card

    #regexArray['NAME']=r'(INDIA EH F|WW)\s*\K[A-Z]+\s[A-Z]+'
    #regexArray['DOB']=r'[A-Z](\s*)?[0-9](\s*)?(\-|\/|I)[A-Z](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4}|[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9](\s*)?[0-9]{3}'
    #regexArray['AADHAAR NUMBER']=r'[0-9 ]{15}'
    #regexArray['FATHER NAME']=r'[A-Z]{3,15}\s*[A-Z]+\s*([0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4})|[A-Z]{3,15}\s*[A-Z]+\s*[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9]\s*[0-9]{3}'    
    #regexArray['GENDER']=r'\/[MALE|FEMALE]+'
    #regexArray['ADDRESS']=r'(S/O:)\s[A-Z ]+(\,)?\s[A-Z]\-[0-9]\/[0-9]+\s[A-Z]+\s[A-Z ]+(\,)?[A-Z ]+(\.\s)?[A-Z ]+(\,\s)?[A-Z ]+(\.\s)?[A-Z ]+(\,\s)?[A-Z ]+(\-\s)?[0-9 ]+'
   
    parsed_data = {}
    #for key, value in regexArray.iteritems() :
    # print (key, value)
    for (attrib, regx) in regexArray.iteritems():
        print "Debug: ", attrib, ">> ", regx
    
        if regex.search(regx, newtest):
            match = regex.search(regx, newtest)
            #print(key)
            #print "Match at index".(match.start(), match.end())
            string = (match.group(0))
            
            parsed_data[attrib] = string
        
        else:
            parsed_data[attrib] = "NA" 
            # print ( key + "=> notfound")

  
    #index += 1
    #print(index)
    #newarray[key] = index
    ##newarray.append(key)
    # print ("the key name is" + key + "and its value is" + regexArray[key])


    #for key, value in regexArray.iteritems():
        #print '{}: {}'.format(key, value)
       
    
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
    

#parsed data for DL

    parsed_data['NAME'] = re.sub('\s{2,}', ' ', re.sub('[0-9\/_]+', '', parsed_data['NAME']))
    parsed_data['DL']=re.sub('\s{2,}','',re.sub('[a-z]+','',parsed_data['DL']))
    parsed_data['ISS']=re.sub('\s{2,}','',re.sub('[A-Z]+','',parsed_data['ISS']))
    parsed_data['EXP']=re.sub('\s{2,}','',re.sub('[A-Z]+','/',parsed_data['EXP']))
    parsed_data['DOB']=re.sub('\s{2,}','',re.sub('[A-Z]+','/',parsed_data['DOB']))
    parsed_data['GENDER']=re.sub('\s{1,}','',re.sub('[SEX(:)?]+','',parsed_data['GENDER']))

#parsed data for PAN CARD

    #parsed_data['NAME']=re.sub('\s{2,}', ' ', re.sub('[0-9\/_\']+', '', parsed_data['NAME']))
    #parsed_data['DOB']=re.sub('\s{1,2}','',re.sub('[A-Z]+','/',parsed_data['DOB']))
    #parsed_data['PAN NUMBER']=re.sub('\s{1,}','',parsed_data['PAN NUMBER'])
    #parsed_data['FATHER NAME']=re.sub('\s{2,}','',re.sub('[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4}|[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9]\s*[0-9]{3}','',parsed_data['FATHER NAME']))

#parsed data for AADHAAR NUMBER

    #parsed_data['NAME']=re.sub('\s{2,}', ' ', re.sub('[0-9\/_\']+', '', parsed_data['NAME']))
    #parsed_data['DOB']=re.sub('\s{1,2}','',re.sub('[A-Z]+','0',parsed_data['DOB']))
    #parsed_data['AADHAAR NUMBER']=re.sub('\s{1,}','',parsed_data['AADHAAR NUMBER'])
   # parsed_data['FATHER NAME']=re.sub('\s{2,}','',re.sub('','',parsed_data['FATHER NAME']))
    #parsed_data['GENDER']=re.sub('\s{2,}','',re.sub('\/','',parsed_data['GENDER']))
    #parsed_data['ADDRESS']=re.sub('\.','\n',re.sub('[A-Z]\-[0-9]\/[0-9]+\s*\K[A-Z]+','',parsed_data['ADDRESS']))
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
    
    #return "\n".join(parsed_data).strip('"{}')
    #finalz=parsed_data.strip(' "{}')
    #finalz.split("\n")
    #f = open('C:/Users/pallavi.pundir/Documents/selected_images_text.txt','r')
    #message = f.read()
    #print()
    #f.close()
    finalz='\n'.join("{}: {}".format(attrib, regx) for attrib, regx in parsed_data.items())
    #file = open("C:/Users/pallavi.pundir/Documents/selected_images_text.txt","w") 
    #file.write(finalz) 
    #file.close()
    #cv2.imshow("", img_file)
    #cv2.imshow("Person Identity", crop_img)
    #cv2.waitKey(0)
    #return finalz
