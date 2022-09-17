# -*- coding: UTF-8 -*
import pyautogui
pyautogui.PAUSE = 0.01
timer = 0
while timer <= 30:
    targetLocation = pyautogui.locateCenterOnScreen('target.png', region=(530, 122, 869, 535), confidence=0.251)
    if targetLocation is None:
        continue
    else:
        targetLocation = pyautogui.locateCenterOnScreen('target.png', region=(530, 122, 869, 535), confidence=0.251)
        pyautogui.click(targetLocation)
        print(  targetLocation)
        timer += 1