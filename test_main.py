from PIL import Image
import pytesseract
import cv2
import os , re

image = cv2.imread("F:/Softwares/New folder/pancard.jpg")
height, width = image.shape[:2]
image = cv2.resize(image, (width*6, height*3), interpolation = cv2.INTER_AREA) 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# check to see if we should apply thresholding to preprocess the image #
if image == "thresh":
	gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	# make a check to see if median blurring should be done to remove noise #
elif image == "blur":
	gray = cv2.medianBlur(gray, 3)

	# write the grayscale image to disk as a temporary file so we can apply OCR to it #
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file #
def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

text = re.sub('[:/^a-zA-Z0-9\s\n]+','', text)
print text
finaltext = strip_non_ascii(text)
print finaltext
os.remove(filename)

	# show the output images
	# cv2.imshow("Image", image)
	# cv2.imshow("Output", gray)
cv2.waitKey(0)