import num2words
import pydirectinput
from pynput.keyboard import Controller
import time


keyboard = Controller()

print(f'You have 5 seconds to get to your input window.')
time.sleep(5)


for i in range(1, 101):
    pydirectinput.keyDown('/')
    pydirectinput.keyUp('/')

    keyboard.type(num2words.num2words(i).upper()+'!')
    time.sleep(0.3)

    pydirectinput.keyDown('enter')
    pydirectinput.keyUp('enter')
    pydirectinput.keyDown('space')
    pydirectinput.keyUp('space')
    time.sleep(1.4)







