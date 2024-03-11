play_motion2:
  ros__parameters:
    motion_planner:
      disable_motion_planning: false
      planning_groups: # Sorted by order of preference
@[if has_arm_left]@
        - arm_left_torso
        - arm_left
@[end if]@
@[if has_arm_right]@
        - arm_right_torso
        - arm_right
@[end if]@
@[if has_arm_left and has_arm_right]@
        - both_arms_torso
@[end if]@
        - torso
      exclude_from_planning_joints:
        - head_1_joint
        - head_2_joint
@[if end_effector_left == "pal-hey5"]@
        - hand_left_thumb_joint
        - hand_left_mrl_joint
        - hand_left_index_joint
@[end if]@
@[if end_effector_right == "pal-hey5"]@
        - hand_right_thumb_joint
        - hand_right_mrl_joint
        - hand_right_index_joint
@[end if]@
@[if end_effector_left == "pal-gripper"]@
        - gripper_left_left_finger_joint
        - gripper_left_right_finger_joint
@[end if]@
@[if end_effector_right == "pal-gripper"]@
        - gripper_right_left_finger_joint
        - gripper_right_right_finger_joint
@[end if]@
@[if end_effector_left in ["robotiq-2f-85", "robotiq-2f-140"]]@
        - gripper_left_finger_joint
@[end if]@
@[if end_effector_right in ["robotiq-2f-85", "robotiq-2f-140"]]@
        - gripper_right_finger_joint
@[end if]@
      joint_tolerance: 0.01

      # Parameters for non-planned approach
      approach_velocity: 0.5
      approach_min_duration: 0.5
