^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_dual_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.3 (2024-03-06)
------------------

2.0.2 (2024-02-28)
------------------
* Rename approach_planner config to motion_planner
* Update approach_planner configuration
* change sufix no-end-effector to no-ee
* use the same functionality to create the suffix for the config files
* Contributors: Aina Irisarri, Noel Jimenez

2.0.1 (2024-01-18)
------------------

2.0.0 (2024-01-18)
------------------
* Merge branch 'ros2-tiago-gazebo' into 'humble-devel'
  Ros2 tiago gazebo
  See merge request robots/tiago_dual_robot!81
* Add missing open left motion for pal gripper
* Add maintainer
* Update authors
* Remove typos in appraoch planner loader
* CMake version to 3.8
* Add approach planner
* update to  new robot argument method
* Add copyright license
* Update launch file layout and use new scoped_launch_file function
* Add joy_teleop config
* Add modules for module manager
* Add website tag
* Add regen_em script as node
* Allow for tiago dual to launch with one arm
* Update arg propagation
* update motion names
* Basic launch structure ready. Gazebo does not launch properly
* Add motions files(still old param style) and controller yaml
* Add general motions and removed schunk-wsg from the regen_em scripts
* Update twist mux and joystick launch files
* Add bringup and playmotion launch files
* Cmakelists.txt and package.xml only
* Merge branch 'change_license_to_apache' into 'erbium-devel'
  change public license to Apache License 2.0
  See merge request robots/tiago_dual_robot!77
* change public license to Apache License 2.0
* Contributors: David ter Kuile, Jordan Palacios, Sai Kishor Kothakota, davidterkuile

0.4.9 (2023-04-18)
------------------
* Merge branch 'update-joystick' into 'erbium-devel'
  Update joystick device name
  See merge request robots/tiago_dual_robot!68
* Update joystick device name
* Contributors: David ter Kuile, Sai Kishor Kothakota

0.4.8 (2023-03-13)
------------------

0.4.7 (2023-01-23)
------------------
* Merge branch 'robot-state-publisher' into 'erbium-devel'
  Update node to robot_state_publisher
  See merge request robots/tiago_dual_robot!67
* Update node to robot_state_publisher
* Contributors: David ter Kuile, Jordan Palacios

0.4.6 (2022-11-16)
------------------

0.4.5 (2022-10-24)
------------------

0.4.4 (2022-08-10)
------------------

0.4.3 (2022-07-26)
------------------

0.4.2 (2022-07-21)
------------------
* Merge branch 'add_omni_tiago_dual' into 'erbium-devel'
  Add special motions for Tiago dual omni to not collide with the base
  See merge request robots/tiago_dual_robot!55
* Add base_type to the missing launch files
* Add special motions for Tiago dual omni to not collide with the base
* Contributors: saikishor, thomaspeyrucain

0.4.1 (2022-07-14)
------------------

0.4.0 (2022-05-03)
------------------
* Merge branch 'no-end-effector-bugfix' into 'erbium-devel'
  No end effector bugfix
  See merge request robots/tiago_dual_robot!54
* file_suffix consistency
* bools to true
* update for tiago missing one of the arms
* update motion.em
* update motions
* minor bugfixes in launch files
* Genereate motion and planning appraoch files|
* generate new config files
* update motions
* minor bugfixes in launch files
* Genereate motion and planning appraoch files|
* generate new config files
* minor bugfixes in launch files
* Genereate motion and planning appraoch files|
* generate new config files
* Contributors: David ter Kuile, saikishor

0.3.8 (2022-03-23)
------------------
* Merge branch 'fix_motions_aborting' into 'erbium-devel'
  Fixing aborting motions due to joint limit + change slightly home position
  See merge request robots/tiago_dual_robot!53
* Fixing aborting motions due to joint limit
* Contributors: saikishor, thomaspeyrucain

0.3.7 (2022-03-18)
------------------
* Merge branch 'add_robotiq_epick_gripper' into 'erbium-devel'
  Add robotiq-epick gripper to tiago dual
  See merge request robots/tiago_dual_robot!51
* Remove open/close both buttons for epick + add cartesian impedance cotroller support for epick + add effort package
* Change controller and joint name and adapt the joystick and the motions for the epick gripper
* Add robotiq-epick config files
* Contributors: davidfernandez, thomaspeyrucain

0.3.6 (2021-12-22)
------------------

0.3.5 (2021-11-26)
------------------

0.3.4 (2021-11-22)
------------------
* Merge branch 'conditional_dependencies' into 'erbium-devel'
  Conditional dependencies
  See merge request robots/tiago_dual_robot!47
* change to package version 3
* Contributors: Sai Kishor Kothakota, victor

0.3.3 (2021-11-10)
------------------

0.3.2 (2021-11-10)
------------------

0.3.1 (2021-11-09)
------------------

0.3.0 (2021-11-03)
------------------
* Merge branch 'omni_base_robot' into 'erbium-devel'
  Creating tiago dual with omni base robot
  See merge request robots/tiago_dual_robot!44
* modified .em file in order to generate the joy config file
* added speed limit for the lateral mouvements of the robot with joystick
* Clening the code for the joy controller and calling the proper gazebo file
* bringup of the tiago dual with omni base
* Contributors: antoniobrandi, saikishor

0.2.3 (2021-08-31)
------------------

0.2.2 (2021-08-06)
------------------

0.2.1 (2021-06-01)
------------------

0.2.0 (2021-05-06)
------------------
* Merge branch 'robotiq_gripper' into 'erbium-devel'
  Robotiq gripper
  See merge request robots/tiago_dual_robot!39
* run incremental action server for robotiq grippers
* Update joy teleop configurations
* generate tiago hardware configuration
* generate the joy teleop configurations
* generated play motion configuration for robotiq 2F-85 and 2F-140
* generated approach planner configuration
* add changes to generate configuration for new robotiq 2F-85 and 2F-140 grippers
* Contributors: Sai Kishor Kothakota, saikishor

0.1.37 (2021-03-29)
-------------------
* Merge branch 'cutom-end-effector' into 'erbium-devel'
  Cutom end effector
  See merge request robots/tiago_dual_robot!38
* fix: delete unused motions and adapt contions to it
* motions only need to add custom ones
* chore: extra spaces
* fix: lauch file logic for play motion
* docs: not todo task for customer
* chore: play_motion launch
* chore: package and CMakeLists
* feat: combinations with custom ee
* Contributors: daniellopez, davidfernandez

0.1.36 (2021-01-12)
-------------------
* Merge branch 'missing_safety_files' into 'erbium-devel'
  added missing safety files for the wrist and torso joints
  See merge request robots/tiago_dual_robot!36
* Merge branch 'gravityfix' into 'missing_safety_files'
  Add gravity mode for new wrist model on tiagodual
  See merge request robots/tiago_dual_robot!35
* Add gravity mode for new wrist model on tiagodual
* Contributors: Irina Cocolos, victor

0.1.35 (2021-01-12)
-------------------

0.1.34 (2020-11-25)
-------------------

0.1.33 (2020-10-21)
-------------------

0.1.32 (2020-09-08)
-------------------

0.1.31 (2020-08-03)
-------------------
* Merge branch 'fix_tf_prefix' into 'erbium-devel'
  Fix argument name
  See merge request robots/tiago_dual_robot!32
* Fix argument name
* Contributors: davidfernandez, luca

0.1.30 (2020-07-30)
-------------------
* Merge branch 'rename_tf_prefix' into 'erbium-devel'
  Rename tf_prefix param
  See merge request robots/tiago_dual_robot!23
* Rename tf_prefix param
* Contributors: davidfernandez, victor

0.1.29 (2020-07-27)
-------------------

0.1.28 (2020-07-10)
-------------------
* Merge branch 'add-no-safety-eps' into 'erbium-devel'
  Add no_safety_eps param
  See merge request robots/tiago_dual_robot!30
* Add no_safety_eps to tiago_dual.launch
* Contributors: Victor Lopez, victor

0.1.27 (2020-07-01)
-------------------
* Merge branch 'add-master-calibration' into 'erbium-devel'
  Add master calibration to tiago dual
  See merge request robots/tiago_dual_robot!28
* Add use of multipliers from master_calibration
* Contributors: Victor Lopez, victor

0.1.26 (2020-06-19)
-------------------
* Merge branch 'motions' into 'erbium-devel'
  fix home left/right and wave to avoid collision with elo
  See merge request robots/tiago_dual_robot!29
* fix home left/right and wave to avoid collision with elo
* Contributors: YueErro, victor

0.1.25 (2020-06-06)
-------------------

0.1.24 (2020-06-02)
-------------------
* Merge branch 'fix_home_for_screen' into 'erbium-devel'
  fix home motion to avoid collision with screen
  See merge request robots/tiago_dual_robot!26
* fix home motion to avoid collision with screen
* Contributors: Sai Kishor Kothakota, victor

0.1.23 (2020-05-28)
-------------------
* Merge branch 'has_screen_fix' into 'erbium-devel'
  removed unused argument of has_screen
  See merge request robots/tiago_dual_robot!25
* removed unused argument of has_screen
* Contributors: Sai Kishor Kothakota, victor

0.1.22 (2020-05-27)
-------------------
* Merge branch 'tiago_dual_screen' into 'erbium-devel'
  added changes to support tiago_dual with and without screen
  See merge request robots/tiago_dual_robot!24
* added changes to support tiago_dual with and without screen
* Contributors: Sai Kishor Kothakota, victor

0.1.21 (2020-05-12)
-------------------

0.1.20 (2020-05-06)
-------------------

0.1.19 (2020-04-21)
-------------------
* Merge branch 'more_wrist_2019_fixes' into 'erbium-devel'
  More wrist 2019 fixes
  See merge request robots/tiago_dual_robot!19
* Add wrist-2017 as default wrist model
* Contributors: Sai Kishor Kothakota, victor

0.1.18 (2020-04-20)
-------------------
* Merge branch 'fix_wave' into 'erbium-devel'
  Fix wrist orient for wave
  See merge request robots/tiago_dual_robot!20
* Fix wrist orient for wave
* Contributors: davidfernandez, victor

0.1.17 (2020-04-20)
-------------------
* Merge branch 'wrist_2019_fix' into 'erbium-devel'
  Update arm\_*_6 range based on the wrist type
  See merge request robots/tiago_dual_robot!18
* Update arm\_*_6 range based on the wrist type
* Contributors: Sai Kishor Kothakota, victor

0.1.16 (2020-04-16)
-------------------
* Fixd wrist ft topic names
* Contributors: Victor Lopez

0.1.15 (2020-04-08)
-------------------
* Merge branch 'add-arm-sides' into 'erbium-devel'
  Add arm sides
  See merge request robots/tiago_dual_robot!17
* Split has_arm into has_arm_left and has_arm_right
* Add arm_left and arm_right params
* Contributors: Victor Lopez, victor

0.1.14 (2020-03-25)
-------------------
* Merge branch 'fix-arm-bug' into 'erbium-devel'
  Set Arm existance default to true
  See merge request robots/tiago_dual_robot!16
* Set Arm existance default to true
* Contributors: davidfernandez, victor

0.1.13 (2020-03-23)
-------------------
* Update regen script for no file.
  Fixes #3
* regen motions without arm as well
* Merge branch 'fix-play-motion' into 'erbium-devel'
  fixed play motion for no-arm arg
  Closes #2
  See merge request robots/tiago_dual_robot!15
* fixed play motion for no-arm arg
* Contributors: Procópio Stein, Victor Lopez, victor

0.1.12 (2020-01-28)
-------------------

0.1.11 (2020-01-08)
-------------------
* Fixed right/left wrist ft name
* Contributors: Jordan Palacios

0.1.10 (2019-11-06)
-------------------
* Merge branch 'remove-sonar-cloud' into 'erbium-devel'
  removed sonar cloud
  See merge request robots/tiago_dual_robot!12
* removed dep
* removed sonar cloud
* Contributors: Procópio Stein, Victor Lopez

0.1.9 (2019-10-03)
------------------

0.1.8 (2019-10-02)
------------------
* Remove speed_limit
* Contributors: Victor Lopez

0.1.7 (2019-09-27)
------------------
* Merge branch 'speed-limit' into 'erbium-devel'
  changed dep to speed limit node
  See merge request robots/tiago_dual_robot!10
* changed dep to speed limit node
* Contributors: Procópio Stein, Victor Lopez

0.1.6 (2019-09-26)
------------------

0.1.5 (2019-09-05)
------------------
* Merge branch 'fix_gripper_controller_name' into 'erbium-devel'
  Fixed the name open_right for the motions
  See merge request robots/tiago_dual_robot!8
* Fixed the open_right name in the template .em
* Fixed the name open_right for the motions
* Merge branch 'fix_gripper_controller_name' into 'erbium-devel'
  Fixed the gripper controller name
  See merge request robots/tiago_dual_robot!7
* Fixed the gripper controller name
* Contributors: Victor Lopez, alessandrodifava

0.1.4 (2019-06-07)
------------------

0.1.3 (2019-05-22)
------------------
* Merge branch 'arm-update' into 'erbium-devel'
  Arm update
  See merge request robots/tiago_dual_robot!4
* Minor fixes to tiago motions
* Updated reach motions
* Made home a little bit safer
* Fix alive motions
* Fix last wrist in home and update wave
* Update home motions
* Contributors: Victor Lopez, davidfernandez

0.1.2 (2019-05-02)
------------------
* Merge branch 'motions' into 'erbium-devel'
  Add generic motions
  See merge request robots/tiago_dual_robot!2
* Add Reach Max and Floor
* Open and Close end-effectors
* Remove dummy home from generated files
* Add generic motions
* Contributors: Victor Lopez, davidfernandez

0.1.1 (2019-04-16)
------------------
* Fix typo in plan group name
* Contributors: Victor Lopez

0.1.0 (2019-04-15)
------------------
* Merge branch 'tiago-dual' into 'master'
  Tiago dual
  See merge request robots/tiago_dual_robot!1
* Add missing tiago dependencies
* Restore upload
* Remove unused install rules
* Continue creation of tiago_dual_robot
* Add more scripts and play_motion
* Add approeach planner
* Add dummy motions
* First functional version
* Initial commit
* Contributors: Victor Lopez
