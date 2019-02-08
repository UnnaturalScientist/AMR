#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from numpy import mean
from std_msgs.msg import String
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
    lower_red = numpy.array([ 90, 0, 0]) # lower boundary of colour (e.g. red) -- dark
    upper_red = numpy.array([255, 0, 0]) # upper boundary of colour (e.g. red) -- bright

    # Essentially, anything in range of the HSV spectrum...
    # ...between the upper and lower boundaries is detected
    mask = cv2.inRange(hsv, lower_red, upper_red) 

    # colour is sliced and is applied to a new layer mask
    # bitwise_and: computes bit-wise AND of two arrays element-wise
    masked = cv2.bitwise_and(image, image, mask = mask) 
    cv2.imshow("HSV slice window", mask ) # window displaying the mask is shown
    cv2.waitKey(3)

  # publish string (Task 3)
  def mean_publisher():
    rospy.init_node('mean_pub')
    pub = rospy.Publisher('print_mean', String, queue_size=10)
    p = rospy.Publisher('/result_topic', String)
    while not rospy.is_shutdown():
       pub.publish('print_mean') #This may need changing
       p.sleep()
    
rospy.init_node('slice')
slice = Slice()
rospy.spin()

# Main for Task 3
if __name__=='__main__':
    try:
        mean_publisher()
    except rospy.ROSInterruptException:
        pass





