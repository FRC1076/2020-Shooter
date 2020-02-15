import math
import ctre 
import wpilib
import robotpy_ext.common_drivers
from networktables import NetworkTables
import logging
from subsystems.ballShooter import BallShooter as bs


LEFTPORT = 1
RIGHTPORT = 9


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #DRIVETRAIN
        print("It's Alive")
        self.stick = wpilib.XboxController(0)
        self.motor1 = ctre.WPI_TalonSRX(LEFTPORT)
        self.motor2 = None

        #display motor rpm
        NetworkTables.initialize()
        logging.basicConfig(level = logging.DEBUG)
        self.sd = NetworkTables.getTable("SmartDashboard")

        #BALLSHOOTER
        self.bs = bs(self.motor1,)
        
    def robotPeriodic(self):
        return

    def teleopInit(self):
        print("TELEOP BEGINS")
       # self.drive = DifferentialDrive(self.motor1, self.motor2)
        self.encoder = wpilib.Encoder(0,1)
        # setup wheel diameter

    def teleopPeriodic(self):
        forward = self.stick.getRawAxis(5)
        self.motor1.set(forward)
        #print(self.encoder.get())
        
        QuadPosition = self.motor1.getQuadraturePosition()
        print(QuadPosition)
        self.sd.putNumber("ShooterRPM", QuadPosition)

        if self.stick.getAButtonPressed():
            self.bs.setaim(1500)
        if self.stick.getAButton():
            speed =self.bs.aim()
            aiming = True
        if aiming:
            self.motor1.set(speed)
if __name__ == "__main__":
	wpilib.run(Robot)
    # /14 *50 *60