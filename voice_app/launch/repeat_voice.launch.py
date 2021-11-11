import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'node_prefix',
            default_value=[launch.substitutions.EnvironmentVariable('USER'), '_'],
            description='Prefix for node names'),
        launch_ros.actions.Node(
            package='voice_app', executable='iat_publish', output='screen',
            name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'iat_publish']),
        launch_ros.actions.Node(
            package='voice_app', executable='tts_subscribe', output='screen',
            name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'tts_subscribe']),
    ])
