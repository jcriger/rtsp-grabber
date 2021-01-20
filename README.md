# RTSP-Grabber
Grab still images from RTSP streams. Useful for making things like timelapses.

RTSP-Grabber is an application for grabbing still images from RTSP streams at specific intervals.
Instructions are for running on a Raspberry Pi and connecting to Wyze cameras, but should work with other RTSP devices with minimal changes.

If you are new to using a Raspberry Pi , checkout the HINTS.md file.

# Camera
Designed to work with Wyze Cam v2 running the alternate RTSP firmware. Instructions and alternate firmware can be found here:

https://wyzelabs.zendesk.com/hc/en-us/articles/360026245231-Wyze-Cam-RTSP

# Setup
You will need to install some dependancies in order to run the script. Run the following commands to get setup:

 Install [OpenCV](https://opencv.org) for Python
 ```sh
pip3 install opencv-python
 ```

Install [OpenCV](https://opencv.org) dependancies
```sh
sudo apt update
```
```sh
sudo apt-get install -y libatlas-base-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test
```

Install Python packages for date/time handling
```sh
pip3 install python-dateutil 
```

# Downloading the app
Download the following files and put them in a directory of your choosing (make sure they are both in the same directory):
 - config.txt
 - rtsp-grabber.py

Alternatively you can download them using the following command in the terminal:
```sh
wget https://github.com/jcriger/rtsp-grabber/blob/main/config.txt
wget https://github.com/jcriger/rtsp-grabber/blob/main/rtsp-grabber.py
```

# Configuration

The configuration is stored in the config.txt file. At a minimum you will need to edit the __rtsp_url__ before using the app. 

The main settings are:

__rtsp_url__: This url is found in the setting on the Wyze app (you need to be running the alternate firmware with RTSP enabled)

__image_directory__: This is where the captured images will be stored

__interval__: The seconds to wait between capturing images. 0 is as fast as possible (ends up being around every 5 seconds). 3600 is once an hour. 86400 is once a day.

__name_format__: How the image files are named. Options are unix, utc, local. utc and local are human readable, but use different timezones. unix is a number representing seconds since a standard date. Only jpeg files are currently supported.

__quality__: Image compression. 100 is best. 0 will hurt your eyes, but is really small.

# Running the app

RTSP-Grabber will look for a file called config.txt in the directory it is running. If this file is not found it will display an error and quit.

The easiest way to run the application is to open the Terminal [*ctrl + alt + t*], then navigate to the directory is it in and running the command below. When you want to stop press [*ctrl + c*]
 ```sh
python3 rtsp-grabber.py
 ```