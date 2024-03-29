#!/usr/bin/env python3
import em
import sys
import os


em_file_path = sys.argv[1]

no_em_extension_path = os.path.splitext(em_file_path)[0]
no_extension_path = os.path.splitext(no_em_extension_path)[0]
extension = os.path.splitext(no_em_extension_path)[1]

end_effectors = ["pal-hey5", "pal-gripper", "schunk-wsg", "robotiq-2f-85", "robotiq-2f-140", "robotiq-epick", "custom", "no-ee"]
ft_sensors = ["schunk-ft", None]
arm_config = [True, False] #For validation of pmb2 only

for left_end_effector in end_effectors:
    for right_end_effector in end_effectors:
        for left_ft_sensor in ft_sensors:
            for right_ft_sensor in ft_sensors:
                for has_arm_left in arm_config:
                    for has_arm_right in arm_config:
                        cfg = {
                           "has_arm_left": has_arm_left,
                           "has_arm_right": has_arm_right,
                           "end_effector_left": left_end_effector,
                           "end_effector_right": right_end_effector,
                           "ft_sensor_left": left_ft_sensor,
                           "ft_sensor_right": right_ft_sensor,
                        }
                        if not has_arm_left:
                            cfg["end_effector_left"] = None
                            cfg["ft_sensor_left"] = None
                        if not has_arm_right:
                            cfg["end_effector_right"] = None
                            cfg["ft_sensor_right"] = None

                        with open(em_file_path, "r") as f:
                            expanded_contents = em.expand(f.read(), cfg)
                        left_suffix = ""
                        right_suffix = ""
                        if not has_arm_left:
                            left_suffix = "_no-arm-left"
                        else:
                            if left_ft_sensor is None:
                                left_suffix += "_{}".format(left_end_effector)
                            else:
                                left_suffix += "_{}_{}".format(left_end_effector, left_ft_sensor)
                        if not has_arm_right:
                            right_suffix = "_no-arm-right"
                        else:
                            if right_ft_sensor is None:
                                right_suffix += "_{}".format(right_end_effector)
                            else:
                                right_suffix += "_{}_{}".format(right_end_effector, right_ft_sensor)
                        expanded_file_name = no_extension_path + left_suffix + right_suffix + extension
                        with open(expanded_file_name, "w") as f:
                            msg = "Autogenerated file, don't edit this, edit {} instead".format(
                                os.path.basename(em_file_path))
                            if extension == ".yaml":
                                f.write("#" + msg + "\n")
                            elif extension in [".xacro", ".xml", ".srdf"]:
                                f.write("<!-- " + msg + "-->\n")

                            f.write(expanded_contents)
                        print("Generated " + expanded_file_name)
