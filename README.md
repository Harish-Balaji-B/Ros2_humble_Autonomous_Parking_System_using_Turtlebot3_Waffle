# Autonomous Parking System using ROS2 Humble
This repository contains the code and resources for an Autonomous Parking System developed using ROS2 Humble. The system utilizes ROS2 as the framework for communication and coordination between various components, enabling a robust and efficient solution for automated parking.

# Table of Contents
- Introduction
- Installation
- Usage
- Configuration
- System Architecture
- Contributing
- License

# Introduction
The Autonomous Parking System is designed to enable vehicles to park automatically without human intervention. It utilizes various sensors, such as cameras, lidar, and ultrasonic sensors, to perceive the environment and make informed decisions for safe and efficient parking.

This system leverages the capabilities of ROS2 Humble, a flexible and modular open-source framework for developing robot software applications. ROS2 provides a robust middleware layer for communication and coordination between the different components of the parking system, ensuring seamless integration and efficient data exchange.

# Installation
To install and set up the Autonomous Parking System on your system, follow these steps:

Clone this repository to your local machine:
<br>
` git clone https://github.com/Harish-Balaji-B/Ros2_humble_Autonomous_Parking_System_using_Turtlebot3_Waffle.git `<br>

Install the required dependencies. Make sure you have ROS2 Humble installed on your system.<br>
`sudo apt install ros-humble-desktop`<br>

Build the ROS2 packages by navigating to the root directory of the cloned repository and executing the following command:<br>
`colcon build`<br>

Once the build is successful, you can proceed to the next section to configure and run the Autonomous Parking System.

# Usage
To run the Autonomous Parking System, follow these steps:

Launch the system using the provided launch file:<br>
`ros2 launch autonomous_parking_system parking_system.launch.py`<br>

The system will start initializing and establishing the necessary connections with the sensors and actuators.
Once the initialization is complete, the system will be ready to perform autonomous parking.
Monitor the system's output and any relevant logs or visualizations to observe the parking process.

# Configuration
The Autonomous Parking System can be configured to adapt to different environments and vehicle types. The configuration options and parameters can be found in the <strong>config</strong> directory of this repository.

To customize the system's behavior, modify the respective configuration files according to your requirements. Make sure to rebuild the ROS2 packages after making any changes.

# System Architecture
The Autonomous Parking System follows a modular architecture, consisting of several interconnected components. Here is an overview of the major components:

- <strong>Perception</strong>: This component uses sensors like cameras, lidar, and ultrasonic sensors to perceive the environment, detect obstacles, and determine the parking space.

- <strong>Planning</strong>: The planning component processes the sensor data and generates a trajectory or path for the vehicle to follow while parking. It considers factors such as obstacle avoidance, parking spot availability, and vehicle constraints.

- <strong>Control</strong>: The control component receives the planned trajectory and generates control commands for the vehicle's actuators, such as steering, acceleration, and braking, to execute the parking maneuver accurately.

- <strong>Localization</strong>: Localization helps in accurately determining the vehicle's position and orientation within the parking environment. It uses sensor data and mapping information to estimate the vehicle's pose.

- <strong>Human-Machine Interface</strong>: This component provides a user interface for interacting with the Autonomous Parking System. It enables users to monitor the system's status, configure settings, and override or interrupt the parking process if necessary.

# Sample Images


