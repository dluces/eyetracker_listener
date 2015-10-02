#!/usr/bin/env python

import rospy
from eyetracker_listener.msg import GazeData


def callback(data):
    rospy.loginfo("I heard (%.1f, %.1f, %d)", data.loc.x, data.loc.y, data.event)
    
def listener():
    rospy.init_node('eyetracker_listener')
    rospy.Subscriber("eyetracker", GazeData, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()