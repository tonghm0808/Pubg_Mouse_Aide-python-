# -*- coding: UTF-8 -*-
try:
    import pythoncom
    import pyHook
except ImportError:
    print 'The pythoncom or pyHook modules are not installed.'
import driver
import gui
import time
import random
import threading

AID = 0  # 全局开启状态标志位
DY = 0  # 武器基础偏移
FIX = 0  # 鼠标修正状态标志位
OFFSET = 0  # 过热偏移


def Mouse_Fix():
    global TIMER, APP, DY, FIX, OFFSET, AID

    if FIX == 1:
        driver.SendInput(driver.Mouse(0x0001, 0, DY + OFFSET))
        OFFSET = OFFSET + 1

    APP.Update(AID, DY)
    TIMER = threading.Timer(random.randint(9, 11) / 100.0, Mouse_Fix)
    TIMER.start()


def onMouseEvent(event):
    global FIX, AID, OFFSET
    # print event.Message
    if AID == 1:
        if event.Message == 513:
            FIX = 1
        elif event.Message == 514:
            FIX = 0
            OFFSET = 0
        else:
            pass
    return True


def onKeyboardEvent(event):
    global DY, AID

    # print event.KeyID
    keyid = event.KeyID
    if keyid == 107:
        DY = DY + 1
    elif keyid == 109 and DY > 0:
        DY = DY - 1
    elif keyid == 13:
        if AID == 0:
            AID = 1
        else:
            AID = 0
    else:
        pass
    return True


def main():
    global APP
    APP = gui.App()
    APP.Update()
    TIMER = threading.Timer(1, Mouse_Fix)
    TIMER.start()
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
