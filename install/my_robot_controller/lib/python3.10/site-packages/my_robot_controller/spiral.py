#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose 
from geometry_msgs.msg import Twist 
from turtlesim.srv import Spawn
from functools import partial
import math 
import random
import time

class spiral(Node):
    def __init__(self):
        super().__init__("Spiral_Motion")
        self.velocity_publisher_ = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.pose_subscriber_ = self.create_subscription(Pose,"/turtle/pose",self.pose_callback,10)
        self.pose_x = 0
        self.pose_y = 0
        self.timer_=self.create_timer(1.0, self.publish_velocity)
        self.get_logger().info("Turtle is doing spiral...enjoy")
        self.radius = 2.0

    def pose_callback(self,pose_msg=Pose()):
        self.pose_x = pose_msg.x
        self.pose_y = pose_msg.y

        if(round(self.pose_y)==8.0):
            self.get_logger().warn("About to hit wall!")

    def publish_velocity(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.radius

        if self.pose_x < 10.0 and self.pose_y < 10.0:
            vel_msg.angular.z = 22/7
            self.radius += 0.2
        else:
            vel_msg.angular.z = 0.0
            vel_msg.linear.x = 0.0

            self.get_logger().info("done rotation...")
            self.timer_.cancel()

        self.velocity_publisher_.publish(vel_msg)

def main(args=None):
    rclpy.init(args=args)
    node = spiral()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__": 

     main() 