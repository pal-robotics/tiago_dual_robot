play_motion:
  controllers: @{
# This executed and printed, and this is written to the resulting yaml file
controllers = ["head_controller", "torso_controller", "arm_left_controller", "arm_right_controller"]
if end_effector_left  in ["schunk-wsg", "pal-gripper"]:
  controllers.append("gripper_left_controller")
elif end_effector_left == "pal-hey5":
  controllers.append("hand_left_controller")
if end_effector_right  in ["schunk-wsg", "pal-gripper"]:
  controllers.append("gripper_right_controller")
elif end_effector_right == "pal-hey5":
  controllers.append("hand_right_controller")

print controllers
}@
  motions:
    home: #This is completely made up and is only an example
      joints: [torso_lift_joint, arm_left_1_joint,
      arm_left_2_joint, arm_left_3_joint, arm_left_4_joint, arm_left_5_joint,
      arm_left_6_joint, arm_left_7_joint, arm_right_1_joint,
      arm_right_2_joint, arm_right_3_joint, arm_right_4_joint, arm_right_5_joint,
      arm_right_6_joint, arm_right_7_joint]
      points:
      - positions: [0.25, 0.20, 0.35, -0.20, 1.94, -1.57, 1.37, 0.0, 0.20,
      0.35, -0.20, 1.94, -1.57, 1.37, 0.0]
        time_from_start: 0.5
      meta:
        name: Home
        usage: demo
        description: 'Go home'
