import pyautogui
import time
text = 'Hi' #which text need to be sent
x = 20  #how many times have to be sent
delay = 3  #delay between one two text
i=1
while True:
  time.sleep(delay)
  
  while i < x+1 :
   pyautogui.typewrite(text+ " "+  str(i))
   pyautogui.press('enter') 
   i += 1
  break 

