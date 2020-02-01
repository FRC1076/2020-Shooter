from navx import AHRS
import wpilib
if wpilib.RobotBase.isSimulation():
        # These PID parameters are used in simulation
        kP = 0.06
        kI = 0.00
        kD = 0.00
        kF = 0.00
else:
        # These PID parameters are used on a real robot
        kP = 0.03
        kI = 0.00
        kD = 0.00
        kF = 0.00
kToleranceDegrees = 2.0
class Aimer:
    def __init__(self,gyro):
        self.gyro=gyro
        

        
        
        turnController = wpilib.PIDController(
            self.kP, self.kI, self.kD, self.kF, self.ahrs, output=self
        )
        turnController.setInputRange(-180.0, 180.0)
        turnController.setOutputRange(-1.0, 1.0)
        turnController.setAbsoluteTolerance(self.kToleranceDegrees)
        turnController.setContinuous(True)
        self.turncontroller =turnController
        self.rotateToAngleRate = 0
       # self.rotateToAngle = true
        #self.ahrs.reset()

        #if self.rotateToAngle:
        def   rotateToAngle(self)
            self.turnController.enable()
            self.currentRotationRate = self.rotateToAngleRate

        #else:
         #   self.turnController.disable()
         #   self.currentRotationRate = self.stick.getTwist()
            
        def aim(self,setpoint):
            #self.ahrs.reset()
            self.turnController.setSetpoint(setpoint)
            self.turnController.enable()
            self.currentRotationRate = self.rotateToAngleRate
            return self.currentRotationRate
    #def PIDInputType
    def pidWrite(self, output):
        """This function is invoked periodically by the PID Controller,
        based upon navX MXP yaw angle input and PID Coefficients.
        """
        self.rotateToAngleRate = output
        