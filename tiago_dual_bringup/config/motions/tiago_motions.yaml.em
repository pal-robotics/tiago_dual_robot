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

print(controllers)
}@
