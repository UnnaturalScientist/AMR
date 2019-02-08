#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32
//define the display text
def callback(data):
    rospy.loginfo("I receive %s", data.data)

//define the subscriber
def random_subscriber():
    rospy.init_node('random_subscriber')
    rospy.Subscriber('rand_no',Int32, callback)
    rospy.spin()

if __name__=='__main__':
    random_subscriber()
