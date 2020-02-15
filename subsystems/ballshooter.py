
import wpilib
SHOOT_SPEED = 1.0
STOP_SPEED = 0.0
kP = 0.03
kI = 0.00
kD = 0.00
kF = 0.00
rpu = 10

class BallShooter:
    def __init__(self, l_motor, r_motor = None):
        self.l_motor = l_motor
        self.r_motor = r_motor
        speedController = wpilib.PIDController(
            kP, kI, kD, self, output=self
        )
        speedController.setInputRange(-180.0, 180.0)
        speedController.setOutputRange(-1.0, 1.0)
        speedController.setAbsoluteTolerance(rpu)
        speedController.setContinuous(True)
        self.speedController =speedController
        self.speed = 0
        self.lastvalue =0
    def setaim(self,setpoint):
        self.lastvalue =0
        self.setpoint=setpoint
        self.speedController.setSetpoint(self.setpoint)
    def aim(self):
        #self.ahrs.reset()
        self.speedController.enable()
        self.currentspeed = self.speed-self.lastvalue
        self.lastvalue=self.speed
        return self.currentspeed
    def getPidSourceType(self):
        return wpilib.PIDController.PIDSourceType.kRate
    def pidGet(self,source):
        self.rpm =(self.speed-self.lastvalue)/14*50*60
        return self.rpm
    def shoot(self, speed = SHOOT_SPEED):
        self.l_motor.set(speed)
        if self.r_motor != None:
            self.r_motor.set(speed)
    
    def stop(self, speed = STOP_SPEED):
        self.l_motor.set(speed)
        if self.r_motor != None:
            self.r_motor.set(speed)

def pidWrite(self, output):
    """This function is invoked periodically by the PID Controller,
    based upon navX MXP yaw angle input and PID Coefficients.
    """
    self.speed = output
        