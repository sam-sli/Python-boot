import pyautogui 
import webbrowser 
import time
webbrowser.open('https://web.whatsapp.com/')
time.sleep(10)
for i in range(1000):
    pyautogui.press("z")
    pyautogui.press("a")
    pyautogui.press("m")
    pyautogui.press("l") 
    pyautogui.press("enter")
