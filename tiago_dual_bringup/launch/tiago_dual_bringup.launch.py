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

from typing import Dict

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_pal.include_utils import include_scoped_launch_py_description


def generate_launch_description():

    # @TODO: robot pose publisher
    # @TODO: tf lookup
    # @TODO: dynamic footprint

    # Create the launch description and populate
    ld = LaunchDescription()

    launch_args = declare_launch_arguments()

    for arg in launch_args.values():
        ld.add_action(arg)

    declare_actions(ld, launch_args)

    return ld


def declare_launch_arguments() -> Dict:

    arg_dict = {}

    sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='False',
        description='Use sim time. ')

    arg_dict[sim_time_arg.name] = sim_time_arg

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

    return arg_dict


def declare_actions(launch_description: LaunchDescription, launch_args: Dict):

    default_controllers = include_scoped_launch_py_description(
        pkg_name='tiago_dual_controller_configuration',
        paths=['launch', 'default_controllers.launch.py'])

    launch_description.add_action(default_controllers)

    play_motion2 = include_scoped_launch_py_description(
        pkg_name='tiago_dual_bringup',
        paths=['launch', 'tiago_dual_play_motion2.launch.py'],
        launch_args=[launch_args["robot_name"],
                     launch_args["arm_type_right"],
                     launch_args["arm_type_left"],
                     launch_args["end_effector_right"],
                     launch_args["end_effector_left"],
                     launch_args["ft_sensor_right"],
                     launch_args["ft_sensor_left"]],
        launch_configurations={"robot_name": LaunchConfiguration("robot_name"),
                               "arm_type_right": LaunchConfiguration("arm_type_right"),
                               "arm_type_left": LaunchConfiguration("arm_type_left"),
                               "end_effector_right": LaunchConfiguration("end_effector_right"),
                               "end_effector_left": LaunchConfiguration("end_effector_left"),
                               "ft_sensor_right": LaunchConfiguration("ft_sensor_right"),
                               "ft_sensor_left": LaunchConfiguration("ft_sensor_left")})

    launch_description.add_action(play_motion2)

    twist_mux = include_scoped_launch_py_description(
        pkg_name='tiago_dual_bringup',
        paths=['launch', 'twist_mux.launch.py'],
    )

    launch_description.add_action(twist_mux)

    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name='tiago_dual_description',
        paths=['launch', 'robot_state_publisher.launch.py'],
        launch_args=[launch_args['use_sim_time']],
        launch_configurations={'use_sim_time': 'True'})

    # launch_configurations={'use_sim_time': LaunchConfiguration('use_sim_time')})

    launch_description.add_action(robot_state_publisher)

    return
