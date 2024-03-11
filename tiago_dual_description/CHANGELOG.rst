^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_dual_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.4.18 (2024-03-11)
-------------------
* remove empty line
* deg_to_rad not necessary
* fix material package name
* fix package depend. pal_urdf_utils
* Contributors: Sai Kishor Kothakota, ileniaperrella

0.4.17 (2024-03-06)
-------------------

0.4.16 (2024-03-01)
-------------------

0.4.15 (2024-02-28)
-------------------
* Merge branch 'davidterkuile-erbium-devel-patch-98202' into 'erbium-devel'
  Update tiago_dual_description/urdf/torso/torso_dual.urdf.xacro
  See merge request robots/tiago_dual_robot!92
* Slightly decrease size of updated collision link
* Update tiago_dual_description/urdf/torso/torso_dual.urdf.xacro
* Contributors: David ter Kuile, davidterkuile

0.4.14 (2023-11-20)
-------------------

0.4.13 (2023-11-17)
-------------------

0.4.12 (2023-11-08)
-------------------

0.4.11 (2023-10-25)
-------------------

0.4.10 (2023-10-24)
-------------------
* Merge branch 'urdf-utils' into 'erbium-devel'
  Change to urdf utils
  See merge request robots/tiago_dual_robot!79
* Change to urdf utils
* Merge branch 'change_license_to_apache' into 'erbium-devel'
  change public license to Apache License 2.0
  See merge request robots/tiago_dual_robot!77
* change public license to Apache License 2.0
* Merge branch 'fixed_torso_argument_2' into 'erbium-devel'
  Fixed torso argument 2
  See merge request robots/tiago_dual_robot!74
* updated the torso to be at half it's range when fixed
* Manual formating
* Added if condition in torso xacro
* Added parameter to main xacro
* Merge branch 'davidterkuile-erbium-devel-patch-00829' into 'erbium-devel'
  Update deprecated joint state publisher gui
  See merge request robots/tiago_dual_robot!71
* Update deprecated joint state publisher gui
* Contributors: David ter Kuile, Jordan Palacios, Sai Kishor Kothakota, Victor Lutz, davidterkuile

0.4.9 (2023-04-18)
------------------

0.4.8 (2023-03-13)
------------------
* Merge branch 'feat/ydlidar' into 'erbium-devel'
  added support to ydlidar
  See merge request robots/tiago_dual_robot!66
* added support to ydlidar
* Contributors: antoniobrandi

0.4.7 (2023-01-23)
------------------

0.4.6 (2022-11-16)
------------------

0.4.5 (2022-10-24)
------------------

0.4.4 (2022-08-10)
------------------
* Merge branch 'fix_torso_collision' into 'erbium-devel'
  Fix collision boxes for the torso
  See merge request robots/tiago_dual_robot!59
* Fix collision boxes for the torso
* Contributors: saikishor, thomaspeyrucain

0.4.3 (2022-07-26)
------------------

0.4.2 (2022-07-21)
------------------

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
* Add no-ee to tests in CMAKELIST
* correctly update tiago_dual.urdf.xacro
* update
* Genereate motion and planning appraoch files|
* generate new config files
* merge
* Genereate motion and planning appraoch files|
* generate new config files
* Genereate motion and planning appraoch files|
* generate new config files
* Contributors: David ter Kuile, saikishor

0.3.8 (2022-03-23)
------------------

0.3.7 (2022-03-18)
------------------
* Merge branch 'add_robotiq_epick_gripper' into 'erbium-devel'
  Add robotiq-epick gripper to tiago dual
  See merge request robots/tiago_dual_robot!51
* Add robotiq-epick config files
* Add robotiq-epick gripper to tiago dual
* Contributors: davidfernandez, thomaspeyrucain

0.3.6 (2021-12-22)
------------------

0.3.5 (2021-11-26)
------------------
* Merge branch 'fix-omni' into 'erbium-devel'
  removed call to gazebo_omni
  See merge request robots/tiago_dual_robot!49
* removed call to gazebo_omni
* Contributors: antoniobrandi, davidfernandez

0.3.4 (2021-11-22)
------------------
* Merge branch 'conditional_dependencies' into 'erbium-devel'
  Conditional dependencies
  See merge request robots/tiago_dual_robot!47
* added PAL_DISTRO conditioning for PAL dependencies
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
* Clening the code for the joy controller and calling the proper gazebo file
* Creating tiago dual with omni base robot
* Contributors: antoniobrandi, saikishor

0.2.3 (2021-08-31)
------------------

0.2.2 (2021-08-06)
------------------

0.2.1 (2021-06-01)
------------------
* Merge branch 'parametrize-robot-description' into 'erbium-devel'
  Add parameter for robot_description
  See merge request robots/tiago_dual_robot!40
* Add parameter for robot_description
* Contributors: Victor Lopez, victor

0.2.0 (2021-05-06)
------------------
* Merge branch 'robotiq_gripper' into 'erbium-devel'
  Robotiq gripper
  See merge request robots/tiago_dual_robot!39
* add the robotiq grippers to the tests and added dependencies
* add robotiq grippers to valid end effectors list
* Contributors: Sai Kishor Kothakota, saikishor

0.1.37 (2021-03-29)
-------------------
* Merge branch 'cutom-end-effector' into 'erbium-devel'
  Cutom end effector
  See merge request robots/tiago_dual_robot!38
* fix: adapt to dual when importing tiago_end_effector from single
* chore: urdf xacro
* chore: package and CMakeLists
* Contributors: daniellopez, davidfernandez

0.1.36 (2021-01-12)
-------------------

0.1.35 (2021-01-12)
-------------------

0.1.34 (2020-11-25)
-------------------
* Merge branch 'no_safety_eps_head' into 'erbium-devel'
  added no safety eps to head
  See merge request robots/tiago_dual_robot!33
* added no safety eps to head
* Contributors: Sai Kishor Kothakota, victor

0.1.33 (2020-10-21)
-------------------
* Merge branch 'fix-camera-extrinsics-path' into 'erbium-devel'
  Fix camera extrinsics calibration env variable name
  See merge request robots/tiago_dual_robot!34
* Fix camera extrinsics calibration env variable name
* Contributors: Victor Lopez, victor

0.1.32 (2020-09-08)
-------------------

0.1.31 (2020-08-03)
-------------------

0.1.30 (2020-07-30)
-------------------

0.1.29 (2020-07-27)
-------------------

0.1.28 (2020-07-10)
-------------------
* Merge branch 'add-no-safety-eps' into 'erbium-devel'
  Add no_safety_eps param
  See merge request robots/tiago_dual_robot!30
* Add no_safety_eps param
* Contributors: Victor Lopez, victor

0.1.27 (2020-07-01)
-------------------
* Merge branch 'add-master-calibration' into 'erbium-devel'
  Add master calibration to tiago dual
  See merge request robots/tiago_dual_robot!28
* Add extrinsic compatibility
* Fix env variable
* Use optenv to get description calibration path
* Add master calibration to tiago dual
* Contributors: Victor Lopez, victor

0.1.26 (2020-06-19)
-------------------

0.1.25 (2020-06-06)
-------------------

0.1.24 (2020-06-02)
-------------------

0.1.23 (2020-05-28)
-------------------

0.1.22 (2020-05-27)
-------------------
* Merge branch 'tiago_dual_screen' into 'erbium-devel'
  added changes to support tiago_dual with and without screen
  See merge request robots/tiago_dual_robot!24
* added changes to support tiago_dual with and without screen
* Contributors: Sai Kishor Kothakota, victor

0.1.21 (2020-05-12)
-------------------
* Merge branch 'description-calibration-fixes' into 'erbium-devel'
  Description calibration fixes
  See merge request robots/tiago_dual_robot!22
* parse package name instead of individual elements and load files respective to package
* pass the camera origin as an argument to head
* Contributors: Sai Kishor Kothakota, victor

0.1.20 (2020-05-06)
-------------------
* Merge branch 'fix-tiago-wrist-offset' into 'erbium-devel'
  Change tool link position depending on wrist type
  See merge request robots/tiago_dual_robot!21
* Change tool link position depending on wrist type
* Contributors: Victor Lopez, victor

0.1.19 (2020-04-21)
-------------------
* Merge branch 'more_wrist_2019_fixes' into 'erbium-devel'
  More wrist 2019 fixes
  See merge request robots/tiago_dual_robot!19
* Add wrist-2017 as default wrist model
* Added check for proper wrist model
* Added tests for different wrists
* added missing xacro properties
* added missing arg in upload.launch
* Contributors: Sai Kishor Kothakota, victor

0.1.18 (2020-04-20)
-------------------

0.1.17 (2020-04-20)
-------------------
* Merge branch 'wrist_2019_fix' into 'erbium-devel'
  Update arm\_*_6 range based on the wrist type
  See merge request robots/tiago_dual_robot!18
* Update arm\_*_6 range based on the wrist type
* Contributors: Sai Kishor Kothakota, victor

0.1.16 (2020-04-16)
-------------------
* Allow disable end effector
* Contributors: Victor Lopez

0.1.15 (2020-04-08)
-------------------
* Merge branch 'add-arm-sides' into 'erbium-devel'
  Add arm sides
  See merge request robots/tiago_dual_robot!17
* Add arm_left and arm_right params
* Contributors: Victor Lopez, victor

0.1.14 (2020-03-25)
-------------------

0.1.13 (2020-03-23)
-------------------

0.1.12 (2020-01-28)
-------------------

0.1.11 (2020-01-08)
-------------------

0.1.10 (2019-11-06)
-------------------
* Merge branch 'arm_offset_fix' into 'erbium-devel'
  parse arm joint offsets through macro
  See merge request robots/tiago_dual_robot!13
* parse arm joint offsets through macro
* Contributors: Sai Kishor Kothakota, Victor Lopez

0.1.9 (2019-10-03)
------------------

0.1.8 (2019-10-02)
------------------

0.1.7 (2019-09-27)
------------------

0.1.6 (2019-09-26)
------------------
* Merge branch 'ferrum-fixes' into 'erbium-devel'
  Fix urdf False parsing
  See merge request robots/tiago_dual_robot!9
* Fix urdf False parsing
* Contributors: Victor Lopez

0.1.5 (2019-09-05)
------------------

0.1.4 (2019-06-07)
------------------

0.1.3 (2019-05-22)
------------------
* Merge branch 'arm-update' into 'erbium-devel'
  Arm update
  See merge request robots/tiago_dual_robot!4
* Update description to match hardware changes
* Contributors: Victor Lopez

0.1.2 (2019-05-02)
------------------
* Merge branch 'urdf-update' into 'erbium-devel'
  New torso inertia and fixed arm_1 "Y"
  See merge request robots/tiago_dual_robot!3
* Update meshes for tiago dual arm
* New torso inertia and fixed arm_1 "Y"
* Contributors: Victor Lopez

0.1.1 (2019-04-16)
------------------
* Fix wrong robot name in urdf
* Contributors: Victor Lopez

0.1.0 (2019-04-15)
------------------
* Fix package versions
* Merge branch 'tiago-dual' into 'master'
  Tiago dual
  See merge request robots/tiago_dual_robot!1
* Add missing tiago dependencies
* Finish dual arm urdf
* Remove unused install rules
* Continue creation of tiago_dual_robot
* Fix xacro warnings
* Add torso for 2 arms
* Add test for urdf
* First working version, with 2 right arms
* First steps towards urdf
* First functional version
* Contributors: Victor Lopez
