# SeniorDesignMiniProject - Vehicle Detection using Raspberry Pi

# Motivation
With the advent of features like auto-pilot in cars as well as recent advancements in self-driving car technology, one of the most crucial steps toward more advanced driverless navigation systems is achieving greater levels of safety. Driverless navigation systems need to be extremely effective at detecting and recognizing their surroundings, including other vehicles. Our project aims to create a fairly basic program which will be used to detect vehicles using a Raspberry Pi. 

## Materials

1). [Raspberry Pi Zero](https://www.google.com/aclk?sa=l&ai=DChcSEwihoYK7rMjdAhUJnLMKHUmkBkQYABABGgJxbg&sig=AOD64_1MRwKVqANLd_4U0Q5fyg3-UyDgEw&ctype=5&q=&ved=0ahUKEwiW3fy6rMjdAhVNm-AKHT5mCawQ9aACCDE&adurl=)

2). [Raspberry Pi Camera](https://www.google.com/aclk?sa=l&ai=DChcSEwjlkYbLrMjdAhXFVg0KHRbuBWUYABAEGgJxYg&sig=AOD64_2SDYdBCgdkinCS4KokfkoZclmBbw&ctype=5&q=&ved=0ahUKEwj51YDLrMjdAhUtneAKHfYsA4IQ9aACCDg&adurl=)

3). [MicroUSB power source](https://www.google.com/aclk?sa=l&ai=DChcSEwiZuPXfrMjdAhVMgbMKHcOZBSwYABAEGgJxbg&sig=AOD64_3-79f1w5ECbjEMgNozrPNbRH6uUg&ctype=5&q=&ved=0ahUKEwiZqu_frMjdAhXrdN8KHTKfBeYQ9aACCD4&adurl=) 

4). [MircoUSB to USB-C](https://www.google.com/aclk?sa=l&ai=DChcSEwi00_mCrcjdAhWXiLMKHbZzCaEYABAFGgJxbg&sig=AOD64_3XFmfzVcgdf3B5r5507Uqw77oytw&ctype=5&q=&ved=0ahUKEwjfnfSCrcjdAhXlct8KHVuPAdcQ9aACCD8&adurl=)

OR 

Purchase the affordable [kit](https://www.vilros.com/shop/raspberry-pi-kits/raspberry-pi-zero-w-basic-starter-kit/) 


## Hardware Component Setup

1). Download OpenCv on Raspberry Pi.  To download OpenCV on Raspberry Pi, we used the help provided in https://docs.opencv.org/3.4.1/d7/d9f/tutorial_linux_install.html

2). Recording video using Raspberry Pi Camera NoiR. To record the video using the Raspberry Pi, we first had to connect a camera to the pi. After this was connected we had to create a script using Python to record a video for 20 seconds. However one of the issues with the recorded video was that the resolution was too high, which meant processing time was too long. Hence we had to change the resolution of the recorded video to 512 by 512 pixels. This script can be found in camera.py. 

## Software Component Setup

1) To create the vehicle detection program we decided to use Python owing to its wide range of libraries which help with this project. We name the file ```countcar.py```. 

2) We first imported openCV into python.

3) We then imported the video that was recorded through the raspberry pi, and converted it into frames. 

4) An xml classifier is used so objects similar to cars are recognized in the frames.

5) The frames that are read are converted first into gray scale, and from these new images, cars of different sizes are detected.

6) A for loop is used to draw rectangles around all the detected vehicles in the frames

7) All the new frames are then displayed, with the rectangles, in a new window

8) Finally a function closes this new window and de-allocates any associated memory usage

## Running the Code

1). Ensure to install numpy using ```pip install numpy``` 

2). Download this repository

3). First, point your Raspberry Pi Camera to traffic, then in terminal type: 

```camera.py``` in your desired directory. 

4). The file should be saved in the appropiate directory. Then type in terminal 

```countcar.py``` The code should then be able to detect the amount of cars in each frame. 


## Contributions

Anirudh Sriram (CE) - Developed vehicle detection script, Installed OpenCV on Raspberry Pi, Connected Camera to Pi, Increased Virtual Memory

Ashaki Gumbs (EE)- Installed OS and OpenCV on Raspberry Pi, Developed video recording script, Connected Camera to pi, Increased Virtual Memory, Setup SSH on Raspberry Pi

## Project Obstacles 

One of the issues with using a raspberry pi is the little amount of RAM, which makes processing time too long. Hence to account for this, we restriced the video time to just 20 seconds and set the video to record at a low resolution of 512 by 512 pixels. Another small hindrance was the extremely long build time for OpenCV. The Raspberry pi was left running overnight to let OpenCV install completely. Another small issue with the program is the few false alarms being detected in the newly generated video, which meant the program is not 100% accurate.

## Future Improvements

To develop our project further, we would focus on eliminating all false alarms in our vehicle detection. Furthermore, we would also want to implement code which will help count the number of cars passing through a particular area. 
 
## References


https://raspi.tv/2013/another-way-to-convert-raspberry-pi-camera-h264-output-to-mp4

https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7

https://docs.opencv.org/3.4.1/d7/d9f/tutorial_linux_install.html
 
