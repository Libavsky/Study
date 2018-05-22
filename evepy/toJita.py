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

# try:
#        while True:
#            x, y = gui.position()
#            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#            print(positionStr, end='')
#            print('\b' * 20, end='', flush=True)
# except KeyboardInterrupt:
#     print('\nDone.')
print("Liczba kursow")
z = int(input())
for i in range(0,z):
    time.sleep(5)
    #undock
    gui.moveTo(1789, 214, duration=0.5)
    gui.click()
    time.sleep(13)
    #warp undock
    gui.moveTo(141,690,duration=0.5)
    gui.click(button='right')
    gui.moveTo(191, 697, duration=0.5)
    gui.click()
    time.sleep(50)
    #jump peri
    gui.moveTo(133, 811, duration=0.5)
    gui.click(button='right')
    gui.moveTo(183, 818, duration=0.5)
    gui.click()
    time.sleep(190)
    #dock peri
    gui.moveTo(133, 811, duration=0.5)
    gui.click(button='right')
    gui.moveTo(183, 861, duration=0.5)
    gui.click()
    time.sleep(102)
    #zaladunek
    gui.moveTo(618, 565, duration=0.5)
    gui.click(618,565)
    dragItem(733,519,628,490)
    gui.moveTo(929, 604, duration=0.7)
    gui.click(929, 604)
    time.sleep(2)
    #undock
    gui.moveTo(1865, 190, duration=0.5)
    gui.click()
    time.sleep(8)
    #jump jita
    gui.moveTo(144, 672, duration=0.5)
    gui.click(button='right')
    gui.moveTo(194, 680, duration=0.5)
    gui.click()
    time.sleep(75)
    #dock jita
    gui.moveTo(144, 672, duration=0.5)
    gui.click(button='right')
    gui.moveTo(194, 722, duration=0.5)
    gui.click()
    time.sleep(190)
    #rozladunek
    gui.moveTo(628,490,0.2)
    gui.click(628,490)
    dragItem(733,519,618,634)

