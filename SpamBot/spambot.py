import pyautogui, time
time.sleep(10)
f = open(r'C:\VisualCode\python\faszom.txt', 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')