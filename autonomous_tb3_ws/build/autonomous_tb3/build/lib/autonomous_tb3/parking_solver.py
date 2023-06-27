import math
import sys
import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator

def calculate_distance(pose1, pose2):
    dx = pose1.pose.position.x - pose2.pose.position.x
    dy = pose1.pose.position.y - pose2.pose.position.y
    return math.sqrt(dx*dx + dy*dy)

def main():
    rclpy.init()
    navigator = BasicNavigator()

    # Set the initial pose of the robot
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.pose.position.x = -7.99
    initial_pose.pose.position.y = -13.85
    initial_pose.pose.orientation.w = 1.0

    # Set the list of parking coordinates
    parking_coordinates = [
        PoseStamped(),
        PoseStamped(),
        PoseStamped()
    ]

    # Coordinate 1
    parking_coordinates[0].header.frame_id = 'map'
    parking_coordinates[0].pose.position.x = -1.09
    parking_coordinates[0].pose.position.y = -5.7
    parking_coordinates[0].pose.orientation.w = 1.0

    # Coordinate 2
    parking_coordinates[1].header.frame_id = 'map'
    parking_coordinates[1].pose.position.x = -6.55
    parking_coordinates[1].pose.position.y = -4.08
    parking_coordinates[1].pose.orientation.w = 1.0

    # Coordinate 3
    parking_coordinates[2].header.frame_id = 'map'
    parking_coordinates[2].pose.position.x = -7.41
    parking_coordinates[2].pose.position.y = -6.5
    parking_coordinates[2].pose.orientation.w = 1.0

    navigator.setInitialPose(initial_pose)
    navigator.waitUntilNav2Active()  # Wait until Nav2 is active

    # Calculate the distances from the robot to each parking coordinate
    distances = []
    for coord in parking_coordinates:
        distance = calculate_distance(initial_pose, coord)
        distances.append(distance)

    # Find the index of the coordinate with the shortest distance
    min_distance_index = distances.index(min(distances))
    target_coordinate = parking_coordinates[min_distance_index]

    # Navigate to the coordinate with the shortest distance
    navigator.goToPose(target_coordinate)
    while not navigator.isTaskComplete():
        feedback = navigator.getFeedback()
        if feedback.navigation_time > 600:
            navigator.cancelTask()

    # Get the final result of the navigation task
    result = navigator.getResult()
    if result == navigator.TaskResult.SUCCEEDED:
        print('Parking navigation succeeded!')
    elif result == navigator.TaskResult.CANCELED:
        print('Parking navigation was canceled!')
    elif result == navigator.TaskResult.FAILED:
        print('Parking navigation failed!')

    # Shutdown the ROS node
    navigator.destroyNode()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
