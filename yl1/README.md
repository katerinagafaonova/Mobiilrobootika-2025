# Ül1  ROS 2 tööruumi loomine ja overlay kontroll (Humble)

## Eesmärk
- Luua ROS 2 workspace ja ehitada `turtlesim` pakett lähtekoodist.
- Tõestada overlay kasutamine (muutsin `turtlesim` aknapealkirja "MyTurtleSim").

## Asukoht
Workspace asub: `yl1/ros2_ws`

## Eeldused
- ROS 2 Humble on paigaldatud (kasutan `/opt/ros/humble`)

## Ehitus
```bash
cd yl1/ros2_ws
source /opt/ros/humble/setup.bash

# (vajadusel) sõltuvused
rosdep update
rosdep install -i --from-paths src --rosdistro humble -y

# build
colcon build --symlink-install
source install/local_setup.bash

