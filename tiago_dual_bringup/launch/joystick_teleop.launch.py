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
from launch.actions import DeclareLaunchArgument, OpaqueFunction, SetLaunchConfiguration
from launch.conditions import LaunchConfigurationEquals
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

from launch_pal.arg_utils import read_launch_argument

from tiago_dual_description.tiago_dual_launch_utils import get_tiago_dual_hw_suffix
from launch_pal.arg_utils import LaunchArgumentsBase, launch_arg_factory
from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentDeclaration(LaunchArgumentsBase):
    cmd_vel: DeclareLaunchArgument = DeclareLaunchArgument(
        name='cmd_vel',
        default_value='input_joy/cmd_vel',
        description='Joystick cmd_vel topic')


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    robot_name = "tiago_dual"
    has_robot_config = True
    custom_args = ArgumentDeclaration()
    launch_args = launch_arg_factory(custom_args,
                                     has_robot_config=has_robot_config, robot_name=robot_name)

    launch_args.add_to_launch_description(ld)

    declare_actions(ld, launch_args)

    return ld


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArgumentsBase):

    launch_description.add_action(OpaqueFunction(
        function=create_joy_teleop_filename))

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

    joy_teleop_config = SetLaunchConfiguration(
        'teleop_config', joy_teleop_path)
    return [joy_teleop_config]
