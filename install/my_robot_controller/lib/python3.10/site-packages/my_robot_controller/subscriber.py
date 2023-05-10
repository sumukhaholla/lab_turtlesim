#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String

class subscriber(Node):
     def __init__(self):
          super().__init__("Subscriber")
          self.get_logger().info("Hello from subscriber...please subscribe to my channel")
          self.counter=0
          self.publisher_ = self.create_publisher(Int32,"/msg_count",10)
          self.subscribe_=self.create_subscription(Int32, "/message",self.subscriber_callback,10)

     def subscriber_callback(self,msg):
         msg_a = Int32()
         msg_int = int(msg.data)
         self.get_logger().info(str(msg.data))
         #msg_a.data = str(msg)+"Hello_Sumukha " + str(self.counter)
         msg_a.data = msg_int + self.counter
         self.publisher_.publish(msg_a)
         self.counter+=1

def main(args=None):
  rclpy.init(args=args)
  node = subscriber()
  rclpy.spin(node)
  rclpy.shutdown()


if __name__=="__main__":
   main()