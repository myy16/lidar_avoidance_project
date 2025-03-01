import random

class LidarSensor:
    def __init__(self):
        self.scan_data = []

    def get_scan(self):
        self.scan_data = [random.uniform(0.5, 5.0) for _ in range(360)]
        return self.scan_data
