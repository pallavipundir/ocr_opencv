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
    #print height
    #print width
    image = cv2.resize(image, (width*2, height*2), interpolation = cv2.INTER_CUBIC)
    
    print height
    print width
    
    
    
    
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
   
    # cv2.imwrite("E:/licence/test10.jpg",bilateral)
     # write the grayscale image to disk as a temporary file so we can apply OCR to it #
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, custom)
    cv2.imwrite("E:/licence/2.png",custom)

    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file #
    text = pytesseract.image_to_string(Image.open(filename)).upper()
   
    
    text = regex.sub('[^a-zA-Z0-9\s\d\w\b\t\n:/\-\'^.,*\/]*','', text)
    #return text
    text1=text.split() 
    newtest = " ".join(str(x) for x in text1)
    
    #text=text.replace("/","-")
    text=text.replace('\n\n','\n')
    #text=text.replace('\n\n','\n')
    #print " ".join(text)
   # text1="7AN DRIVER LICENSE MDL 14728398 9 CLASSC 4A ISS 06-03-2014 2 EXP 05-27-2018 3 DOB 05-27-1974 1 HERNANDEZ 2 ERMINDA LYNN 8 220 MAUDE ST. WHARTON TX 77488"
    text1=str(text1) 
    #return text
    #print np.array(list(text))
    
   # regexArray['INFO']=r'RESTRICTIONS\s+[a-zA-Z]+\sUEND\s+[a-zA-Z]+\n[0-9a-zA-Z]+\s+HGT\s[0-9]\/[0-9]{2}\s[0-9]{2}\s+[a-zA-Z]+\s(M|F)\s+[0-9]\.\s+[a-zA-Z]+\s[a-zA-Z]+'



#For pan card 

    


# for aadhar card

   
      # print ( key + "=> notfound"
    m = regex.search('((T|I|\/|\/ )(/s*)?[MALE|FEMALE ]+)(=?)[0-9 ]{15}', newtest)
    r= regex.search('(PERMANENT ACCOUNT NUMBET|PERMANENT ACCOUNT NUMBER|PERMANENT ACCOUNT NUMHRAN|PERMANENT ACCOUNT NU-OR)\s*\K[A-Z 0-9A-Z]{10,11}', newtest)
    d= regex.search('(DL|MDL)\s*\K[A-Z0-9]{8,10}\s*|NUMBER\s*\K[A-Z0-9]{8,11}',newtest)
    if m:
        regexArray = dict.fromkeys(['NAME','DOB/YEAR OF BIRTH','AADHAAR NUMBER','GENDER'])
        regexArray['NAME']=r'(WW R|INDIA EH F|[0-9]{9}|[0-9]{2,3}(::)?)(\s*)?\K[A-Z]+\s[A-Z]+|[A-Z ]+(?=WI\/)'
        regexArray['DOB/YEAR OF BIRTH']=r'[A-Z](\s*)?[0-9](\s*)?(\-|\/|I)[A-Z](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4}|[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9](\s*)?[0-9]{3}|(YEAR OF BIRTH)\s*(:)?\s*\K[0-9]+'
        regexArray['AADHAAR NUMBER']=r'[0-9 ]{15}'
        #regexArray['FATHER NAME']=r'[A-Z]{3,15}\s*[A-Z]+\s*([0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4})|[A-Z]{3,15}\s*[A-Z]+\s*[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9]\s*[0-9]{3}'    
        regexArray['GENDER']=r'( I|QRR I|\/|\/ )(/s*)?\K[MALE|FEMALE]+'
        
        parsed_data = {}        
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

 

        parsed_data['NAME']=re.sub('\s{2,}', ' ', re.sub('[0-9\/_\']+', '', parsed_data['NAME']))
        parsed_data['DOB/YEAR OF BIRTH']=re.sub('\s{1,2}','',re.sub('[A-Z]+','0',parsed_data['DOB/YEAR OF BIRTH']))
        parsed_data['AADHAAR NUMBER']=re.sub('\s{1,}','',parsed_data['AADHAAR NUMBER'])
        #parsed_data['FATHER NAME']=re.sub('\s{2,}','',re.sub('','',parsed_data['FATHER NAME']))
        parsed_data['GENDER']=re.sub('\s{2,}','',re.sub('\/GQRRI','',parsed_data['GENDER']))
        #finalz='\n'.join("{}: {}".format(attrib, regx) for attrib, regx in parsed_data.items())
        finalz='\n'.join("{}: {}".format(attrib, regx) for attrib, regx in parsed_data.items())
        return finalz

        
    elif r:
        regexArray = dict.fromkeys(['DOB','NAME','PAN NUMBER','FATHER NAME'])
        regexArray['NAME']=r'(INDIA EH F|INCOME TAX DEPARTMENT CI GOVT(.)? OF INDIA TV |INCOME TAX DEPARTMENT|INCOMETAX DEPARTMENT|GOVT(.)? OF INDIA|INCOME TAX DEPARTMENT GOVT(.)? OF INDIA|INCOME TAX DEPARTMENT (_\')? GOVT(.)? OF INDIA|NZMRMNXR)\s*\K[A-Z]+\s[A-Z]+'
        regexArray['DOB']=r'[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4}|[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9]\s*[0-9]{3}'
        regexArray['PAN NUMBER']=r'(NUMBET|NUMBER|NUMHRAN|NU-OR)\s*\K[A-Z 0-9A-Z]{10,11}'
        regexArray['FATHER NAME']=r'[A-Z]{3,15}\s*[A-Z]+\s*([0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4})|[A-Z]{3,15}\s*[A-Z]+\s*[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9]\s*[0-9]{3}'
        parsed_data = {}        
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


        parsed_data['NAME']=re.sub('\s{1,}', ' ', re.sub('[0-9\/_\']+', '', parsed_data['NAME']))
        parsed_data['DOB']=re.sub('\s{1,2}','',re.sub('[A-Z]+','/',parsed_data['DOB']))
        parsed_data['PAN NUMBER']=re.sub('\s{1,}','',parsed_data['PAN NUMBER'])
        parsed_data['FATHER NAME']=re.sub('\s{2,}','',re.sub('[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|I|L)[0-9]{4}|[0-9](\s*)?[0-9](\s*)?(\-|\/|I)[0-9](\s*)?[0-9](\s*)?(\-|\/|1)[0-9]\s*[0-9]{3}','',parsed_data['FATHER NAME']))
        #finalz='\n'.join("{}: {}".format(attrib, regx) for attrib, regx in parsed_data.items())
        finalz='\n'.join("{}: {}".format(attrib, regx) for attrib, regx in parsed_data.items())
        return finalz

    elif d:
        regexArray = dict.fromkeys(['DL','CLASS','ISS','EXP','DOB','NAME','ADDRESS','GENDER'])
        regexArray['DL'] = r'(DL|[0-9]|[a-zA-Z]{6,8})\s*\K[A-Za-z0-9]{8,10}\s*(?=[0-9]+\s*.*)|NUMBER\s*\K[A-Z0-9]{8,11}(?=\s*.*)'
        regexArray['CLASS']=r'C(I|L)ASS(:)?\s*\K[A-Z](?=.*)'
        regexArray['ISS']=r'(I|L)SS\s*\K[0-9]{2}(\-|\/)[0-9]{2}(\-|\/)[0-9]{4}|ISSUED\s*\K[0-9]{2}(\-|\/)[0-9]{2}(\-|\/)([0-9]{4}|[0-9\s]{4,5})'
        regexArray['EXP']=r'(EXP|EXP(IR|U)ES)\s*\K[0-9 ]{2,}(\-|\/|L)[0-9]{2}(\-|\/)[0-9]{4}'
        regexArray['DOB']=r'(DOB|DATE\s*OF\s*BIRTH|ONE|NOS)(:)?\s*\K[0-9]{2}(\-|\/|I)[0-9]{2}(\-|\/|I)[0-9]{4}'
        regexArray['NAME']=r'(DOB|ONE)\s*[0-9]{2}(\/|\-)[0-9]{2}(\/|\-)[0-9]{4}\s*([0-9]{1,2})?\s*\K[A-Z]+\s*([A-Z]+)?\s*([0-9]{1,2}|\'|_)?\s*[A-Z ]+(?=\s*[0-9]{1}\s*)|[0-9]{2}(\-|\/)[0-9]{2}(\-|\/)[0-9]{4}\s*[0-9]{0,2}\s*[A-Z]+\s*[0-9]{0,2}\s*[A-Z\s]+(?=\s*[0-9]{1,2}\s*[0-9]{2,5})|(ARIZONA|RIZON)\s*DRIVER\s*LICENSE\s*\K[A-Z\s]+(?=[0-9]{1,5})|(LN)\s*[a-zA-Z]+\s*(FN)\s*[a-zA-Z ]+'
        #regexArray['FATHER NAME']=r'[a-zA-Z ]'
        regexArray['ADDRESS']=r'(DOB|ONE|NOS|EXP)\s*[0-9]{2}(\/|\-)[0-9]{2}(\/|\-)[0-9]{4}\s*([0-9]{1,2})?\s*[A-Z]+\s*([A-Z]+)?\s*([0-9]{1,2}|\'|_)?\s*[A-Z ]+\s{1,2}([0-9]{1}\s{1,2})?\K[0-9]{3,6}\s*[A-Z]+(.*)TX\s*[0-9]{3,6}(\-[0-9]{4})?|((ARIZONA|RIZON)\s*DRIVER\s*LICENSE|ISSUED\s*[0-9]{2}\/[0-9]{2}\/[0-9]{4})\s*[A-Z\s]+\K[0-9]{3,6}.*AZ\s*[0-9]{3,6}(\s*\-[0-9]{2,4})?'
        regexArray['GENDER']=r'(SEX)(:)?\s*(M|F)'

        parsed_data = {}        
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


        parsed_data['NAME'] = re.sub('\s{2,}', ' ', re.sub('[0-9\/_]+', '', parsed_data['NAME']))
        parsed_data['DL']=re.sub('\s{2,}','',re.sub('[a-z]+','',parsed_data['DL']))
        parsed_data['ISS']=re.sub('\s{2,}','',re.sub('[A-Z]+','',parsed_data['ISS']))
        parsed_data['EXP']=re.sub('\s{2,}','',re.sub('[A-Z]+','/',parsed_data['EXP']))
        parsed_data['DOB']=re.sub('\s{2,}','',re.sub('[A-Z]+','/',parsed_data['DOB']))
        parsed_data['GENDER']=re.sub('\s{1,}','',re.sub('[SEX(:)?]+','',parsed_data['GENDER']))
        
        finalz='\n'.join("{}: {}".format(attrib, regx) for attrib, regx in parsed_data.items())            
        return finalz

    else:
        return "Enter the clear image"


   
    #print()
    #f.close()
        
    #file = open("C:/Users/pallavi.pundir/Documents/selected_images_text.txt","w") 
    #file.write(finalz) 
    #file.close()
    #cv2.imshow("", img_file)
    #cv2.imshow("Person Identity", crop_img)
    #cv2.waitKey(0)
        
    
