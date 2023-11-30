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
from launch.actions import DeclareLaunchArgument
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, launch_arg_factory
from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentDeclaration(LaunchArgumentsBase):
    use_sim_time: DeclareLaunchArgument = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='False',
        description='Use simulation time')


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

    pkg = get_package_share_directory('tiago_dual_bringup')

    config_locks_file = os.path.join(
        pkg, 'config', 'twist_mux', 'twist_mux_locks.yaml')
    config_topics_file = os.path.join(
        pkg, 'config', 'twist_mux', 'twist_mux_topics.yaml')
    joystick_file = os.path.join(pkg, 'config', 'twist_mux', 'joystick.yaml')

    twist_mux = include_scoped_launch_py_description(
        pkg_name='twist_mux', paths=['launch', 'twist_mux_launch.py'],
        launch_arguments={
            'cmd_vel_out': 'mobile_base_controller/cmd_vel_unstamped',
            'config_locks': config_locks_file,
            'config_topics': config_topics_file,
            'config_joy': joystick_file,
            'use_sim_time': launch_args.use_sim_time
        }
    )

    launch_description.add_action(twist_mux)

    return
