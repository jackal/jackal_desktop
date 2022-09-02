from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_jackal_viz = FindPackageShare('jackal_viz')

    config_arg = DeclareLaunchArgument(
        name='config',
        default_value='slam.rviz',
    )

    rviz_config = PathJoinSubstitution(
        [pkg_jackal_viz, 'rviz', LaunchConfiguration('config')]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config]
    )

    ld = LaunchDescription()
    ld.add_action(config_arg)
    ld.add_action(rviz_node)
    return ld
