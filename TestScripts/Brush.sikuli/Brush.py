import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestBrush(unittest.TestCase):

    def setUp(self):       
        cleanCache_And_LaunchPSE()

    def test_UI_Brush(self):
        findElement("BaselineIMG_LeftHandPanel.png")
        clickElement("QuickSelectionTool.png")
        findElement("BaselineIMG_SelectionPanel.png")
        clickElement(Pattern("SelectionBrushTool.png").similar(0.90))
        findElement("BaselineIMG_SelectionBrushPanel.png")
        clickElement(Pattern("EyeTool.png").similar(0.80))
        findElement("BaselineIMG_RedEyeRemovalPanel.png")
        clickElement(Pattern("CloneStampTool.png").similar(0.80))
        findElement("BaselineIMG_CloneStampPanel.png")
        clickElement(Pattern("ColorPickerTool.png").similar(0.80))
        findElement("BaselineIMG_ColorPickerPanel.png")       
        wait(3)

    def tearDown(self):
       closePSE()        

