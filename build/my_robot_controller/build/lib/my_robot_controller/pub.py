#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class publisher(Node):
    def __init__(self):
        super().__init__("Publsiher")
        self.get_logger().info("Hello from ROS2, Node is Started")
        # self.counter = 0
        self.publisher_ = self.create_publisher(Int32,"/message",10)
        self.timer_ = self.create_timer(1.0,self.timer_callback)
    def timer_callback(self): 
        msg = Int32()
        msg.data = 8    #"Hello " + str(self.counter)
        #self.get_logger().info(msg.data)
        self.publisher_.publish(msg)
        # self.counter+=1

def main(args=None):
    rclpy.init(args=args)
    node = publisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
   main()