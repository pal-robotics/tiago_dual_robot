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
from launch.actions import OpaqueFunction, GroupAction, SetLaunchConfiguration
from launch.conditions import IfCondition, LaunchConfigurationNotEquals
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_pal.param_utils import merge_param_files
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.include_utils import include_scoped_launch_py_description
from launch.actions import DeclareLaunchArgument
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs
from tiago_dual_description.launch_arguments import TiagoDualArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    base_type: DeclareLaunchArgument = TiagoDualArgs.base_type
    arm_type_right: DeclareLaunchArgument = TiagoDualArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoDualArgs.arm_type_left
    arm_motor_model_right: DeclareLaunchArgument = TiagoDualArgs.arm_motor_model_right
    arm_motor_model_left: DeclareLaunchArgument = TiagoDualArgs.arm_motor_model_left
    end_effector_right: DeclareLaunchArgument = TiagoDualArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoDualArgs.end_effector_left
    ft_sensor_right: DeclareLaunchArgument = TiagoDualArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = TiagoDualArgs.ft_sensor_left
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    namespace: DeclareLaunchArgument = CommonArgs.namespace


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    # Create the extra configs from the LAs
    launch_description.add_action(OpaqueFunction(function=create_base_configs))

    pkg_share_folder = get_package_share_directory(
        'tiago_dual_controller_configuration')

    # Base controller
    base_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="mobile_base_controller",
                controller_params_file=LaunchConfiguration("base_params"),
            )
        ]
    )
    launch_description.add_action(base_controller)

    # Joint state broadcaster
    joint_state_broadcaster = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="joint_state_broadcaster",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "joint_state_broadcaster.yaml"
                ),

            )
        ],
    )
    launch_description.add_action(joint_state_broadcaster)

    # IMU sensor broadcaster
    imu_sensor_broadcaster = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name='imu_sensor_broadcaster',
                controller_params_file=os.path.join(
                    pkg_share_folder, 'config', 'imu_sensor_broadcaster.yaml'))

        ],
    )
    launch_description.add_action(imu_sensor_broadcaster)

    # Torso controller
    torso_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name='torso_controller',
                controller_params_file=os.path.join(
                    pkg_share_folder,
                    'config', 'torso_controller.yaml')
            )
        ],
    )
    launch_description.add_action(torso_controller)

    # Head controller
    head_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name='head_controller',
                controller_params_file=os.path.join(
                    get_package_share_directory('tiago_controller_configuration'),
                    'config', 'head_controller.yaml'))
        ],
    )
    launch_description.add_action(head_controller)

    # Gravity compensation controller
    gravity_compensation_controller = GroupAction(
        [
            include_scoped_launch_py_description(
                pkg_name="tiago_dual_controller_configuration",
                paths=['launch', "gravity_compensation_controller.launch.py"],
                launch_arguments={"arm_motor_model_right": launch_args.arm_motor_model_right,
                                  "arm_motor_model_left": launch_args.arm_motor_model_left,
                                  "end_effector_right": launch_args.end_effector_right,
                                  "end_effector_left": launch_args.end_effector_left},
            )
        ]
    )

    launch_description.add_action(gravity_compensation_controller)

    # Add controller of right arm, end-effector and ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['right']))

    # Add controller of left arm, end-effector and ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['left']))

    return


def create_base_configs(context, *args, **kwargs):

    base_launch_configs = []
    base_type = read_launch_argument("base_type", context)
    is_public_sim = read_launch_argument("is_public_sim", context)

    base_share_pkg_folder = get_package_share_directory(base_type + "_controller_configuration")
    base_params = base_share_pkg_folder + "/config/mobile_base_controller.yaml"

    if is_public_sim and (base_type == "pmb2"):
        base_params = base_share_pkg_folder + "/config/mobile_base_controller_public_sim.yaml"

    calibration_config = "/etc/calibration/master_calibration.yaml"
    if os.path.exists(calibration_config):
        base_params = merge_param_files([base_params, calibration_config])

    base_launch_configs.append(SetLaunchConfiguration("base_params", base_params))

    return base_launch_configs


def configure_side_controllers(context, end_effector_side='right', *args, **kwargs):

    pkg_share_folder = get_package_share_directory(
        'tiago_dual_controller_configuration')

    # Arg names
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
        [
            generate_load_controller_launch_description(
                controller_name=arm_controller_name,
                controller_params_file=os.path.join(
                    pkg_share_folder,
                    'config', f'{arm_controller_name}.yaml'))
        ],
        condition=LaunchConfigurationNotEquals(arm_arg_name, 'no-arm'))

    # Setup ee controller
    end_effector = read_launch_argument(end_effector_arg_name, context)
    end_effector_underscore = end_effector.replace('-', '_')

    if "robotiq" in end_effector:
        ee_pkg_name = "pal_robotiq_controller_configuration"
        ee_launch_file = "robotiq_gripper_controller.launch.py"
    else:
        ee_pkg_name = f"{end_effector_underscore}_controller_configuration"
        ee_launch_file = f"{end_effector_underscore}_controller.launch.py"

    end_effector_controller = include_scoped_launch_py_description(
        pkg_name=ee_pkg_name,
        paths=['launch', ee_launch_file],
        launch_arguments={"side": end_effector_side},
        condition=IfCondition(
            PythonExpression(
                [
                    "'",
                    LaunchConfiguration(arm_arg_name),
                    "' != 'no-arm' "
                ]
            )
        ),
    )

    # Setup ft-sensor controller
    ft_sensor_controller_name = concatenate_strings(
        strings=['ft_sensor', end_effector_side, 'controller'],
        delimiter='_',
        skip_empty=True)

    ft_sensor_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name=ft_sensor_controller_name,
                controller_params_file=os.path.join(
                    pkg_share_folder,
                    'config', f'{ft_sensor_controller_name}.yaml'))
        ],
        condition=IfCondition(
            PythonExpression(
                [
                    "'",
                    LaunchConfiguration(arm_arg_name),
                    "' != 'no-arm' and '",
                    LaunchConfiguration(ft_sensor_arg_name),
                    "' != 'no-ft-sensor'"
                ]
            )
        ),
    )

    return [arm_controller, end_effector_controller, ft_sensor_controller]


def concatenate_strings(strings: List[str], delimiter: str = '', skip_empty: bool = False):

    concatenated_string = ''

    if skip_empty:
        concatenated_string = delimiter.join(filter(None, strings))
    else:
        concatenated_string = delimiter.join(strings)

    return concatenated_string
