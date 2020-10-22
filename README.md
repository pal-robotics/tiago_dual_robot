# TIAGo++ robot

This package contains the description, controllers and bringup for all possible TIAGo++ configurations (end effectors, force torque sensors..).

To make maintenance easier, the `tiago_dual.urdf.xacro` takes arguments that specify the end effector types, force torqu sensors, laser model and many other parameters.

The other configuration files that  differ between between robot configurations are generated from template files.

The templates are written using [empy](https://pypi.org/project/empy/) and have the extension `.em`. 

To regenerate a group of files, you must execute `rosrun tiago_dual_bringup regen_em_file.py EM_FILE_NAME` from the directory where the `.em` file is. 





