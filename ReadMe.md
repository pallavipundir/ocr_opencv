Setting up demo on Ubuntu 16.04
-
Install Deps

    $ sudo apt install libtesseract3 tesseract-ocr tesseract-ocr-eng
    $ sudo apt-get install build-essential emacs dkms synaptic ssh
    $ sudo apt-get install libleptonica-dev

Install OpenCV [from this link](https://github.com/abhis27/opencv_xenial/blob/master/Readme.md) .  

    $ sudo pip install numpy pillow pytesseract argparse logger jinja2 flask werkzeug regex --upgrade

To run demo app , use:

    $ python server.py 
