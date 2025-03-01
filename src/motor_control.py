class MotorControl:
    def __init__(self):
        self.left_speed = 0
        self.right_speed = 0

    def move_forward(self, speed=1.0):
        print(f"🚗 İleri gidiliyor: Hız = {speed}")
        self.left_speed = speed
        self.right_speed = speed

    def move_backward(self, speed=1.0):
        print(f"🚗 Geri gidiliyor: Hız = {speed}")
        self.left_speed = -speed
        self.right_speed = -speed

    def turn_left(self, speed=0.5):
        print("↩️ Sola dönülüyor")
        self.left_speed = 0
        self.right_speed = speed

    def turn_right(self, speed=0.5):
        print("↪️ Sağa dönülüyor")
        self.left_speed = speed
        self.right_speed = 0

    def stop(self):
        print("🛑 Araç durdu")
        self.left_speed = 0
        self.right_speed = 0
