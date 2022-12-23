from time import sleep
from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard
from pynput.keyboard import Key, Controller, Listener
from pynput.mouse import Button
from pynput.mouse import Controller as Ct
from pynput.mouse import Listener as Li
from threading import Thread

file = open('data.txt', 'r')
data = file.read()
file.close()

if data == "None":
    Npos = float(input("Please enter the X of the number coordinates (pixels): ")), float(
        input("Please enter the Y of the number coordinates (pixels): "))  # (325, 310)
    Apos = float(input("Please enter the X of the A coordinates (pixels): ")), float(
        input("Please enter the Y of the A coordinates (pixels): "))  # (670, 710)
    Bpos = float(input("Please enter the X of the B coordinates (pixels): ")), float(
        input("Please enter the Y of the B coordinates (pixels): "))  # (1270, 910)
    Epos = float(input("Please enter the X of the extra coordinates: ")), float(
        input("Please enter the Y of the extra coordinates: "))  # (1200, 510)
    Aamnt = float(input("Please enter the A (increasing amount) value (ex. 745 -> 7,45): ")) / 100  # 1.00
    Bamnt = float(input("Please enter the B (increasing amount) value (ex. 745 -> -7,45): ")) / 100  # 1.00
    Tframe = float(input("Please enter the time frame (miliseconds, 1 second = 1000 miliseconds): ")) / 1000  # 1
    Thold = float(input("Please enter the holding time (miliseconds, 1 second = 1000 miliseconds): ")) / 1000  # 3
    Textra = float(input("Please enter the extra click time (miliseconds, 1 second = 1000 miliseconds): ")) / 1000  # 2
    actualBTC=0
    file = open('data.txt', 'w')
    file.write(
        f'{Npos[0]}\n{Npos[1]}\n{Apos[0]}\n{Apos[1]}\n{Bpos[0]}\n{Bpos[1]}\n{Epos[0]}\n{Epos[1]}\n{Aamnt}\n{Bamnt}\n{Tframe}\n{Thold}\n{Textra}')
    file.close()

else:
    data = data.split('\n')
    Npos = float(data[0]), float(data[1])
    Apos = float(data[2]), float(data[3])
    Bpos = float(data[4]), float(data[5])
    Epos = float(data[6]), float(data[7])
    Aamnt = float(data[8])
    Bamnt = float(data[9])
    Tframe = float(data[10])
    Thold = float(data[11])
    Textra = float(data[12])
    extraClickPercentage = float(data[13])
def on_press(key):
    print("AMOUNT",Aamnt)
    global breaking
    if key == Key.alt:
        working = not working

    elif key == Key.ctrl_r:
        listener.stop()
        breaking = False
        exit()


def on_click(x, y, button, pressed):
    global allowed, working, count
    if allowed and pressed:
        print(x, y, working)
        for i in [Npos, Apos, Bpos, Epos]:
            if abs(x - i[0]) ** 2 + abs(y - i[1]) ** 2 > 90 ** 2:
                working = False

            else:
                count = 0
                working = True
                break

            print(abs(x - i[0]) ** 2 + abs(y - i[1]) ** 2)


working = True
breaking = True
allowed = True
Keyboard = Controller()
Mouse = Ct()

listener = Listener(on_press=on_press)
listener.start()

li = Li(on_click=on_click)
li.start()


def execute():
    global count, previous, allowed
    count += 1
    try:
        Keyboard.release(Key.ctrl)
    except:
        pass
    sleep(0.01)
    Keyboard.press(Key.ctrl)
    Keyboard.press('c')
    Keyboard.release('c')
    Keyboard.release(Key.ctrl)
    try:

        OpenClipboard()
        data = GetClipboardData()
        CloseClipboard()
        curent = float(data.replace(',', '').replace('\r', '').replace('\n', ''))
        if count == 1:
            previous = float(data.replace(',', '').replace('\r', '').replace('\n', ''))
            return 0
        print(curent)
        print(previous)
        print(curent - previous, Aamnt, Bamnt)
        if curent - previous >= Aamnt:
            print('A')
            allowed = False
            Mouse.position = Apos
            Mouse.click(Button.left, 1)
            exc = Thread(target=exception)
            exc.start()
            allowed = True

            sleep(Thold)
            count = 0

            allowed = False
            Mouse.position = Npos
            Mouse.click(Button.left, 3)
            actualBTC = (Npos + Aamnt - Textra) + extraClickPercentage * Textra;
            print("BTC AMOUNT: " + actualBTC)
            allowed = True

        elif curent - previous <= -Bamnt:
            print('B')
            allowed = False
            Mouse.position = Bpos
            Mouse.click(Button.left, 1)
            exc = Thread(target=exception)
            exc.start()
            actualBTC = (Npos + Aamnt - Textra) - extraClickPercentage*Textra;
            print("BTC AMOUNT: "+actualBTC)
            allowed = True

            sleep(Thold)
            count = 0

            allowed = False

            Mouse.position = Npos
            Mouse.click(Button.left, 3)

            allowed = True

        previous = curent
    except:
        pass


def exception():
    sleep(Textra)
    allowed = False
    Mouse.position = Epos
    Mouse.click(Button.left, 1)

    sleep(0.01)

    Mouse.position = Npos
    Mouse.click(Button.left, 3)

    allowed = True


count = 0
previous = 0.0
sleep(5)

while breaking:
    execute()
    if working:
        execute()
        try:
            sleep(Tframe)
        except:
            pass

