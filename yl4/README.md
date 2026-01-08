# Ül4: py_srvcli teenus ja klient (AddTwoInts)

ROS 2 Python pakett `py_srvcli`, mis realiseerib teenuse ja kliendi `example_interfaces/srv/AddTwoInts` jaoks.

## Käivitamine

### Build
cd yl4/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --packages-select py_srvcli
source install/setup.bash

### Terminal 1 (service)
ros2 run py_srvcli service

### Terminal 2 (client)
ros2 run py_srvcli client 2 3
