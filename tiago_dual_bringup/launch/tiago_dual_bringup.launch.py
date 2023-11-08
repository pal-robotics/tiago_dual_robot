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

from launch import LaunchDescription
from launch_pal.include_utils import include_scoped_launch_py_description


def generate_launch_description():

    # @TODO: robot pose publisher
    # @TODO: tf lookup
    # @TODO: dynamic footprint

    # Create the launch description and populate
    ld = LaunchDescription()

    declare_launch_arguments(ld)
    declare_actions(ld)

    return ld


def declare_launch_arguments(launch_description: LaunchDescription):
    return


def declare_actions(launch_description: LaunchDescription):

    default_controllers = include_scoped_launch_py_description(
        pkg_name='tiago_dual_controller_configuration',
        paths=['launch', 'default_controllers.launch.py'])

    launch_description.add_action(default_controllers)

    play_motion2 = include_scoped_launch_py_description(
        pkg_name='tiago_dual_bringup',
        paths=['launch', 'tiago_dual_play_motion2.launch.py'])

    launch_description.add_action(play_motion2)

    twist_mux = include_scoped_launch_py_description(
        pkg_name='tiago_dual_bringup',
        paths=['launch', 'twist_mux.launch.py'])

    launch_description.add_action(twist_mux)

    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name='tiago_dual_description',
        paths=['launch', 'robot_state_publisher.launch.py'])

    launch_description.add_action(robot_state_publisher)

    return
