import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/home/pallavi/Downloads/countries/alabama/dl(8).jpg")
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
cv2.imwrite("/home/pallavi/E/licence/customy2.jpg",img)
plt.imshow(img)
plt.colorbar()
plt.show()
