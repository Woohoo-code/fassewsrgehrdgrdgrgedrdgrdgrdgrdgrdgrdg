import pyautogui
import random
import time
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
time.sleep(.2)
pyautogui.hotkey("ctrl", "alt", "win", "n")
time.sleep(.2)
pyautogui.press("enter")
time.sleep(.5)
var = random.randint(0,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
extension = ".py"
pyautogui.write(f"file{var}{extension}")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl", "f5")
time.sleep(.2)
pyautogui.click(x=1018, y=60)
time.sleep(.5)
pyautogui.click(x=1033, y=519)
