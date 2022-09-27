from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():

    robot_monitor = Node(
        package='rqt_robot_monitor',
        executable='rqt_robot_monitor',
        output='screen')

    ld = LaunchDescription()
    ld.add_action(robot_monitor)
    return ld