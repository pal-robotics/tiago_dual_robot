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
  motions:
@[if end_effector_left == "pal-gripper"]@
    close_left:
      joints: [gripper_left_left_finger_joint, gripper_left_right_finger_joint]
      points:
        - time_from_start: 0.5
          positions: [0.0, 0.0]
      meta:
        name: Close left
        usage: picking
        description: Close Left gripper
    open_left:
      joints: [gripper_left_left_finger_joint, gripper_left_right_finger_joint]
      points:
        - time_from_start: 0.5
          positions: [0.044, 0.044]
      meta:
        name: Open left
        usage: picking
        description: Open Left gripper
@[elif end_effector_left == "pal-hey5"]@
    close_left:
      joints: [hand_left_thumb_joint, hand_left_index_joint, hand_left_mrl_joint]
      points:
        - positions: [2.37, 0.0, 0.0]
          time_from_start: 0.1
        - positions: [6.2, 6.8, 9.2]
          time_from_start: 2.5
      meta:
        name: Close left
        usage: picking
        description: Close Left hand
    open_left:
      joints: [hand_left_thumb_joint, hand_left_index_joint, hand_left_mrl_joint]
      points:
        - positions: [-1.0, -1.0, -1.0]
          time_from_start: 0.1
        - positions: [0.0, 0.0, 0.0]
          time_from_start: 2.5
      meta:
        name: Open left
        usage: picking
        description: Open Left hand
@[elif end_effector_left == "schunk-wsg"]@
    close_left:
      joints: [gripper_left_finger_joint]
      points:
        - time_from_start: 0.5
          positions: [0.0]
      meta:
        name: Close left
        usage: picking
        description: Close Left gripper
    open_left:
      joints: [gripper_left_finger_joint]
      points:
        - time_from_start: 0.5
          positions: [0.031]
      meta:
        name: Open left
        usage: picking
        description: Open Left gripper
@[end if]@

@[if end_effector_right == "pal-gripper"]@
    close_right:
      joints: [gripper_right_left_finger_joint, gripper_right_right_finger_joint]
      points:
        - time_from_start: 0.5
          positions: [0.0, 0.0]
      meta:
        name: Close right
        usage: picking
        description: Close right gripper
    open_left:
      joints: [gripper_right_left_finger_joint, gripper_right_right_finger_joint]
      points:
        - time_from_start: 0.5
          positions: [0.044, 0.044]
      meta:
        name: Open right
        usage: picking
        description: Open right gripper
@[elif end_effector_right == "pal-hey5"]@
    close_right:
      joints: [hand_right_thumb_joint, hand_right_index_joint, hand_right_mrl_joint]
      points:
        - positions: [2.37, 0.0, 0.0]
          time_from_start: 0.1
        - positions: [6.2, 6.8, 9.2]
          time_from_start: 2.5
      meta:
        name: Close right
        usage: picking
        description: Close right hand
    open_right:
      joints: [hand_right_thumb_joint, hand_right_index_joint, hand_right_mrl_joint]
      points:
        - positions: [-1.0, -1.0, -1.0]
          time_from_start: 0.1
        - positions: [0.0, 0.0, 0.0]
          time_from_start: 2.5
      meta:
        name: Open right
        usage: picking
        description: Open right hand
@[elif end_effector_right == "schunk-wsg"]@
    close_right:
      joints: [gripper_right_finger_joint]
      points:
        - time_from_start: 0.5
          positions: [0.0]
      meta:
        name: Close right
        usage: picking
        description: Close right gripper
    open_right:
      joints: [gripper_right_finger_joint]
      points:
        - time_from_start: 0.5
          positions: [0.035]
      meta:
        name: Open right
        usage: picking
        description: Open right gripper
@[end if]@

@{
has_hand = False
if end_effector_right == "pal-hey5" or end_effector_left == "pal-hey5":
  has_hand = True

joints = []
positions_one_open = []
positions_one_close = []
positions_two_open = []
positions_two_close = []

if end_effector_left == "pal-gripper":
  joints.extend(["gripper_left_left_finger_joint", "gripper_left_right_finger_joint"])
  positions_one_open.extend([0.044, 0.044])
  positions_one_close.extend([0.0, 0.0])
  if has_hand:
    positions_two_open.extend([0.044, 0.044])
    positions_two_close.extend([0.0, 0.0])
elif end_effector_left == "pal-hey5":
  joints.extend(["hand_left_thumb_joint", "hand_left_index_joint", "hand_left_mrl_joint"])
  positions_one_open.extend([-1.0, -1.0, -1.0])
  positions_two_open.extend([0.0, 0.0, 0.0])
  positions_one_close.extend([2.37, 0.0, 0.0])
  positions_two_close.extend([6.2, 6.8, 9.2])
elif end_effector_left == "schunk-wsg":
  joints.extend(["gripper_left_finger_joint"])
  positions_one_open.extend([0.031])
  positions_one_close.extend([0.0])
  if has_hand:
    positions_two_open.extend([0.031])
    positions_two_close.extend([0.0])

if end_effector_right == "pal-gripper":
  joints.extend(["gripper_right_left_finger_joint", "gripper_right_right_finger_joint"])
  positions_one_open.extend([0.044, 0.044])
  positions_one_close.extend([0.0, 0.0])
  if has_hand:
    positions_two_open.extend([0.044, 0.044])
    positions_two_close.extend([0.0, 0.0])
elif end_effector_right == "pal-hey5":
  joints.extend(["hand_right_thumb_joint", "hand_right_index_joint", "hand_right_mrl_joint"])
  positions_one_open.extend([-1.0, -1.0, -1.0])
  positions_two_open.extend([0.0, 0.0, 0.0])
  positions_one_close.extend([2.37, 0.0, 0.0])
  positions_two_close.extend([6.2, 6.8, 9.2])
elif end_effector_right == "schunk-wsg":
  joints.extend(["gripper_right_finger_joint"])
  positions_one_open.extend([0.031])
  positions_one_close.extend([0.0])
  if has_hand:
    positions_two_open.extend([0.031])
    positions_two_close.extend([0.0])
}@

    close_both:
      joints: @{print(joints)}@
      points:
        - time_from_start: 0.5
          positions: @{print(positions_one_close)}@
@[if has_hand]@
        - time_from_start: 2.5
          positions: @{print(positions_two_close)}@
@[end if]
      meta:
        name: Close Both
        usage: picking
        description: Close both end effectors
    open_both:
      joints: @{print(joints)}@
      points:
        - time_from_start: 0.5
          positions: @{print(positions_one_open)}@
@[if has_hand]@
        - time_from_start: 2.5
          positions: @{print(positions_two_open)}@
@[end if]
      meta:
        name: Open Both
        usage: picking
        description: Open both end effectors