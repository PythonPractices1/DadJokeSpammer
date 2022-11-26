import pyautogui
import time
f = open("dadjoke.txt","r")
myJokes=[]

for i in f:
	myJokes.append(i.strip())

time.sleep(20)

for i in myJokes:
	pyautogui.write(i)
	pyautogui.press('enter')
