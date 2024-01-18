play_motion2:
  ros__parameters:
@[if has_arm_left or has_arm_right]@
    controllers: @{
# This executed and printed, and this is written to the resulting yaml file
controllers = ["head_controller", "torso_controller"]
if has_arm_left:
      controllers.append("arm_left_controller")
if has_arm_right:
      controllers.append("arm_right_controller")
if end_effector_left in ["pal-gripper", "robotiq-2f-85", "robotiq-2f-140"]:
      controllers.append("gripper_left_controller")
elif end_effector_left == "pal-hey5":
      controllers.append("hand_left_controller")
if end_effector_right  in ["pal-gripper", "robotiq-2f-85", "robotiq-2f-140"]:
      controllers.append("gripper_right_controller")
elif end_effector_right == "pal-hey5":
      controllers.append("hand_right_controller")
print(controllers)
}@
@[else]@
    controllers: [head_controller, torso_controller]
@[end if]@
@[if has_arm_left or has_arm_right]@
    motions:
@[if end_effector_left == "pal-gripper"]@
      close_left:
        joints: [gripper_left_left_finger_joint, gripper_left_right_finger_joint]
        positions: [0.0, 0.0]
        times_from_start: [0.5]
        meta:
          name: Close left
          usage: picking
          description: Close Left gripper
      open_left:
        joints: [gripper_left_left_finger_joint, gripper_left_right_finger_joint]
        times_from_start: [0.5]
        positions: [0.044, 0.044]
        meta:
          name: Open left
          usage: picking
          description: Open left gripper
@[elif end_effector_left == "pal-hey5"]@
      close_left:
        joints: [hand_left_thumb_joint, hand_left_index_joint, hand_left_mrl_joint]
        positions: [2.37, 0.0, 0.0,
                    6.2, 6.8, 9.2]
        times_from_start: [0.1, 2.5]
        meta:
          name: Close left
          usage: picking
          description: Close Left hand
      open_left:
        joints: [hand_left_thumb_joint, hand_left_index_joint, hand_left_mrl_joint]
        positions: [-1.0, -1.0, -1.0,
                      0.0, 0.0, 0.0]
        times_from_start: [0.1, 2.5]
        meta:
          name: Open left
          usage: picking
          description: Open Left hand
@[elif end_effector_left in ["robotiq-2f-85", "robotiq-2f-140"]]@
      close_left:
        joints: [gripper_left_finger_joint]
        times_from_start: [0.5]
@[if end_effector_left == "robotiq-2f-85"]@
        positions: [0.8]
@[elif end_effector_left == "robotiq-2f-140"]@
        positions: [0.7]
@[end if]@
        meta:
          name: Close left
          usage: picking
          description: Close Left gripper
      open_left:
        joints: [gripper_left_finger_joint]
        times_from_start: [0.5]
        positions: [0.0]
        meta:
          name: Open left
          usage: picking
          description: Open Left gripper
@[end if]@
@[if end_effector_right == "pal-gripper"]@
      close_right:
        joints: [gripper_right_left_finger_joint, gripper_right_right_finger_joint]
        times_from_start: [0.5]
        positions: [0.0, 0.0]
        meta:
          name: Close right
          usage: picking
          description: Close right gripper
      open_right:
        joints: [gripper_right_left_finger_joint, gripper_right_right_finger_joint]
        times_from_start: [0.5]
        positions: [0.044, 0.044]
        meta:
          name: Open right
          usage: picking
          description: Open right gripper
@[elif end_effector_right == "pal-hey5"]@
      close_right:
        joints: [hand_right_thumb_joint, hand_right_index_joint, hand_right_mrl_joint]
        positions: [2.37, 0.0, 0.0, 
                    6.2, 6.8, 9.2]
        times_from_start: [0.1, 2.5]
        meta:
          name: Close right
          usage: picking
          description: Close right hand
      open_right:
        joints: [hand_right_thumb_joint, hand_right_index_joint, hand_right_mrl_joint]
        positions: [-1.0, -1.0, -1.0,
                        0.0, 0.0, 0.0]
        times_from_start: [0.1, 2.5]
        meta:
          name: Open right
          usage: picking
          description: Open right hand
@[elif end_effector_right in ["robotiq-2f-85", "robotiq-2f-140"]]@
      close_right:
        joints: [gripper_right_finger_joint]
        times_from_start: [0.5]
@[if end_effector_right == "robotiq-2f-85"]@
        positions: [0.8]
@[elif end_effector_right == "robotiq-2f-140"]@
        positions: [0.7]
@[end if]@
        meta:
          name: Close right
          usage: picking
          description: Close Right gripper
      open_right:
        joints: [gripper_right_finger_joint]
        times_from_start: [0.5]
        positions: [0.0]
        meta:
          name: Open right
          usage: picking
          description: Open right gripper
@[end if]@

  # TODO: Make motions for open both

@[else]@
    motions: {}
@[end if]@
