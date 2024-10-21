# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
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

from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from tiago_dual_description.launch_arguments import TiagoDualArgs

from urdf_test.xacro_test import define_xacro_test

xacro_file_path = Path(
    get_package_share_directory('tiago_dual_description'),
    'robots',
    'tiago_dual.urdf.xacro',
)

arm_args = (
    TiagoDualArgs.arm_type_right,
    TiagoDualArgs.arm_type_left,
)

gripper_args = (
    TiagoDualArgs.end_effector_right,
    TiagoDualArgs.end_effector_left,
    TiagoDualArgs.ft_sensor_right,
    TiagoDualArgs.ft_sensor_left,
)

test_xacro_base = define_xacro_test(xacro_file_path, arm_args, TiagoDualArgs.base_type)
test_xacro_laser = define_xacro_test(xacro_file_path, arm_args, TiagoDualArgs.laser_model)
test_xacro_camera = define_xacro_test(xacro_file_path, arm_args, TiagoDualArgs.camera_model)
test_xacro_ee = define_xacro_test(xacro_file_path, arm_args, gripper_args)
