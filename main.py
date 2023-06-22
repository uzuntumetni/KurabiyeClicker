import pyautogui
import time

pyautogui.FAILSAFE = False
calisiyor = True
kurabiyesayaci = 0
while calisiyor:
    if pyautogui.position() == (0, 0):  # programı imleci sol üste çekerek kapatacak kod
        calisiyor = False
        print('Program kapatılıyor.')
        break
    else:
        time.sleep(0.5)
        kurabiyekontrol = pyautogui.locateOnScreen('cookie.png', confidence=0.5)
        if kurabiyekontrol is None:
            print('Kurabiye Bulunamadı')
        else:
            kurabiyeyeri = pyautogui.locateCenterOnScreen('cookie.png', confidence=0.5)
            if kurabiyeyeri is not None:
                kurabiyesayaci += 1
                print('Tıklanılan kurabiye sayısı:', kurabiyesayaci)  # Sayaç ekledim
                x, y = kurabiyeyeri
                pyautogui.moveTo(x, y)
                pyautogui.leftClick()
                if pyautogui.position() == (0, 0):  # döngünün içindeyken imleci götürürsek te kapansın diye buraya da koydum.
                    print('Program Kapanıyor.')
                    exit()
            else:
                print('Kurabiye yeri bulunamadı')
