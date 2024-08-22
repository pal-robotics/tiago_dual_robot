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
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from dataclasses import dataclass
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import read_launch_argument
from tiago_dual_description.tiago_dual_launch_utils import get_tiago_dual_hw_suffix
from launch_pal.param_utils import merge_param_files
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import CommonArgs
from tiago_dual_description.launch_arguments import TiagoDualArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    arm_type_right: DeclareLaunchArgument = TiagoDualArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoDualArgs.arm_type_left
    end_effector_right: DeclareLaunchArgument = TiagoDualArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoDualArgs.end_effector_left
    ft_sensor_right: DeclareLaunchArgument = TiagoDualArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = TiagoDualArgs.ft_sensor_left

    use_sim_time:  DeclareLaunchArgument = CommonArgs.use_sim_time


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    play_motion2 = include_scoped_launch_py_description(
        pkg_name='play_motion2',
        paths=['launch', 'play_motion2.launch.py'],
        launch_arguments={
            "use_sim_time":  launch_args.use_sim_time,
            "motions_file": LaunchConfiguration('motions_file'),
            'motion_planner_config': LaunchConfiguration('motion_planner_config')
        })

    launch_description.add_action(OpaqueFunction(
        function=create_play_motion_filename))
    launch_description.add_action(play_motion2)

    return


def create_play_motion_filename(context):

    pkg_name = 'tiago_dual_bringup'
    pkg_share_dir = get_package_share_directory(pkg_name)
    arm_right = read_launch_argument('arm_type_right', context)
    arm_left = read_launch_argument('arm_type_left', context)
    ee_right = read_launch_argument('end_effector_right', context)
    ee_left = read_launch_argument('end_effector_left', context)

    hw_suffix = get_tiago_dual_hw_suffix(
        arm_right=arm_right,
        arm_left=arm_left,
        end_effector_right=ee_right,
        end_effector_left=ee_left
    )

    ee_motions = []
    motions_folder = os.path.join(pkg_share_dir, 'config', 'motions')
    base_motions_file = 'tiago_motions_no_arms.yaml'
    # both arms
    if arm_right != 'no-arm' and arm_left != 'no-arm':
        base_motions_file = 'tiago_motions_general.yaml'
    # right arm only
    elif arm_right != 'no-arm' and arm_left == 'no-arm':
        base_motions_file = 'tiago_motions_general_arm_right.yaml'
    # left arm only
    elif arm_right == 'no-arm' and arm_left != 'no-arm':
        base_motions_file = 'tiago_motions_general_arm_left.yaml'

    if ee_left != 'no-end-effector' and arm_left != 'no-arm':
        ee_motions.append(f"tiago_motions_{ee_left}_left.yaml")
    if ee_right != 'no-end-effector' and arm_right != 'no-arm':
        ee_motions.append(f"tiago_motions_{ee_right}_right.yaml")

    motion_files = [base_motions_file]
    motion_files.extend(ee_motions)

    motion_yamls = [os.path.join(motions_folder, f) for f in motion_files]

    combined_yaml = merge_param_files(motion_yamls)

    motion_planner_file = f"motion_planner{hw_suffix}.yaml"
    motion_planner_config = os.path.join(
        pkg_share_dir, 'config', 'motion_planner', motion_planner_file)

    return [SetLaunchConfiguration("motions_file", combined_yaml),
            SetLaunchConfiguration("motion_planner_config", motion_planner_config)]
