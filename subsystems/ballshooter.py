SHOOT_SPEED = 1.0
STOP_SPEED = 0.0

class BallShooter:
    def __init__(self, l_motor, r_motor = NONE):
        self.l_motor = l_motor
        self.r_motor = r_motor
    
    def shoot(self, speed = SHOOT_SPEED):
        self.l_motor.set(speed)
        self.r_motor.set(speed)
    
    def stop(self, speed = STOP_SPEED):
        self.l_motor.set(speed)
        self.r_motor.set(speed)

