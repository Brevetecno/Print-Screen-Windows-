import pyautogui as auto
import time

while True:
    auto.alert(f'Confirme para tirar PRINT')
    time.sleep(0.2) 
    auto.hotkey('printscreen')
    time.sleep(0.2)
    auto.hotkey('Win')
    time.sleep(0.2)
    auto.press(['p','a','i', 'n', 't'])
    time.sleep(1)
    auto.press('ENTER')
    time.sleep(1)
    auto.hotkey('ctrl', 'v')
    time.sleep(0.2)
    auto.hotkey('f12')
    exit()


