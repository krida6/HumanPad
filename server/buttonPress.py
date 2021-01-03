# from pymouse import PyMouse
import Quartz
from pykeyboard import PyKeyboard
from time import sleep


#initialize the keyboard simulator
keyboard = PyKeyboard()
#presses the key
keyboard.press_key('x')
#waits five seconds before releasing the key
sleep(5)
#releases the key
keyboard.release_key('x')