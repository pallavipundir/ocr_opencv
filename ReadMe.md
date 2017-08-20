Server => Ubuntu 16.04

Installing Required Modules For Build


Install

sudo apt update
sudo apt install python-pip python-dev python-setuptools git cmake python3-pip python3-setuptools

sudo -H pip install --upgrade pip


sudo -H pip install numpy pillow pytesseract argparse logger --upgrade


Install OpenCV (GTK Extended)

sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran libpjproject-dev
sudo apt-get install python2.7-dev python3.5-dev





sudo -H pip install require

cd opencv-3.1.0/
mkdir build
cd build
sudo cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.1.0/modules \
    -D PYTHON_EXECUTABLE=/usr/bin/python \
    -D BUILD_EXAMPLES=ON ..


sudo make -j4 

# if Error Then Run:
sudo make clean
sudo make


troubleshoot:

$ python
>>> import cv2




 2052  Sun 20.Aug.17 04:36:06 AM => sudo apt-get install build-essential cmake pkg-config
 2053  Sun 20.Aug.17 04:36:14 AM => sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
 2054  Sun 20.Aug.17 04:36:22 AM => sudo apt-get install libgtk-3-dev
 2055  Sun 20.Aug.17 04:36:50 AM => sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
 2056  Sun 20.Aug.17 04:36:59 AM => sudo apt-get install libgtk-3-dev
 2057  Sun 20.Aug.17 04:37:06 AM => sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
 2058  Sun 20.Aug.17 04:37:24 AM => sudo apt-get install build-essential cmake pkg-config
 2059  Sun 20.Aug.17 04:37:46 AM => sudo apt-get install libgtk-3-dev
 2060  Sun 20.Aug.17 04:37:51 AM => sudo apt-get install libatlas-base-dev gfortran
 2061  Sun 20.Aug.17 04:38:38 AM => sudo apt-get install python2.7-dev python3.5-dev
 2062  Sun 20.Aug.17 04:39:09 AM => wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
 2063  Sun 20.Aug.17 04:40:12 AM => wget -c -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
 2064  Sun 20.Aug.17 04:45:57 AM => unzip opencv.zip 
 2065  Sun 20.Aug.17 04:46:03 AM => unzip opencv-3.1.0/
 2066  Sun 20.Aug.17 04:46:08 AM => unzip opencv_contrib.zip 




sudo pip install numpy pillow pytesseract argparse logger jinja2 flask werkzeug --upgrade




git clone <link> app


cd appsudo apt-get install liblapacke-dev checkinstall
bash starter.sh




## Installing CPU boosting libs ##
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install libboost-all-dev

sudo apt-get install libatlas-base-dev
sudo apt-get install libopenblas-dev

sudo apt install libpjproject-dev
sudo apt-get install build-essential emacs dkms synaptic ssh




## Build Tesseract ##

sudo apt-get install libleptonica-dev



sudo apt-get install liblapacke-dev checkinstall