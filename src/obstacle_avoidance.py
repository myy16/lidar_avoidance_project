class ObstacleAvoidance:
    def __init__(self, lidar, motors):
        self.lidar = lidar
        self.motors = motors

    def avoid_obstacles(self):
        scan_data = self.lidar.get_scan()
        front_distance = min(scan_data[170:190])

        if front_distance < 1.0:
            print("⚠️ Engel Algılandı! Kaçınma manevrası yapılıyor.")
            if min(scan_data[0:90]) > min(scan_data[270:360]):  
                self.motors.turn_right()
            else:
                self.motors.turn_left()
        else:
            self.motors.move_forward()
