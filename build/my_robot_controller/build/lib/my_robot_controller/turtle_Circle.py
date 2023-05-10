#!/usr/bin/env python3 

import rclpy 
from rclpy.node import Node 
from turtlesim.msg import Pose 
from geometry_msgs.msg import Twist 
import math 
# from turtle_control import TurtleControllerNode

class traingle(Node):
    def __init__(self):
        super().__init__("turtle_controller") 
        self.length_y = 3.0
        self.theta = math.pi
        self.pose_ = None 
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10) 
        self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10) 
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop) 
    def callback_turtle_pose(self,msg): 
        self.pose_ = msg 

    def control_loop(self): 
      if self.pose_ == None: 

            return 

      msg = Twist() 
      msg.linear.x = self.length_y
      msg.angular.z = self.theta
      self.cmd_vel_publisher_.publish(msg)
 


def main(args=None):
    rclpy.init(args=args)
    tri = traingle()
    rclpy.spin(tri)
    rclpy.shutdown()

if __name__=="__main__":
    main()
