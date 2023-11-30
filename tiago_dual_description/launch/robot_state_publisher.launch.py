# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
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
from pathlib import Path
from typing import Dict

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_param_builder import load_xacro
from launch_pal.arg_utils import read_launch_argument
from launch_pal.arg_utils import LaunchArgumentsBase, launch_arg_factory
from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentDeclaration(LaunchArgumentsBase):
    use_sim_time: DeclareLaunchArgument = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='False',
        description='Use simulation time')
    namespace: DeclareLaunchArgument = DeclareLaunchArgument(
        name='namespace',
        default_value='',
        description='Define namespace of the robot. ')


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
        function=create_robot_description_param))

    rsp = Node(package='robot_state_publisher',
               executable='robot_state_publisher',
               output='both',
               parameters=[{'robot_description': LaunchConfiguration('robot_description')
                            }])

    launch_description.add_action(rsp)

    return


def create_robot_description_param(context, *args, **kwargs):

    xacro_file_path = Path(os.path.join(
        get_package_share_directory('tiago_dual_description'),
        'robots', 'tiago_dual.urdf.xacro'))

    xacro_input_args = {
        'arm_right': read_launch_argument('arm_type_right', context),
        'arm_left': read_launch_argument('arm_type_left', context),
        'camera_model': read_launch_argument('camera_model', context),
        'end_effector_right': read_launch_argument('end_effector_right', context),
        'end_effector_left': read_launch_argument('end_effector_left', context),
        'ft_sensor_right': read_launch_argument('ft_sensor_right', context),
        'ft_sensor_left': read_launch_argument('ft_sensor_left', context),
        'laser_model': read_launch_argument('laser_model', context),
        'wrist_model_right': read_launch_argument('wrist_model_right', context),
        'wrist_model_left': read_launch_argument('wrist_model_left', context),
        'has_screen': read_launch_argument('has_screen', context),
        'base_type': read_launch_argument('base_type', context),
        'use_sim': read_launch_argument('use_sim_time', context),
        'namespace': read_launch_argument('namespace', context),
    }
    robot_description = load_xacro(xacro_file_path, xacro_input_args)

    return [SetLaunchConfiguration('robot_description', robot_description)]
