gravity_compensation:
  type: "force_control/GravityCompensation"
  robot_model_chains:
@[if end_effector_left == "pal-gripper"]@
    - gripper_left_link
@[end if]@
@[if end_effector_right == "pal-gripper"]@
    - gripper_right_link
@[end if]@
@[if end_effector_left == "pal-hey5"]@
    - hand_left_palm_link
@[end if]@
@[if end_effector_right == "pal-hey5"]@
    - hand_right_palm_link
@[end if]@
@[if end_effector_left == "schunk-wsg"]@
    - gripper_left_link
@[end if]@
@[if end_effector_right == "schunk-wsg"]@
    - gripper_right_link
@[end if]@
@[if end_effector_left in ["robotiq-2f-85", "robotiq-2f-140"]]@
    - gripper_left_base_link
@[end if]@
@[if end_effector_right in ["robotiq-2f-85", "robotiq-2f-140"]]@
    - gripper_right_base_link
@[end if]@
@[if end_effector_left == "custom"]@
    - arm_left_tool_link
@[end if]@
@[if end_effector_right == "custom"]@
    - arm_right_tool_link
@[end if]@
@[if end_effector_left == "no-ee"]@
    - arm_left_tool_link
@[end if]@
@[if end_effector_right == "no-ee"]@
    - arm_right_tool_link
@[end if]@
  dt: 0.01


