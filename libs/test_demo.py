#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def test_default(img_file):
    from PIL import Image
    import pytesseract
    import cv2
    import os , re
    import numpy as np
    #image = cv2.imread(img_file,)
    image = img_file
    #print text 
    text = pytesseract.image_to_string(Image.open(image),lang="eng").upper()
    text = re.sub('[^a-zA-Z0-9\s\n/:-]+','', text)
    print text
	#os.remove(filename)

    finaltext = strip_non_ascii(text)

    #if finaltext in locals():
    return finaltext
    #else :
        #return "Your OCR Program is wrong, plz rework"
    
