import math
import ctre 
import wpilib
import robotpy_ext.common_drivers
from networktables import NetworkTables
import logging
from navx import AHRS
from Aimer import Aimer
PORT = 9

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
        self.motor1 = ctre.WPI_TalonSRX(PORT)
        self.encoder = wpilib.Encoder(0,1)
        
        #display motor rpm
        NetworkTables.initialize()
        logging.basicConfig(level = logging.DEBUG)
        self.sd = NetworkTables.getTable("SmartDashboard")
        # Gyro
        self.ahrs = AHRS.create_spi()
        self.Aimer = Aimer(self.ahrs)
        self.s = wpilib.Joystick(0)

        

         
    def robotPeriodic(self):
        return

    def teleopInit(self):
        print("TELEOP BEGINS")
        
        self.encoder.reset()
        #self.encoder.setDistancePerPulse(DISTANCE_PER_PULSE)
        #self.encoder.setMaxPeriod(MAX_PERIOD)
        #self.encoder.setMinRate(MIN_RATE)


        #self.motor2 = ctre.WPI_TalonSRX(PORT)
       # self.drive = DifferentialDrive(self.motor1, self.motor2)
        # setup wheel diameter

        
    def teleopPeriodic(self):
        aiming = False
        forward = self.stick.getRawAxis(5)
        self.motor1.set(forward)
        #print(self.encoder.get())
        QuadPosition = self.motor1.getQuadraturePosition()
        print(QuadPosition)
        self.sd.putNumber("ShooterRPM", QuadPosition)
        
        if self.s.getRawButton(2):
            spin=self.Aimer.aim()  
            aiming = True
        if aiming:
            self.motor1.set(spin)
if __name__ == "__main__":
	wpilib.run(Robot)
    