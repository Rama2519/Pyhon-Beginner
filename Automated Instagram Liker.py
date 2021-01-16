# Import relevant modules
import time
import pyautogui

time.sleep(5)

pyautogui.moveTo(667, 611)
pyautogui.click()

for i in range(14994):
    time.sleep(1)
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.press('enter')

