#!/usr/bin/env python3

import rospy 
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def callback(data):


    bridge = CvBridge()
    #rospy.loginfo(rospy.get_caller_id() + " Encoding = %s ", data.encoding)
    
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')   

    edges = cv2.Canny(cv_image, 200 ,200 )
    #hsv = cv2.cvtColor(cv_image , cv2.COLOR_BGR2HSV)

    #lower_range = np.array([128,0,0])
    #upper_range = np.array([165,42,42])
   
    #mask1 = cv2.inRange(hsv ,lower_range ,upper_range)
    
   
    imgray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    
    ret, thresh = cv2.threshold(edges, 127, 255,0)
    
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(cv_image, contours, 1 , (0,0,255), 3)
    
    cv2.imshow('image', cv_image)

    cv2.imshow('mask', edges)
    
    cv2.waitKey(0) 
    
    cv2.destroyAllWindows()
    
def get_image():

    rospy.init_node('lane_detector', anonymous=True)
    rospy.Subscriber("/camera/rgb/image_raw", Image, callback)
    rospy.spin()
    
if __name__ == '__main__':
	
       get_image()