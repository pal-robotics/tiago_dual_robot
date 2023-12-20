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

from typing import List
import os
from dataclasses import dataclass
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import OpaqueFunction, GroupAction
from launch.conditions import IfCondition, LaunchConfigurationNotEquals
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_pal.arg_utils import read_launch_argument
from launch_pal.param_utils import merge_param_files
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.include_utils import include_scoped_launch_py_description


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    pass


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    pkg_share_folder = get_package_share_directory(
        'tiago_dual_controller_configuration')

    # Mobile base controller
    default_config = os.path.join(
        pkg_share_folder,
        'config', 'mobile_base_controller.yaml')

    calibration_config = '/etc/calibration/master_calibration.yaml'

    if os.path.exists(calibration_config):
        params_file = merge_param_files([default_config, calibration_config])
    else:
        params_file = default_config

    mobile_base_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='mobile_base_controller',
            controller_type='diff_drive_controller/DiffDriveController',
            controller_params_file=params_file)
         ],
        forwarding=False)

    launch_description.add_action(mobile_base_controller)

    # Joint state broadcaster
    joint_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_state_broadcaster',
            controller_type='joint_state_broadcaster/JointStateBroadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_state_broadcaster.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(joint_state_broadcaster)

    # Torso controller
    torso_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='torso_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'torso_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(torso_controller)

    # Head controller
    head_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='head_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'head_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(head_controller)

    # Add controller of right arm, end-effector and ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['right']))

    # Add controller of left arm, end-effector and ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['left']))

    return


def configure_side_controllers(context, end_effector_side='right', *args, **kwargs):

    pkg_share_folder = get_package_share_directory(
        'tiago_dual_controller_configuration')

    end_effector_arg_name = concatenate_strings(
        strings=['end_effector', end_effector_side],
        delimiter='_',
        skip_empty=True)

    arm_arg_name = concatenate_strings(
        strings=['arm_type', end_effector_side],
        delimiter='_',
        skip_empty=True)

    ft_sensor_arg_name = concatenate_strings(
        strings=['ft_sensor', end_effector_side],
        delimiter='_',
        skip_empty=True)

    # Setup arm controller
    arm_controller_name = concatenate_strings(
        strings=['arm', end_effector_side, 'controller'],
        delimiter='_',
        skip_empty=True)

    arm_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name=arm_controller_name,
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', f'{arm_controller_name}.yaml'))
         ],
        forwarding=False,
        condition=LaunchConfigurationNotEquals(arm_arg_name, 'no-arm'))

    end_effector = read_launch_argument(end_effector_arg_name, context)
    end_effector_underscore = end_effector.replace('-', '_')

    end_effector_controller = include_scoped_launch_py_description(
        pkg_name=f'{end_effector_underscore}_controller_configuration',
        paths=['launch', f'{end_effector_underscore}_controller.launch.py'],
        launch_arguments={"side": end_effector_side},
        condition=IfCondition(
            PythonExpression(
                ["'", LaunchConfiguration(arm_arg_name), "' != 'no-arm' and '",
                 LaunchConfiguration(end_effector_arg_name), "' != 'no-end-effector'"]
            )
        ))

    # Setup ft-sensor controller
    ft_sensor_controller_name = concatenate_strings(
        strings=['ft_sensor', end_effector_side, 'controller'],
        delimiter='_',
        skip_empty=True)

    ft_sensor_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name=ft_sensor_controller_name,
            controller_type='force_torque_sensor_broadcaster/ForceTorqueSensorBroadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', f'{ft_sensor_controller_name}.yaml'))
         ],
        forwarding=False,
        condition=IfCondition(
            PythonExpression(
                ["'", LaunchConfiguration(arm_arg_name), "' != 'no-arm' and '",
                 LaunchConfiguration(ft_sensor_arg_name), "' != 'no-ft-sensor'"]
            )
        ))

    return [arm_controller, end_effector_controller, ft_sensor_controller]


def concatenate_strings(strings: List[str], delimiter: str = '', skip_empty: bool = False):

    concatenated_string = ''

    if skip_empty:
        concatenated_string = delimiter.join(filter(None, strings))
    else:
        concatenated_string = delimiter.join(strings)

    return concatenated_string
