import subprocess
import os

# image name to load #
filename = "11.17.13.PM_28.Aug.2017_img.jpg"

# get current directry #
pwd = os.getcwd()

# output text file path #
output_text = os.path.join(pwd, "storage", "cache", filename+'.txt')

# command for cli => tessearct image_file output_text_file
cmdCommand = "tesseract "+os.path.join(pwd, "storage", "files", filename)+" "+output_text
#print cmdCommand

# catch any exception in command
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# read output text file
files = open(output_text+'.txt', "r") 
final_text = files.read() 

print final_text

# remove temporary text file
## os.remove(output_text+'.txt')

