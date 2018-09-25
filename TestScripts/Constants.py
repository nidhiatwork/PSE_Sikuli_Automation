import os, sys, platform
from sikuli import *


AppPath_PRE = "//Applications//Adobe Photoshop Elements 2019//Support Files//Adobe Photoshop Elements Editor.app"
userdir = os.path.expanduser('~')

RootFolder = userdir + "/Desktop/PSE_Sikuli_Automation"
BaselineFolder = RootFolder + "/BaselineImages/"
OutputFolder = RootFolder + "/Output/"
TestDataFile_path = "test.mp4"
Sikuli_Path = userdir + "/Downloads"
PRE_Test_Execution_Data = RootFolder + "/TestData/PSE_Test_Execution_Data.xls"
ScreenshotsFolder = OutputFolder + "Screenshots"