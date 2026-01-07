# Ül2  ROS 2 paketi loomine (ament_python)

## Eesmärk
Luua ROS 2 Python pakett `ament_python` build-tüübiga ning käivitada node `ros2 run` käsuga.

## Asukoht
Workspace: `yl2/ros2_ws`  
Pakett: `my_py_pkg`  
Node: `my_node`

## Ehitus ja käivitamine
```bash
cd yl2/ros2_ws
source /opt/ros/humble/setup.bash
colcon build
source install/local_setup.bash
ros2 run my_py_pkg my_node

