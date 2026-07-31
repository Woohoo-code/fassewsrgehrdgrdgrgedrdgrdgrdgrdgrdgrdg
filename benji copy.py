import pyautogui
import time
import random
print("STARTING TO SPAM FILES")
time.sleep(3)
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl","c")
name = "file" + str(random.randint(0,99999999999999999999999999999999999999999999999999999999999999999999)) + ".py"
open(f"{name}", "w")
paths = f"C:\\Users\\User\\Documents\\Benji King\\afawawf\\{name}"
pyautogui.hotkey('ctrl', 'F5')
time.sleep(1)
pyautogui.click(x=1033, y=519)
