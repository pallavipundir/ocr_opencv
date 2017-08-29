import subprocess
import os

# image name to load #
filename = "04.42.50.PM_28.Aug.2017_dl1.png"

# get current directry #
pwd = os.getcwd()
print pwd
# output text file path #
output_text = os.path.join(pwd, filename+'.txt')
#print output_text
# command for cli => tessearct image_file output_text_file
cmdCommand = "tesseract "+os.path.join(pwd,"storage", "files", filename)+" "+output_text
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
