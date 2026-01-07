# Ül3  Publisher ja Subscriber (py_pubsub)

## Eesmärk
Luua ROS 2 Python pakett, mis sisaldab talker (publisher) ja listener (subscriber) node'i.

## Asukoht
Workspace: `yl3/ros2_ws`  
Pakett: `py_pubsub`

## Failid
- `py_pubsub/publisher_member_function.py`
- `py_pubsub/subscriber_member_function.py`

## Sõltuvused
`package.xml` sisaldab:
- `rclpy`
- `std_msgs`

## Ehitus
```bash
cd yl3/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --packages-select py_pubsub
source install/setup.bash

