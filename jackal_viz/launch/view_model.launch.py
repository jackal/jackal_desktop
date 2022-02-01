from ament_index_python.packages import get_package_share_path
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    description_launch = IncludeLaunchDescription(str(get_package_share_path('jackal_description') / 'launch' / 'description.launch.py'))

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', str(get_package_share_path('jackal_viz') / 'rviz' / 'model.rviz')]
    )

    return LaunchDescription([joint_state_publisher_gui_node,
                              description_launch,
                              rviz_node,
                              ])
