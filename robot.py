import math
import ctre 
import wpilib
import robotpy_ext.common_drivers
from networktables import NetworkTables
import logging

MOTOR1 = 1
MOTOR2 = 2

# Encoder Constants
# made up values, must do testing
DISTANCE_PER_PULSE = 1.0 
MAX_PERIOD = 1.0
MIN_RATE = 1.0



class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #DRIVETRAIN
        print("It's Alive")
        self.stick = wpilib.XboxController(0)
        self.motor1 = ctre.WPI_TalonSRX(MOTOR1)
        self.motor2 = ctre.WPI_TalonSRX(MOTOR2)
        self.encoder = wpilib.Encoder(0,1)
        
        #display motor rpm
        NetworkTables.initialize()
        logging.basicConfig(level = logging.DEBUG)
        self.sd = NetworkTables.getTable("SmartDashboard")

    def robotPeriodic(self):
        return

    def teleopInit(self):
        print("TELEOP BEGINS")

        # Encoder parameters initialization.
        self.encoder.reset()
        #self.encoder.setDistancePerPulse(DISTANCE_PER_PULSE)
        #self.encoder.setMaxPeriod(MAX_PERIOD)
        #self.encoder.setMinRate(MIN_RATE)


        #self.motor2 = ctre.WPI_TalonSRX(PORT)
       # self.drive = DifferentialDrive(self.motor1, self.motor2)
        # setup wheel diameter

    def teleopPeriodic(self):
        forward = self.stick.getRawAxis(5)
        self.motor1.set(forward)
        self.motor2.set(forward)
        #print(self.encoder.get())
        QuadPosition = self.motor1.getQuadraturePosition()
        print(QuadPosition)
        self.sd.putNumber("ShooterRPM", QuadPosition)


if __name__ == "__main__":
	wpilib.run(Robot)
    