#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import PoseStamped
from time import sleep

def set_ir():
    
    x = [2.0, 1.0, -1.5, 1.5]
    y = [0.5, -1.5, -0.5, 2.0]
    theta = [1.57, 2.14, -1.32, 0.0]

    ir = []

    for i in range(4):
        ir.append(PoseStamped())
        ir[i].header.frame_id = 'map'
        ir[i].pose.position.x = x[i]
        ir[i].pose.position.y = y[i]

        quat = quaternion_from_euler(0, 0, theta[i])
        ir[i].pose.orientation.x = quat[0]
        ir[i].pose.orientation.y = quat[1]
        ir[i].pose.orientation.z = quat[2]
        ir[i].pose.orientation.w = quat[3]

    return ir

def talker_principal(ir):
    
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rate = rospy.Rate(4)
    
    
    if not rospy.is_shutdown():

        rospy.loginfo(ir)
        pub.publish(ir)
        rate.sleep()
        rospy.loginfo(ir) 
        pub.publish(ir)



def listener_callback(data):

    global status
    status = data.status.status



    
          
if __name__ == '__main__':
        
    status = 0
    poses = set_ir()
    rospy.init_node('pose_goal')
    
    for i in range(4):

        talker_principal(poses[i])
        sleep(4)

