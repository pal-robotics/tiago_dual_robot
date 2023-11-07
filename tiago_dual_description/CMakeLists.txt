cmake_minimum_required(VERSION 3.5)
project(tiago_dual_description)

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

#############
## Testing ##
#############

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

endif()

#############
## Install ##
#############

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE)
