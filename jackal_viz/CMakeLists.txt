cmake_minimum_required(VERSION 3.5)
project(jackal_viz)
find_package(ament_cmake REQUIRED)

install(DIRECTORY launch rviz rqt
  DESTINATION share/${PROJECT_NAME}
)
ament_package()
