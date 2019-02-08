#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# define the display text
def callback(data):
    rospy.loginfo("I receive %s", data.data)

# define the subscriber
def mean_subscriber():
    rospy.init_node('mean_sub')
    rospy.Subscriber('print_mean',String, callback)
    rospy.spin()

if __name__=='__main__':
    mean_subscriber()
