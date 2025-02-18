# ROPE_Real-time_Onboard_Pose_Estimation_for_perching_MAV
by Georg Strunck

This is the GitHub repository containing all the work for my thesis, including my literature study, about the pose estimation for a perching MAV.


## Table of Contents
- [ROPE\_Real-time\_Onboard\_Pose\_Estimation\_for\_perching\_MAV](#rope_real-time_onboard_pose_estimation_for_perching_mav)
  - [Table of Contents](#table-of-contents)
  - [S: Setting up the stereo cam](#s-setting-up-the-stereo-cam)
    - [S1: Using the IntelRealsense Camera Viewer](#s1-using-the-intelrealsense-camera-viewer)
      - [S1.1: Install the IntelRealsense SDK to view and configure](#s11-install-the-intelrealsense-sdk-to-view-and-configure)
      - [S1.2: How to view the PointCloud and video feed of the stereo camera](#s12-how-to-view-the-pointcloud-and-video-feed-of-the-stereo-camera)
    - [S2: Using ROS1 with the RealSense camera](#s2-using-ros1-with-the-realsense-camera)
      - [S2.1: Installing ROS1 Noetic](#s21-installing-ros1-noetic)
      - [S2:2 Install RealSense ROS libraries:](#s22-install-realsense-ros-libraries)
      - [S2.3: Run ROS, show output](#s23-run-ros-show-output)
    - [S3: SDK](#s3-sdk)
  - [SI: Setting up the AvoidBench Simulator](#si-setting-up-the-avoidbench-simulator)
    - [SI.1: Installing the Simulator](#si1-installing-the-simulator)
    - [SI.2: Running the Simulator](#si2-running-the-simulator)
    - [SI.P: Procedures](#sip-procedures)
    - [SI.F: Running into Errors \& fixing them](#sif-running-into-errors--fixing-them)
      - [Gazebo not working](#gazebo-not-working)
      - [Unity not connecting](#unity-not-connecting)



## S: Setting up the stereo cam
For the Intel RealSense stereo camera, there are multiple ways to show the feed and change the settings. Below some of them are explained.

### S1: Using the IntelRealsense Camera Viewer

This only installs the Intel software to view the camera feeds and alter settings. It does not enable you to run ROS-related tasks. For that please see below.

#### S1.1: Install the IntelRealsense SDK to view and configure 

**Note:** Only do this if you do not do the ros package installation below, that already includes the librealsense viewer and if both exist they might clash!

To install the SDK I followed the instructions from [the official Intel tutorial](https://dev.intelrealsense.com/docs/compiling-librealsense-for-linux-ubuntu-guide).
The Git repository I cloned under Thesis/Software/librealsense.

#### S1.2: How to view the PointCloud and video feed of the stereo camera
First cd into the LibRealSense folder:
```
cd Thesis/Software/librealsense
```

Then it is possible to launch the RealSense viewer displaying the video and point-cloud feed in the Intel interface:

```
realsense-viewer
```



### S2: Using ROS1 with the RealSense camera

To install the ROS1 packages and dependencies the [official Intel guide](https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy) has been followed.
Next to that, [this YouTube tutorial](https://www.youtube.com/watch?v=d7JaQvmrVFA) was followed.

#### S2.1: Installing ROS1 Noetic

On a (more or less) clean Ubuntu 20 version I freshly installed ROS Noetic following [the official tutorial](http://wiki.ros.org/noetic/Installation/Ubuntu).

For refreshing the ROS structure and handling please have a look at the [official ROS tutorials](http://wiki.ros.org/ROS/Tutorials#Core_ROS_Tutorials).

To run any ROS related tasks don't forget to source the environment with: 
```
source /opt/ros/noetic/setup.bash
```
Note that this only holds for the noetic distribution.
Alternatively, it is possible to add the source to the bash.rc file, if no other ROS distributions are on the system. This can then be called with the 
```
source ~/.bashrc
```
shorthand.

#### S2:2 Install RealSense ROS libraries: 
Then to add the stereo cameras ROS wrapper, simply install them via:
```
sudo apt-get install ros-$ROS_DISTRO-realsense2-camera
```

#### S2.3: Run ROS, show output
1. Source the environment: ```source /opt/ros/noetic/setup.bash```
2. Launch the ROS wrapper and publish to the point cloud topic:
```roslaunch realsense2_camera rs_camera.launch filters:=pointcloud```
3. Open up Rviz in a new terminal (source again) to view the topics: ```rviz```
   1. To add the image stream, click on 'Add', go to the 'By topic' ribbon and select '/camera/color/image_raw/Image' and click 'OK'
   2. To add the pointcloud stream, click on 'Add', go to the 'By topic' ribbon and select '/camera/depth/color/points/PointCloud2' and click 'OK'

### S3: SDK
There is also the Intel SDK you can download and use. An Ubuntu guide can be found on [the Ubuntu SDK tutorial](https://ubuntu.com/tutorials/using-intel-realsense-sdk#2-getting-started).



## SI: Setting up the AvoidBench Simulator
This part of the readme explains how the AvoidBench simulator is being set up.
The instructions on the [AvoidBench GitHub](https://github.com/tudelft/AvoidBench) were followed.
The Open3D folder can be found under the  [Thesis/Software](./Thesis/Software/) folder.

### SI.1: Installing the Simulator
The steps explained [on GitHub](https://github.com/tudelft/AvoidBench) already explain everything necessary.

**Note:** Please use the ```make -j``` command carefully. If your system isn't very stable, better just leave one core for the system (eg. if you have 4 cores, then use ```make-j3```).

Make sure to add below your path, on the GitHub this needs to be replaced with your own folder path. It is needed to source the ros setup in the terminal as well.

```echo "export AVOIDBENCH_PATH=~/Documents/Thesis/ROPE_Real-time_Onboard_Pose_Estimation_for_perching_MAV/Thesis/Software/AvoidBench/src/avoidbench" >> ~/.bashrc```


### SI.2: Running the Simulator
Before starting any simulation don't forget to source the ROS workspace and afterwards the avoid_bench build in the AvoidBench directory with:

1. ```source /opt/ros/noetic/setup.bash```
2. ```source devel/setup.bash```

To run the flight simulation 

```roslaunch avoid_manage test_py.launch```

```roslaunch avoid_manage rotors_gazebo.launch```

### SI.P: Procedures

To publish to a topic do tghe below:
```rostopic pub /hummingbird/autopilot/start std_msgs/Empty```

If you do not know what type the message of the topic is like follow the below steps or [this tutorial](https://roboticsbackend.com/ros-topic-command-line-tools-practical-example-rostopic-and-rosmsg/):

```rostopic list ```
```rostopic info /counter```, where ```/counter``` is your topic in this example.
```rosmsg show std_msgs/Int32```, to show the structure of the message type of ```/counter```.
Then based on that the publishing caqn be done. 

### SI.F: Running into Errors & fixing them

#### Gazebo not working


#### Unity not connecting
