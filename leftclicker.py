import pyHook
import pythoncom

def onclick(event):
    print(event.Position)
    return True

hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()