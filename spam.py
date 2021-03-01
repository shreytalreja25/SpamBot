import pyautogui, sleep

time.sleep(5)
f = open("lyrics" , 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")