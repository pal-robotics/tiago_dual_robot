^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_dual_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
