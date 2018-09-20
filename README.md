# SeniorDesignMiniProject

# Motivation
Senior Design groups in the past have have wasted time successfully connecting Raspbery pi's to the BU encrypted internet (802.1x), installing an operating system, and connecting external hardware to the pi. The purpose of this project was to eliminate this pitfall and have electrical engineers in their senior design groups well versed in this piece of hardware. The purpose of this particular project was to determine the amount of cars passing in each frame. 

## Materials

1). [Raspberry Pi Zero](https://www.google.com/aclk?sa=l&ai=DChcSEwihoYK7rMjdAhUJnLMKHUmkBkQYABABGgJxbg&sig=AOD64_1MRwKVqANLd_4U0Q5fyg3-UyDgEw&ctype=5&q=&ved=0ahUKEwiW3fy6rMjdAhVNm-AKHT5mCawQ9aACCDE&adurl=)

2). [Raspberry Pi Camera](https://www.google.com/aclk?sa=l&ai=DChcSEwjlkYbLrMjdAhXFVg0KHRbuBWUYABAEGgJxYg&sig=AOD64_2SDYdBCgdkinCS4KokfkoZclmBbw&ctype=5&q=&ved=0ahUKEwj51YDLrMjdAhUtneAKHfYsA4IQ9aACCDg&adurl=)

3). [MicroUSB power source](https://www.google.com/aclk?sa=l&ai=DChcSEwiZuPXfrMjdAhVMgbMKHcOZBSwYABAEGgJxbg&sig=AOD64_3-79f1w5ECbjEMgNozrPNbRH6uUg&ctype=5&q=&ved=0ahUKEwiZqu_frMjdAhXrdN8KHTKfBeYQ9aACCD4&adurl=) 

4). [MircoUSB to USB-C](https://www.google.com/aclk?sa=l&ai=DChcSEwi00_mCrcjdAhWXiLMKHbZzCaEYABAFGgJxbg&sig=AOD64_3XFmfzVcgdf3B5r5507Uqw77oytw&ctype=5&q=&ved=0ahUKEwjfnfSCrcjdAhXlct8KHVuPAdcQ9aACCD8&adurl=)

OR 

Purchase the affordable [kit](https://www.vilros.com/shop/raspberry-pi-kits/raspberry-pi-zero-w-basic-starter-kit/) 


## Hardware Component Setup

1). Download OpenCv on Raspberry Pi. 

To download OpenCV on Raspberry Pi, we used the help provided in - https://docs.opencv.org/3.4.1/d7/d9f/tutorial_linux_install.html

2). Recording video using Raspberry Pi Camera NoiR

To record the video using the Raspberry Pi, we first had to connect a camera to the pi. After this was connected we had to create a script using Python to record a video for 10 seconds. 

## Software Component Setup

1). Detecting Cars on the video recorded using code provided by Azfal Saan. This file is labeled ```countcar.py``` on our wiki. 

## Running the Code

1). Ensure to install numpy using ```pip install numpy``` 

2). First, point your Raspberry Pi Camera to traffic, then in terminal type: 

```camera.py``` in your desired directory. 

3). The file should be saved in the appropiate directory. Then type in terminal 

```countcar.py``` The code should then be able to detect the amount of cars in each frame. 


## Contributions

Anirudh Sriram (CE) - Developed script and install OpenCV on Raspberry Pi, Connected Camera to Pi, Increased Virtual Memory

Ashaki Gumbs (EE)- Installed OS and OpenCV on Raspberry Pi, Connected Camera to pi, Increased Virtual Memory, Setup SSH on Raspberry Pi
 

## References


https://raspi.tv/2013/another-way-to-convert-raspberry-pi-camera-h264-output-to-mp4

https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7

https://docs.opencv.org/3.4.1/d7/d9f/tutorial_linux_install.html
 
