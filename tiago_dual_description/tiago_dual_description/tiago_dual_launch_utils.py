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

from tiago_description.tiago_launch_utils import get_tiago_hw_suffix


def get_tiago_dual_hw_suffix(
        arm_right: str = 'no-arm',
        arm_left: str = 'no-arm',
        end_effector_right: str = 'no-end-effector',
        end_effector_left: str = 'no-end-effector',
        ft_sensor_right: str = 'no-ft-sensor',
        ft_sensor_left: str = 'no-ft-sensor'):
    """
    Generate a substitution that creates a text suffix combining the specified \
    tiago dual arguments.

    The arguments are read as string
    """
    right_suffix = get_tiago_hw_suffix(
        arm_right, end_effector_right, ft_sensor_right)
    left_suffix = get_tiago_hw_suffix(
        arm_left, end_effector_left, ft_sensor_left)

    suffix = left_suffix + right_suffix
    return suffix
