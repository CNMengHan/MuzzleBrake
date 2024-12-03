from pynput.mouse import Listener
import threading
import ctypes
import time


MOUSEEVENTF_MOVE = 0x0001
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
user32 = ctypes.windll.user32

left_pressed = False
right_pressed = False

run = False
print("Ready...")


def px(y_distance):
    user32.mouse_event(MOUSEEVENTF_MOVE, 0, y_distance, 0, 0)


def on_click(x, y, button, pressed):
    global left_pressed, right_pressed, run

    if button == button.left:
        left_pressed = pressed
    elif button == button.right:
        right_pressed = pressed

    if left_pressed and right_pressed and not run:
        run = True
        threading.Thread(target=main).start()
    elif not (left_pressed and right_pressed) and run:
        run = False


def main():
    global run
    while run:
        px(4)
        time.sleep(0.011)


with Listener(on_click=on_click) as listener:
    listener.join()
