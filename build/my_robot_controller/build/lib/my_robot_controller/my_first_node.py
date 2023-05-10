#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class create_node(Node):
    def __init__(self):
        super().__init__("First_Node")
        self.get_logger().info("Hello from ROS2, Node is Started")
        self.timer_ = self.create_timer(1.0,self.timer_callback)
    
    def timer_callback(self):
        self.get_logger().info("Hello Sumukha")



def main(args=None):
    rclpy.init(args=args)
    node = create_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
   main()