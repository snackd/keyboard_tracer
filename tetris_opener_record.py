# https://pynput.readthedocs.io/en/latest/keyboard.html
from pynput import keyboard

class KeyboardTracer():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.TKI = 0
        self.SDPC = 0
        self.DPC = 0
        self.MKO = 0
        self.Satsuki = 0
        self.MS2 = 0

    def print_opener(self):
        print("---使用次數---")
        print("SDPC:", self.SDPC)
        print("DPC:", self.DPC)
        print("MKO:", self.MKO)
        print("Satsuki:", self.Satsuki)
        print("MS2:", self.MS2)

    def init_opener(self):
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

    def main(self):
        print("---Program Start---")

        # ...or, in a non-blocking fashion:
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

if __name__ == "__main__":
    k1 = KeyboardTracer()
    k1.main()

