#!/usr/bin/env python3 

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Int32
import math 
import time


class three_node(Node):
    def __init__(self):        
      super().__init__("Three_node")
      self.get_logger().info("Node has been started....")
      self.counter = 0
    #   self.timer_ = self.create_timer(1.0,self.timer_callback)## This is timer for publishing.....Hello String....
      self.subscribe_=self.create_subscription(Int32, "/msg_count",self.subscriber_callback,10) ### Created subscriber that subscribes to same topic.. 
      ## called /message topic

    def subscriber_callback(self,msg_a):## Subscribed callback function....where Hello String is available....
      self.get_logger().info(str(msg_a.data))


def main(args=None):
    rclpy.init(args=args)
    node = three_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()