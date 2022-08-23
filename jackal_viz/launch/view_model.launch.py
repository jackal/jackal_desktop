from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_jackal_description = FindPackageShare('jackal_description')
    pkg_jackal_viz = FindPackageShare('jackal_viz')

    rviz_config = PathJoinSubstitution(
        [pkg_jackal_viz, 'rviz', 'model.rviz']
    )

    description_launch = IncludeLaunchDescription(
        PathJoinSubstitution([
            pkg_jackal_description,
            'launch',
            'description.launch.py'])
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config]
    )

    ld = LaunchDescription()
    ld.add_action(joint_state_publisher_gui_node)
    ld.add_action(description_launch)
    ld.add_action(rviz_node)
    return ld
