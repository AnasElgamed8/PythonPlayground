from pynput import keyboard
import time

hand = keyboard.Controller()
working=0


def on_press(key):
    global working

    if (key==keyboard.Key.end):
        working=(working+1)%2


def on_release(key):

    if key == keyboard.Key.esc:
        return False
    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while(True):
        time.sleep(3)
        while(working):
            time.sleep(0.2)
            hand.press(key=keyboard.Key.tab)
            hand.release(key=keyboard.Key.tab)
            time.sleep(0.2)
            hand.press(key=keyboard.Key.space)
            hand.release(key=keyboard.Key.space)
    listener.join()h