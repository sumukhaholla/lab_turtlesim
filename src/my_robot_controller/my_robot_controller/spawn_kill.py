#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose 
from geometry_msgs.msg import Twist 
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from functools import partial
import math 
import random
import time

class spawn_kill(Node):
    def __init__(self):
        super().__init__("Turtle_Kill")
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10) 
        self.pose_1 = self.create_subscription(Pose,'/turtle1/pose',self.pose01_callback,10)
        self.pose_2 = self.create_subscription(Pose,'/turtle2/pose',self.pose02_callback,10)
        self.pose1 = None
        self.pose2 = None
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop) 

    def pose01_callback(self,msg):
        self.pose1= msg
    def pose02_callback(self,msg02):
        self.pose2 = msg02

    def control_loop(self):
        if self.pose1 == None and self.pose2 == None:
            return    
        dist_x = self.pose2.x - self.pose1.x

        dist_y = self.pose2.y - self.pose1.y 

        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y) 
  
        msg = Twist()  
        if distance > 0.2:
            msg.linear.x = distance 
            goal_theta = math.atan2(dist_y, dist_x) 
            diff = goal_theta - self.pose1.theta 
            if diff > math.pi: 

                diff -= 2*math.pi 

            elif diff < -math.pi: 

                diff += 2*math.pi 

            msg.angular.z = diff 
                       
            # time.sleep(1)
        else:
            msg.angular.z = 0.0
            msg.linear.x = 0.0
            # self.cmd_vel_publisher_.publish(msg)
            # time.sleep(2)
            self.callback_kill('turtle2') # Put name of the second spawned turtle....
        self.cmd_vel_publisher_.publish(msg) 
       # time.sleep(5)
        


    def callback_kill(self, name):
        client = self.create_client(Kill,"/kill")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for sevice....")
        
        request = Kill.Request()
        request.name = name

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_kill_it))

    def callback_kill_it(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e,))
 
def main(args=None):
    rclpy.init(args=args)
    node_a = spawn_kill()
    rclpy.spin(node_a)
    rclpy.shutdown()

if __name__=="__main__":
    main()