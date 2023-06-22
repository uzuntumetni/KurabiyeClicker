import pyautogui
import cv2
import time
#confidence metodu için opencv kütüphanesi
while pyautogui.position() != (0, 0):
 #sol üste kaydırınca kapanıcak
    time.sleep(0.5)
    kurabiyekontrol = pyautogui.locateOnScreen('cookie.png', confidence=0.5)
    if kurabiyekontrol is None:
        print('Kurabiye Bulunamadı')
    else:
        kurabiyeyeri = pyautogui.locateCenterOnScreen('cookie.png', confidence=0.5)
        if kurabiyeyeri is None:
            print('Kurabiye yeri bulunamadı')
        else:
            x, y = kurabiyeyeri
            pyautogui.moveTo(x, y)
            pyautogui.leftClick()
