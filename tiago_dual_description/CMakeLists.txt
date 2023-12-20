cmake_minimum_required(VERSION 3.8)
project(tiago_dual_description)

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

if(pal_module_cmake_FOUND)
  pal_register_modules(
    module/30_robot_state_publisher.yaml
  )
endif()


#############
## Testing ##
#############

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  foreach(arm_type_left tiago-arm no-arm)
    foreach(arm_type_right tiago-arm no-arm)
        foreach(end_effector_left pal-gripper pal-hey5 custom no-end-effector)
            foreach(end_effector_right pal-gripper pal-hey5 custom no-end-effector)
                foreach(ft_sensor_left no-ft-sensor schunk-ft)
                    foreach(ft_sensor_right no-ft-sensor schunk-ft)

                        set(left_side "${arm_type_left}_${end_effector_left}_${ft_sensor_left}")
                        set(right_side "${arm_type_right}_${end_effector_right}_${ft_sensor_right}")

                        add_launch_test(
                          test/test_description.launch.py
                          TARGET "tiago_dual_description_${left_side}_${right_side}"
                          ARGS
                          "arm_type_left:=${arm_type_left}"
                          "arm_type_right:=${arm_type_right}"
                          "end_effector_left:=${end_effector_left}"
                          "end_effector_right:=${end_effector_right}"
                          "ft_sensor_left:=${ft_sensor_left}"
                          "ft_sensor_right:=${ft_sensor_right}"
                        )
                    endforeach()
                endforeach()
            endforeach()
        endforeach()


        foreach(laser_model no-laser hokuyo sick-551 sick-561 sick-571)
          add_launch_test(
            test/test_description.launch.py
            TARGET "tiago_dual_description_${arm_type_left}_${arm_type_right}_${laser_model}"
            ARGS "arm_type_left:=${arm_type_left}" "arm_type_right:=${arm_type_right}" "laser_model:=${laser_model}"
          )
        endforeach()
        foreach(camera_model no-camera orbbec-astra orbbec-astra-pro asus-xtion)
          add_launch_test(
            test/test_description.launch.py
            TARGET "tiago_dual_description_${arm_type_left}_${arm_type_right}_${camera_model}"
            ARGS "arm_type_left:=${arm_type_left}" "arm_type_right:=${arm_type_right}" "camera_model:=${camera_model}"
          )
        endforeach()

      endforeach()
    endforeach()
endif()

#############
## Install ##
#############

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE launch config robots meshes urdf ros2_control)
