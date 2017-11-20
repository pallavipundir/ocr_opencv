from PIL import Image
import pytesseract
filepath="C:\\Users\\pallavi.pundir\\Downloads\\countries\\Texas\\final images\\image1.png"
im=Image.open(filepath)
print im.size # (width,height) tuple
#print tesserocr.file_to_text("F:/Softwares/aadhar card/outside/img2.jpg", lang='eng+hin')
