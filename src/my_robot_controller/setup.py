import os
from setuptools import setup
from glob import glob
package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sumukha',
    maintainer_email='sumukha@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = my_robot_controller.my_first_node:main",
            "Pub_node = my_robot_controller.pub:main",
            "sub_node=my_robot_controller.subscriber:main",
            "turtle_control=my_robot_controller.turtle_control:main",
            "circle=my_robot_controller.turtle_Circle:main",
            "traingle=my_robot_controller.turtle_Traingle:main",
            "node=my_robot_controller.three_node:main",
            "node01 = my_robot_controller.spawn:main",
            "spawn_killer = my_robot_controller.spawn_kill:main",
            "spiral = my_robot_controller.spiral:main",
            "square = my_robot_controller.square:main"
        ],
    },
)
