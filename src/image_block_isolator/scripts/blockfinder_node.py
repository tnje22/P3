#!/usr/bin/env python3
import rospy
import cv2

if __name__ == '__main__':
    rospy.init_node("test_node")

    rospy.loginfo("i have begun")

    rospy.sleep(1)

    rospy.loginfo("i have ended")