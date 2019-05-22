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
  dt: 0.01


