import cv2
from PIL import Image
import pytesseract
im = cv2.imread('C:/Users/pallavi.pundir/Downloads/countries/alabama/formatted images/al1(2).jpg')
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
_, contours, _ = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
idx =0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    roi=im[y:y+h,x:x+w]
    cv2.imwrite('C:/Users/pallavi.pundir/Downloads/countries/alabama/formatted images/' + str(idx) + '.jpg', roi)
    #cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)

text = pytesseract.image_to_string(Image.fromarray(im)).upper()
print text
cv2.imshow('img',im)
cv2.waitKey(0)  


  
