from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    config_arg = DeclareLaunchArgument(
        name="config",
        default_value="diagnostics",
    )
    rqt_dashboard_node = Node(
        package='rqt_gui',
        executable='rqt_gui',
        name='rqt_dashboard',
        arguments=['--perspective-file ', get_package_share_directory('jackal_viz'), '/rqt/', LaunchConfiguration('config'), '.perspective'],
        output='screen',
    )
    return LaunchDescription([
        config_arg,
        rqt_dashboard_node
    ])
