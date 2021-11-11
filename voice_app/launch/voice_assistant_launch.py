from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='voice_app',
            executable='iat_publish',
            name='iat_publish'
        ),
        Node(
            package='voice_app',
            executable='voice_assistant',
            name='voice_assistant'
        )
    ])
