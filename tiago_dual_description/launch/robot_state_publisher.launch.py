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
from launch.actions import DeclareLaunchArgument, OpaqueFunction

from launch_pal.arg_utils import read_launch_argument
from launch_param_builder import load_xacro
from launch_ros.actions import Node


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()

    launch_args = declare_launch_arguments()

    for arg in launch_args.values():
        ld.add_action(arg)

    declare_actions(ld, launch_args)

    return ld


def declare_launch_arguments() -> Dict:
    arg_dict = {}

    use_sim_time = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use simulation time')

    arg_dict[use_sim_time.name] = use_sim_time

    robot_name = DeclareLaunchArgument(
        'robot_name',
        default_value='tiago_dual',
        description='Name of the robot. ',
        choices=['pmb2', 'tiago', 'pmb3', 'tiago_dual'])

    arg_dict[robot_name.name] = robot_name

    arm_right = DeclareLaunchArgument(
        'arm_type_right',
        default_value='tiago-arm',
        description='Which type of the right arm.',
        choices=['no-arm', 'tiago-arm', 'sea'])

    arg_dict[arm_right.name] = arm_right

    arm_left = DeclareLaunchArgument(
        'arm_type_left',
        default_value='tiago-arm',
        description='Which type of the left arm.',
        choices=['no-arm', 'tiago-arm', 'sea'])

    arg_dict[arm_left.name] = arm_left

    end_effector_right = DeclareLaunchArgument(
        'end_effector_right',
        default_value='pal-gripper',
        description='End effector model of the right arm.',
        choices=['pal-gripper', 'pal-hey5', 'custom', 'no-end-effector'])

    arg_dict[end_effector_right.name] = end_effector_right

    end_effector_left = DeclareLaunchArgument(
        'end_effector_left',
        default_value='pal-gripper',
        description='End effector model of the left arm.',
        choices=['pal-gripper', 'pal-hey5', 'custom', 'no-end-effector'])

    arg_dict[end_effector_left.name] = end_effector_left

    ft_sensor_right = DeclareLaunchArgument(
        'ft_sensor_right',
        default_value='schunk-ft',
        description='FT sensor model. ',
        choices=['schunk-ft', 'no-ft-sensor'])

    arg_dict[ft_sensor_right.name] = ft_sensor_right

    ft_sensor_left = DeclareLaunchArgument(
        'ft_sensor_left',
        default_value='schunk-ft',
        description='FT sensor model. ',
        choices=['schunk-ft', 'no-ft-sensor'])

    arg_dict[ft_sensor_left.name] = ft_sensor_left

    wrist_model_right = DeclareLaunchArgument(
        'wrist_model_right',
        default_value='wrist-2010',
        description='Wrist model. ',
        choices=['wrist-2010', 'wrist-2017'])

    arg_dict[wrist_model_right.name] = wrist_model_right

    wrist_model_left = DeclareLaunchArgument(
        'wrist_model_left',
        default_value='wrist-2010',
        description='Wrist model. ',
        choices=['wrist-2010', 'wrist-2017'])

    arg_dict[wrist_model_left.name] = wrist_model_left

    camera_model = DeclareLaunchArgument(
        'camera_model',
        default_value='orbbec-astra',
        description='Head camera model. ',
        choices=['no-camera', 'orbbec-astra', 'orbbec-astra-pro', 'asus-xtion'])

    arg_dict[camera_model.name] = camera_model

    laser_model = DeclareLaunchArgument(
        'laser_model',
        default_value='sick-571',
        description='Base laser model. ',
        choices=['no-laser', 'sick-571', 'sick-561', 'sick-551', 'hokuyo'])

    arg_dict[laser_model.name] = laser_model

    return arg_dict


def declare_actions(launch_description: LaunchDescription, launch_args: Dict):

    launch_description.add_action(OpaqueFunction(
        function=create_robot_description_param))

    return


# def declare_args(context, *args, **kwargs):

#     sim_time_arg = DeclareLaunchArgument(
#         'use_sim_time', default_value='true',
#         description='Use simulation time')

#     robot_name = read_launch_argument('robot_name', context)

#     return [get_arm(robot_name),
#             get_camera_model(robot_name),
#             get_end_effector(robot_name),
#             get_ft_sensor(robot_name),
#             get_laser_model(robot_name),
#             get_wrist_model(robot_name),
#             sim_time_arg]


def create_robot_description_param(context, *args, **kwargs):

    robot_description = {'robot_description': load_xacro(
        Path(os.path.join(
            get_package_share_directory('tiago_dual_description'),
            'robots', 'tiago_dual.urdf.xacro')),
        {
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
            'use_sim': read_launch_argument('use_sim_time', context),
        }
    )}

    rsp = Node(package='robot_state_publisher',
               executable='robot_state_publisher',
               output='both',
               parameters=[robot_description])

    return [rsp]


# def generate_launch_description():

#     ld = LaunchDescription()

#     # Declare arguments
#     # we use OpaqueFunction so the callbacks have access to the context
#     ld.add_action(get_robot_name('tiago'))
#     ld.add_action(OpaqueFunction(function=declare_args))

#     # Execute robot_state_publisher node
#     ld.add_action(OpaqueFunction(function=launch_setup))

#     return ld
