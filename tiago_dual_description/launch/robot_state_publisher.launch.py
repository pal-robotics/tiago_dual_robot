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

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_param_builder import load_xacro
from launch_pal.arg_utils import read_launch_argument
from launch_pal.arg_utils import LaunchArgumentsBase
from dataclasses import dataclass
from launch_pal.robot_arguments import TiagoDualArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    base_type: DeclareLaunchArgument = TiagoDualArgs.base_type
    arm_type_right: DeclareLaunchArgument = TiagoDualArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoDualArgs.arm_type_left
    end_effector_right: DeclareLaunchArgument = TiagoDualArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoDualArgs.end_effector_left
    ft_sensor_right: DeclareLaunchArgument = TiagoDualArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = TiagoDualArgs.ft_sensor_left
    wrist_model_right: DeclareLaunchArgument = TiagoDualArgs.wrist_model_right
    wrist_model_left: DeclareLaunchArgument = TiagoDualArgs.wrist_model_left
    camera_model: DeclareLaunchArgument = TiagoDualArgs.camera_model
    laser_model: DeclareLaunchArgument = TiagoDualArgs.laser_model
    has_screen: DeclareLaunchArgument = TiagoDualArgs.has_screen

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
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

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
