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

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

from launch_pal.arg_utils import LaunchArgumentsBase

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    pass


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    pkg_share_directory = get_package_share_directory(
        'tiago_dual_controller_configuration')

    controller_config = os.path.join(
        pkg_share_directory,
        'config', 'gravity_compensation_controller.yaml')
    gravity_spawner_node = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            "gravity_compensation_controller", "--param-file", controller_config, "--inactive"],
    )
    launch_description.add_action(gravity_spawner_node)

    return


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
