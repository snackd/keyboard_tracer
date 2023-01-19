from pynput import keyboard
from termcolor import cprint


class KeyboardTracer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.flag = 1

    def on_press(self, key):
        try:
            print('Alphanumeric key pressed: {0} '.format(
                key.char))
        except AttributeError:
            print('special key pressed: {0}'.format(
                key))

    def on_release(self, key):
        print('Key released: {0}'.format(
            key))
        if key == keyboard.Key.esc:
            self.flag = 0
            cprint("Release ESC, Stop Listener", "red")
            # Stop listener
            return False

    def collector(self):
        # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

    def main(self):
        print("-"*10)
        cprint("Program Start", "green")
        print("-"*10)

        # ...or, in a non-blocking fashion:
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()


if __name__ == "__main__":
    k = KeyboardTracer()
    k.main()

    while k.flag:
        pass

    print("-"*10)
    cprint("End Program", "green")
    print("-"*10)
