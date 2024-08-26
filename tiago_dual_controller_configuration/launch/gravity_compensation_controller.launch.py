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
from dataclasses import dataclass
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import OpaqueFunction, DeclareLaunchArgument, SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration
from launch.actions import GroupAction
from launch import LaunchContext
from launch_pal.arg_utils import read_launch_argument
from launch_pal.arg_utils import LaunchArgumentsBase
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.param_utils import parse_parametric_yaml
from tiago_dual_description.launch_arguments import TiagoDualArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    arm_motor_model_right: DeclareLaunchArgument = TiagoDualArgs.arm_motor_model_right
    arm_motor_model_left: DeclareLaunchArgument = TiagoDualArgs.arm_motor_model_left
    end_effector_right: DeclareLaunchArgument = TiagoDualArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoDualArgs.end_effector_left


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):
    launch_description.add_action(OpaqueFunction(function=setup_gravity_controller_configuration))

    gravity_compensation_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="gravity_compensation_controller",
                controller_params_file=LaunchConfiguration("controller_config"),
                extra_spawner_args=["--inactive"],
            )
        ],
    )
    launch_description.add_action(gravity_compensation_controller)

    return


def setup_gravity_controller_configuration(context: LaunchContext):

    arm_motor_model_right = read_launch_argument('arm_motor_model_right', context)
    arm_motor_model_left = read_launch_argument('arm_motor_model_left', context)
    if (arm_motor_model_left != arm_motor_model_right):
        raise Warning(
            "The motor model of the left and right arms are different.\
                  Configuration of the motor should have been added to the specific of this robot")
    end_effector_right = read_launch_argument('end_effector_right', context)
    end_effector_left = read_launch_argument('end_effector_left', context)

    if (end_effector_left == "no-end-effector"):
        ee_tip_link_left = "arm_left_tool_link"
    elif (end_effector_left == "pal-gripper"):
        ee_tip_link_left = "gripper_left_link"
    elif (end_effector_left == "pal-hey5"):
        ee_tip_link_left = "hand_left_palm_link"
    elif (end_effector_left in ["robotiq-2f-85", "robotiq-2f-140"]):
        ee_tip_link_left = "gripper_left_base_link"
    else:
        ee_tip_link_left = "arm_left_tool_link"

    if (end_effector_right == "no-end-effector"):
        ee_tip_link_right = "arm_right_tool_link"
    elif (end_effector_right == "pal-gripper"):
        ee_tip_link_right = "gripper_right_link"
    elif (end_effector_right == "pal-hey5"):
        ee_tip_link_right = "hand_right_palm_link"
    elif (end_effector_right in ["robotiq-2f-85", "robotiq-2f-140"]):
        ee_tip_link_right = "gripper_right_base_link"
    else:
        ee_tip_link_right = "arm_right_tool_link"

    remappings = {"EE_TIP_LINK_LEFT": ee_tip_link_left, "EE_TIP_LINK_RIGHT": ee_tip_link_right}

    param_file = os.path.join(get_package_share_directory(
        'tiago_dual_controller_configuration'), "config", "gravity_compensation_controller_" +
        arm_motor_model_left + ".yaml")

    parsed_yaml = parse_parametric_yaml(source_files=[param_file], param_rewrites=remappings)

    return [SetLaunchConfiguration('controller_config', parsed_yaml)]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
