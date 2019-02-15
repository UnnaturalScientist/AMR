#!/usr/bin/env python

import rospy
import sys
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from numpy import mean
import numpy as np

class colorContour():

    def __init__(self):

        self.node_name = "color_contour"
        rospy.init_node(self.node_name)

        self.cv_window_name = self.node_name
        self.bridge = CvBridge()

        rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback)
        rospy.Timer(rospy.Duration(0.03), self.open_windows) # timer for displaying windows


    def open_windows(self,event):
    	try:

		cv2.namedWindow("Cammy", cv2.WINDOW_NORMAL)
		cv2.namedWindow("Slice", cv2.WINDOW_NORMAL)

        	cv2.imshow("Cammy",self.frame)
        	cv2.imshow("Slice",self.processed_image)

      		cv2.waitKey(3)

    	except:
		pass

    def image_callback(self, data):
        # Use cv_bridge() to convert the ROS image to OpenCV format
        try:
            self.frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError, e: # try and catch called from Cv2
            print e
	    pass

        frame = np.array(self.frame, dtype = np.uint8)
  	self.processed_image = self.color_slice(frame)

    def color_slice(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	print mean(hsv)	# prints the mean
	lower_blue = np.array([ 10,  10,  10]) # HSV not RGB
	upper_blue = np.array([255, 255, 250])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)        
	masked = cv2.bitwise_and(self.frame, self.frame, mask=mask)	
	
        return masked
	

colorContour()
rospy.spin()
