actuators:
  raw_data:
    position_port: act_position
    effort_port: act_current
    mode_port: act_control_mode
    position_cmd_port: ref_position
    velocity_cmd_port: ref_velocity
    effort_cmd_port: ref_current
    mode_cmd_port: ref_control_mode
    current_limit_cmd_port: ref_limit_current
    absolute_encoder_position_port: act_abs_position

joint_mode_black_list: ['head_controller', 'torso_controller']

@[if (ft_sensor_left == "schunk-ft" or ft_sensor_right == "schunk-ft" or end_effector_left == "schunk-wsg" or end_effector_right == "schunk-wsg")]@
force_torque:
@[end if]@
@[if ft_sensor_left == "schunk-ft"]@
  left_wrist_ft:
    frame: wrist_left_ft_link
    transformation:
      force: [-y,x,z]
      torque: [-y,x,z]
    raw_data:
      force_port: force_wrist_left
      torque_port: torque_wrist_left
@[end if]@
@[if ft_sensor_right == "schunk-ft"]@
  right_wrist_ft:
    frame: wrist_right_ft_link
    transformation:
      force: [-y,x,z]
      torque: [-y,x,z]
    raw_data:
      force_port: force_wrist_right
      torque_port: torque_wrist_right
@[end if]@
@[if end_effector_left == "schunk-wsg"]@
  gripper_left_left_fingertip:
    frame: gripper_left_left_fingertip_link
    transformation:
      force: [x,y,-z]
      torque: [x,y,z]
    raw_data:
      force_port: force_gripper_left_finger_left
      torque_port: torque_gripper_left_finger_left
  gripper_left_right_fingertip:
    frame: gripper_left_right_fingertip_link
    transformation:
      force: [x,y,-z]
      torque: [x,y,z]
    raw_data:
      force_port: force_gripper_left_finger_right
      torque_port: torque_gripper_left_finger_right
@[end if]@
@[if end_effector_right == "schunk-wsg"]@
  gripper_right_left_fingertip:
    frame: gripper_right_left_fingertip_link
    transformation:
      force: [x,y,-z]
      torque: [x,y,z]
    raw_data:
      force_port: force_gripper_right_finger_left
      torque_port: torque_gripper_right_finger_left
  gripper_right_right_fingertip:
    frame: gripper_right_right_fingertip_link
    transformation:
      force: [x,y,-z]
      torque: [x,y,z]
    raw_data:
      force_port: force_gripper_right_finger_right
      torque_port: torque_gripper_right_finger_right
@[end if]@
e_stop:
  raw_data:
    e_stop_port: emergency_stop_state

ros_control_component:
  ignore_read_errors: false
