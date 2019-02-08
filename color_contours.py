  GNU nano 2.5.3                  File: color_contours2.py                                           

#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image

class Slice:
  def __init__(self):
    self.bridge = cv_bridge.CvBridge()
    cv2.namedWindow("HSV slice window", 1)
    self.image_sub = rospy.Subscriber('camera/rgb/image_raw', 
                                      Image, self.image_callback)
  def image_callback(self, data):
    image = self.bridge.imgmsg_to_cv2(data) # Cv bridge to ROS Image
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert the RGB image to HSV (Hue based)

    # Set the colour boundaries
    lower_red = numpy.array([ 50,  50, 170]) # lower boundary of colour (e.g. yellow) -- dark
    upper_red = numpy.array([255, 255, 190]) # upper boundary of colour (e.g. yellow) -- bright

    # Essentially, anything in range of the HSV spectrum...
    # ...between the upper and lower boundaries is detected
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow) 

    # colour is sliced and is applied to a new layer mask
    # bitwise_and: computes bit-wise AND of two arrays element-wise
    masked = cv2.bitwise_and(image, image, mask = mask) 
    cv2.imshow("HSV slice window", mask ) # window displaying the mask is shown
    cv2.waitKey(3)

    # publish string (Task 3)
    
    
rospy.init_node('slice')
slice = Slice()
rospy.spin()





