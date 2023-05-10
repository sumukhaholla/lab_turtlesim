#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose 
from geometry_msgs.msg import Twist 
from turtlesim.srv import Spawn
from functools import partial
import math 
import random


class spawn(Node):
    def __init__(self):
         super().__init__("node01") 
         self.get_logger().info("Hello Node started for spawn program...")
         # self.pose_subscriber = self.create_subscription(Pose,"/turtle1/pose",self.pose_callback, 10)
         self.client_for_spawn()


    def client_for_spawn(self,x = random.uniform(0.5,10),y = random.uniform(0.5,10),theta = 0.0):
         client = self.create_client(Spawn,"/spawn")
         while not client.wait_for_service(1.0):
             self.get_logger().warn("Waiting for service .....")
         request = Spawn.Request()
         request.x = x
         request.y = y
         request.theta = theta

         future = client.call_async(request)
    #      future.add_done_callback(partial(self.callback_spawn))

    # def callback_spwan(self,future):
    #      try:
    #          response = future.result()
    #      except Exception as e:
    #          self.get_logger().error("Service call failed: %r"%(e,))
        
def main(args=None):
    rclpy.init(args=args)
    # global node01
    node01 = spawn()
    rclpy.spin(node01)
    rclpy.shutdown()

if __name__=="__main__":
    main()