from pynput import keyboard
import time

morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
              '.-.': 'R',
              '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
              '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4','.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9'}

text = input()
class InputListener:
    def __init__(self):
        self.press_time = None

    def on_press(self,key):
        if key == keyboard.Key.space and self.press_time is None:
            self.press_time = time.time()

    def on_release(self,key):
        if key == keyboard.Key.space and self.press_time is not None:
            duration = time.time() - self.press_time
            

listener = InputListener()

with keyboard.Listener(on_press = listener.on_press,on_release = listener.on_release) as l:
    l.join()
