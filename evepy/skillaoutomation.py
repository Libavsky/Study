import pyautogui as gui
import time
def dragItem(xfrom,yfrom,xto,yto):
    gui.moveTo(xfrom, yfrom, 0.8)
    gui.mouseDown()
    gui.moveTo(xfrom+3, yfrom+3, 0.8)
    gui.mouseUp()
    gui.moveTo(xfrom+5, yfrom+5, 0.8)
    gui.mouseDown()
    gui.moveTo(xto, yto, 0.8)
    gui.mouseUp()
def dragBar(yfrom,yto):
    time.sleep(2)
    gui.moveTo(1735, yfrom, 0.8)
    gui.mouseDown()
    gui.moveTo(1735, yto, 0.8)
    gui.mouseUp()
    time.sleep(2)
time.sleep(2)
dragBar(72,102)
for i in range(0,10):
    gui.moveTo(1343, 66+(i*40)+i, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(1851, 174, duration=0.5)
    gui.click()
    time.sleep(7)
    gui.moveTo(694, 515, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(63, 590, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(81, 611, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(1892, 6, duration=0.5)
    gui.click()
    time.sleep(10)
dragBar(102,178)
for i in range(0,10):
    gui.moveTo(1343, 66+(i*40)+i, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(1851, 174, duration=0.5)
    gui.click()
    time.sleep(7)
    gui.moveTo(694, 515, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(63, 590, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(81, 611, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(1892, 6, duration=0.5)
    gui.click()
    time.sleep(10)
dragBar(178,253)
for i in range(0,10):
    gui.moveTo(1343, 66+(i*40)+i, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(1851, 174, duration=0.5)
    gui.click()
    time.sleep(7)
    gui.moveTo(694, 515, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(63, 590, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(81, 611, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(1892, 6, duration=0.5)
    gui.click()
    time.sleep(10)
dragBar(253,329)
for i in range(0,10):
    gui.moveTo(1343, 66+(i*40)+i, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(1851, 174, duration=0.5)
    gui.click()
    time.sleep(7)
    gui.moveTo(694, 515, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(63, 590, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(81, 611, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(1892, 6, duration=0.5)
    gui.click()
    time.sleep(10)
dragBar(329,413)
for i in range(0,10):
    gui.moveTo(1343, 56+(i*40)+i, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(1851, 174, duration=0.5)
    gui.click()
    time.sleep(7)
    gui.moveTo(694, 515, duration=0.5)
    gui.click()
    time.sleep(15)
    gui.moveTo(63, 590, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(81, 611, duration=0.5)
    gui.click()
    time.sleep(2)
    gui.moveTo(1892, 6, duration=0.5)
    gui.click()
    time.sleep(10)
# try:
#        while True:
#            x, y = gui.position()
#            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#            print(positionStr, end='')
#            print('\b' * 20, end='', flush=True)
# except KeyboardInterrupt:
#     print('\nDone.')


