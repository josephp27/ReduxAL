import win32gui, win32ui, win32con, win32api
from ctypes import *
import time

def move_mouse(x, y):
    windll.user32.mouse_event(
        c_uint(0x0001),
        c_uint(x),
        c_uint(y),
        c_uint(0),
        c_uint(0)
    )
