import launch 
import launch_ros.actions 
import os
def generate_launch_description():

    # Define the path to the package containing the nodes
    package_path = os.path.join(('/home/sumukha/ros2_ws/src/my_robot_controller/my_robot_controller/pub.py'),('/home/sumukha/ros2_ws/src/my_robot_controller/my_robot_controller/subscriber.py'),('my_package'), 'launch')

    # Declare the publisher node
    publisher_node = launch_ros.actions.Node(
        package='my_robot_controller',
        executable='Pub_node',
        name='publisher'
    )

    # Declare the subscriber node
    subscriber_node = launch_ros.actions.Node(
        package='my_robot_controller',
        executable='sub_node',
        name='subscriber'
    )

    # Group the nodes together
    nodes = [publisher_node, subscriber_node]

    # Create the launch description with the list of nodes
    ld = launch.LaunchDescription(nodes)

    return ld