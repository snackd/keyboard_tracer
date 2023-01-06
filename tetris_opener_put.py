# https://pynput.readthedocs.io/en/latest/keyboard.html
from pynput import keyboard
import pyautogui
import time

class KeyboardTracer():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.PCO = 0
        self.TKI = 0
        self.SDPC = 0
        self.DPC = 0
        self.MKO = 0
        self.Satsuki = 0
        self.MS2 = 0
        self.key = keyboard.Controller()
        self.gap = 0.001

    def print_opener(self):
        print("---使用次數---")
        print("SDPC:", self.SDPC)
        print("DPC:", self.DPC)
        print("MKO:", self.MKO)
        print("Satsuki:", self.Satsuki)
        print("MS2:", self.MS2)

    def init_opener(self):
        self.PCO = 0
        self.TKI = 0
        self.SDPC = 0
        self.DPC = 0
        self.MKO = 0
        self.Satsuki = 0
        self.MS2 = 0

    def on_press(self, key):
        try:
            if key == keyboard.Key.f1:
                self.TKI += 1
            if key == keyboard.Key.f2:
                self.SDPC += 1
            if key == keyboard.Key.f3:
                self.MKO += 1
            if key == keyboard.Key.f4:
                self.Satsuki += 1
            if key == keyboard.Key.f5:
                self.MS2 += 1
            if key == keyboard.Key.f6:
                self.DPC += 1
        except AttributeError:
            print('special key pressed: {0}'.format(
                key))

    def on_release(self, key):
        if key == keyboard.Key.shift_l:
            self.print_opener()
        elif key == keyboard.Key.shift_r:
            self.init_opener()

        if key == keyboard.Key.ctrl_l:
            self.PCO = 1
        if key == keyboard.Key.ctrl_r:
            self.PCO = 0

        if self.PCO:
            print(key)
            if key == keyboard.KeyCode.from_char('t'):
                self.T_move()
            elif key == keyboard.KeyCode.from_char('s'):
                self.S_move()
            elif key == keyboard.KeyCode.from_char('d'):
                self.Z_move()
            elif key == keyboard.KeyCode.from_char('i'):
                self.I_move()
            elif key == keyboard.KeyCode.from_char('j'):
                self.J_move()
            elif key == keyboard.KeyCode.from_char('l'):
                self.L_move()
            elif key == keyboard.KeyCode.from_char('o'):
                self.O_move()

    def main(self):
        print("---Program Start---")

        # ...or, in a non-blocking fashion:
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

    def PCO_opener(self):
        # print("opener")
        self.T_move()
        # self.S_move()
        # self.Z_move()
        # self.O_move()
        # self.I_move()
        # self.J_move()
        # self.L_move()

    def T_move(self):
        pyautogui.press('up')
        pyautogui.press('left', 4, self.gap)
        pyautogui.press('space')

    def S_move(self):
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
        pyautogui.press('left', 2, self.gap)
        pyautogui.press('space')

    def Z_move(self):
        pyautogui.press('left', 3, self.gap)
        pyautogui.press('space')

    def I_move(self):
        pyautogui.press('right')
        pyautogui.press('up')
        pyautogui.press('space')

    def L_move(self):
        # pyautogui.press('a')
        # self.key.press('a')
        pyautogui.press('right', 4, self.gap)
        pyautogui.press('space')

    def J_move(self):
        # self.key.press('a')
        # pyautogui.press('a')
        pyautogui.press('right', 4, self.gap)
        pyautogui.press('space')

    def O_move(self):
        pyautogui.press('right', 3, self.gap)
        pyautogui.press('space')


if __name__ == "__main__":
    k1 = KeyboardTracer()
    k1.main()




