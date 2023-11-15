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
from typing import Dict
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import read_launch_argument
from tiago_dual_description.tiago_dual_launch_utils import get_tiago_dual_hw_suffix
from launch_pal.param_utils import merge_param_files


def generate_launch_description():

    ld = LaunchDescription()

    declare_launch_arguments(ld)
    declare_actions(ld)
    return ld


def declare_launch_arguments(launch_description: LaunchDescription):

    sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='False',
        description='Use sim time. ')

    launch_description.add_action(sim_time_arg)

    robot_name = DeclareLaunchArgument(
        'robot_name',
        default_value='tiago_dual',
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

    return


def declare_actions(launch_description: LaunchDescription):

    # TODO: Update the param files for the motions so they can be read correctly

    play_motion2 = include_scoped_launch_py_description(
        pkg_name='play_motion2',
        paths=['launch', 'play_motion2.launch.py'],
        launch_configurations={
            "use_sim_time":  LaunchConfiguration('use_sim_time'),
            "play_motion2_config": LaunchConfiguration('play_motion2_config')
        })

    launch_description.add_action(OpaqueFunction(
        function=create_play_motion_filename))
    launch_description.add_action(play_motion2)

    return


def create_play_motion_filename(context):

    hw_suffix = get_tiago_dual_hw_suffix(
        arm_right=read_launch_argument('arm_type_right', context),
        arm_left=read_launch_argument('arm_type_left', context),
        end_effector_right=read_launch_argument('end_effector_right', context),
        end_effector_left=read_launch_argument('end_effector_left', context),
        ft_sensor_right=read_launch_argument('ft_sensor_right', context),
        ft_sensor_left=read_launch_argument('ft_sensor_left', context),
    )

    gripper_specific_file = f"tiago_motions_{hw_suffix}.yaml"

    gripper_specific_yaml = PathJoinSubstitution(
        [get_package_share_directory('tiago_dual_bringup'),
         'config', 'motions', gripper_specific_file])

    base_motions_file = 'tiago_motions_general.yaml'

    if read_launch_argument('arm_type_right', context) == 'no-arm':
        base_motions_file = 'tiago_motions_general_arm_left.yaml'

    if read_launch_argument('arm_type_left', context) == 'no-arm':
        base_motions_file = 'tiago_motions_general_arm_right.yaml'

    base_motions_yaml = PathJoinSubstitution([get_package_share_directory(
        'tiago_dual_bringup'), 'config', 'motions', base_motions_file])

    combined_yaml = merge_param_files(
        [base_motions_yaml.perform(context), gripper_specific_yaml.perform(context)])

    return [SetLaunchConfiguration("play_motion2_config", combined_yaml)]
