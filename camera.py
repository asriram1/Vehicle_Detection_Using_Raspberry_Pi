from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.resolution = (512,512)
camera.start_preview()
camera.start_recording('videonew3.h264')
sleep(20)
camera.stop_recording()
camera.stop_preview()
