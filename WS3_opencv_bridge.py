#!/usr/bin/env python

import rospy
from cv2 import namedWindow, cvtColor, imshow
from cv2 import startWindowThread, destroyAllWindows
from cv2 import COLOR_BGR2GRAY, waitKey # BGR because of numpy (reverse RGB)
from cv2 import blur, Canny
from numpy import mean # funny if you leave out
from sensor_msgs.msg import Image
import cv2, cv_bridge

class image_converter:
  # CV Bridge provides and interface between ROS and OpenCV
  def __init__(self): 
    self.bridge = cv_bridge.CvBridge()
    cv2.namedWindow("window", 1) # provides one GUI window
    self.image_sub = rospy.Subscriber('camera/rgb/image_raw', 
                                      Image, self.image_callback)
  def image_callback(self, data): # Callback to the ROS Image Message
    # imgmsg_to_cv2 = catches any conversion errors
    namedWindow("window") # name the window "window" -- also done for blur and canny
    #namedWindow("blur")
    #namedWindow("canny")

    image = self.bridge.imgmsg_to_cv2(data,desired_encoding='bgr8') # 8 bit RGB/BGR image
    gray_img = cvtColor(image, COLOR_BGR2GRAY) # converts the image to grayscale
    print mean(gray_img) # prints the mean of the pixel values

    img2 = blur(gray_img, (3, 3)) # 3*3 kernel?
    imshow("blur", img2) # blur filter applied
    img3 = Canny(gray_img, (10, 200 ))
    imshow("canny", img3) # canny edge detection applied

    cv2.imshow("window", image)
    cv2.waitKey(3) 

startWindowThread() # start the GUI image display

rospy.init_node('ic')
ic = image_converter()
rospy.spin()

destroyAllWindows() # close all GUI windows
