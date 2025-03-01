from lidar_sensor import LidarSensor
from motor_control import MotorControl
from obstacle_avoidance import ObstacleAvoidance
import time

lidar = LidarSensor()
motors = MotorControl()
obstacle_avoidance = ObstacleAvoidance(lidar, motors)

def main():
    while True:
        obstacle_avoidance.avoid_obstacles()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
