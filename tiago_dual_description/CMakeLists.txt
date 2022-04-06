cmake_minimum_required(VERSION 2.8.3)
project(tiago_dual_description)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir robots urdf config meshes)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  foreach(end_effector_left pal-gripper pal-hey5 schunk-wsg robotiq-2f-85 robotiq-2f-140 robotiq-epick custom false)
      foreach(end_effector_right pal-gripper pal-hey5 schunk-wsg robotiq-2f-85 robotiq-2f-140 robotiq-epick custom false)
          foreach(ft_sensor_left false schunk-ft)
              foreach(ft_sensor_right false schunk-ft)
                      add_rostest(test/test_tiago_dual.test ARGS end_effector_left:=${end_effector_left}
                          end_effector_right:=${end_effector_right} ft_sensor_left:=${ft_sensor_left}
                          ft_sensor_right:=${ft_sensor_right})
              endforeach(ft_sensor_right)
          endforeach(ft_sensor_left)
      endforeach(end_effector_right)
  endforeach(end_effector_left)
  # Separated to speed up tests, otherwise it's over 13min
  foreach(laser_model false hokuyo sick-551 sick-561 sick-571)
                      add_rostest(test/test_tiago_dual.test ARGS
                          laser_model:=${laser_model})
  endforeach(laser_model)
  foreach(camera_model false orbbec-astra orbbec-astra-pro asus-xtion)
                      add_rostest(test/test_tiago_dual.test ARGS
                          camera_model:=${camera_model})
  endforeach(camera_model)
  # Test for different wrist models
  foreach(wrist_right_model wrist-2010 wrist-2017)
    foreach(wrist_left_model wrist-2010 wrist-2017)
                      add_rostest(test/test_tiago_dual.test ARGS
                          wrist_left_model:=${wrist_left_model}
                          wrist_right_model:=${wrist_right_model})
    endforeach(wrist_left_model)
  endforeach(wrist_right_model)
endif()
