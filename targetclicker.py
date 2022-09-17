# -*- coding: UTF-8 -*
import pyautogui
pyautogui.PAUSE = 0.01
timer = 0
conf = 0.26
while timer <= 30:
    targetLocation = pyautogui.locateCenterOnScreen('target.png', region=(530, 122, 869, 535), confidence=conf)
    if targetLocation is None:
        continue
    else:
        targetLocation = pyautogui.locateCenterOnScreen('target.png', region=(530, 122, 869, 535), confidence=conf)
        pyautogui.click(targetLocation)
        print(  targetLocation)
        timer += 1
