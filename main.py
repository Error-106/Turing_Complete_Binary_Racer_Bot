import pyautogui
import pytesseract
from PIL import Image,ImageQt
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import *
import win32gui
import sys
import re
patternstr = re.compile(r"What\s*is[0-9/\s]+in\s*binary",flags=re.I) #硬编码，待替换
patternnum=re.compile(r"\d+")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pyautogui.PAUSE = 0.05
hwnd = win32gui.FindWindow('Engine', 'Turing Complete')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
while 1:
    try:
        img = ImageQt.fromqimage(screen.grabWindow(hwnd).toImage()).convert("L")
        code = pytesseract.image_to_string(img, lang='eng',config="-c tessedit_char_blacklist=l|].oO;:-").replace("/","7").replace("L","1").replace("y)","2").replace("vas","77").replace("Q7","97").replace("D4","54") #硬编码，待替换
        print(code)
        print(patternstr.search(code))
        string=patternstr.search(code).group().replace(" ","")
        print(string)
        num=int(patternnum.search(string).group())
        for i in range(0,8):
            if (num>>i)&1:
                pyautogui.press(str(8-i))
        pyautogui.press("space")
    except pyautogui.FailSafeException:
        break
    except: pass