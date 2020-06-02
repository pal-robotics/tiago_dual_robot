^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_dual_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
