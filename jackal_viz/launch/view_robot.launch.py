from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    config_arg = DeclareLaunchArgument(
        name="config",
        default_value="robot",
    )
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d ', get_package_share_directory('jackal_viz'), '/rviz/', LaunchConfiguration('config'), '.rviz'],
    )
    return LaunchDescription([
        config_arg,
        rviz_node
    ])
