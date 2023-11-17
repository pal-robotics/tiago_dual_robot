# Copyright (c) 2022 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import Node, DeclareLaunchArgument, OpaqueFunction
from launch.conditions import LaunchConfigurationEquals
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

from launch_pal.arg_utils import read_launch_argument

from tiago_dual_description.tiago_dual_launch_utils import get_tiago_dual_hw_suffix


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()

    declare_launch_arguments(ld)
    declare_actions(ld)

    return ld


def declare_launch_arguments(launch_description: LaunchDescription):

    robot_name = DeclareLaunchArgument(
        'robot_name',
        # default_value='tiago_dual',
        description='Name of the robot. ',
        choices=['pmb2', 'tiago', 'pmb3', 'tiago_dual'])

    launch_description.add_action(robot_name)

    arm_right = DeclareLaunchArgument(
        'arm_type_right',
        default_value='tiago-arm',
        description='Which type of the right arm.',
        choices=['no-arm', 'tiago-arm', 'sea'])

    launch_description.add_action(arm_right)

    arm_left = DeclareLaunchArgument(
        'arm_type_left',
        default_value='tiago-arm',
        description='Which type of the left arm.',
        choices=['no-arm', 'tiago-arm', 'sea'])

    launch_description.add_action(arm_left)

    end_effector_right = DeclareLaunchArgument(
        'end_effector_right',
        default_value='pal-gripper',
        description='End effector model of the right arm.',
        choices=['pal-gripper', 'pal-hey5', 'custom', 'no-end-effector'])

    launch_description.add_action(end_effector_right)

    end_effector_left = DeclareLaunchArgument(
        'end_effector_left',
        default_value='pal-gripper',
        description='End effector model of the left arm.',
        choices=['pal-gripper', 'pal-hey5', 'custom', 'no-end-effector'])

    launch_description.add_action(end_effector_left)

    ft_sensor_right = DeclareLaunchArgument(
        'ft_sensor_right',
        default_value='schunk-ft',
        description='FT sensor model. ',
        choices=['schunk-ft', 'no-ft-sensor'])

    launch_description.add_action(ft_sensor_right)

    ft_sensor_left = DeclareLaunchArgument(
        'ft_sensor_left',
        default_value='schunk-ft',
        description='FT sensor model. ',
        choices=['schunk-ft', 'no-ft-sensor'])

    launch_description.add_action(ft_sensor_left)

    cmd_val = DeclareLaunchArgument(
        'cmd_vel', default_value='input_joy/cmd_vel',
        description='Joystick cmd_vel topic')

    launch_description.add_action(cmd_val)

    launch_description.add_action(OpaqueFunction(
        function=create_joy_teleop_filename))

    return


def declare_actions(launch_description: LaunchDescription):

    joy_teleop_node = Node(
        package='joy_teleop',
        executable='joy_teleop',
        parameters=[LaunchConfiguration('teleop_config')],
        remappings=[('cmd_vel', LaunchConfiguration('cmd_vel'))])

    launch_description.add_action(joy_teleop_node)

    pkg_dir = get_package_share_directory('tiago_dual_bringup')

    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joystick',
        parameters=[os.path.join(pkg_dir, 'config', 'joy_teleop', 'joy_config.yaml')])

    launch_description.add_action(joy_node)

    torso_incrementer_server = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer',
        namespace='torso_controller')

    launch_description.add_action(torso_incrementer_server)

    head_incrementer_server = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer',
        namespace='head_controller')

    launch_description.add_action(head_incrementer_server)

    gripper_incrementer_server = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer',
        namespace='gripper_right_controller',
        condition=LaunchConfigurationEquals('end_effector_right', 'pal-gripper'))

    launch_description.add_action(gripper_incrementer_server)

    return


def create_joy_teleop_filename(context):
    hw_suffix = get_tiago_dual_hw_suffix(
        arm_right=read_launch_argument('arm_type_right', context),
        arm_left=read_launch_argument('arm_type_left', context),
        end_effector_right=read_launch_argument('end_effector_right', context),
        end_effector_left=read_launch_argument('end_effector_left', context),
        ft_sensor_right=read_launch_argument('ft_sensor_right', context),
        ft_sensor_left=read_launch_argument('ft_sensor_left', context),
    )

    joy_teleop_file = f"joy_teleop_{hw_suffix}.yaml"

    joy_teleop_path = os.path.join(
        get_package_share_directory('tiago_dual_bringup'), 'config', 'joy_teleop', joy_teleop_file)

    joy_teleop_config = DeclareLaunchArgument(
        'teleop_config', default_value=joy_teleop_path,
        description='Joystick teleop configuration file')

    return [joy_teleop_config]
