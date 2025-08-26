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
        self.sentence = []
    def on_press(self,key):
        if key == keyboard.Key.space and self.press_time is None:
            self.press_time = time.time()

    def on_release(self,key):
        if key == keyboard.Key.space and self.press_time is not None:
            duration = time.time() - self.press_time
            if duration < 0.3:
                self.sentence.append('.')
            elif 0.3 <= duration <= 0.9:
                self.sentence.append('-')
            else:
                self.sentence.append(' ')

    def on_esc(self,key):
        pass

    def on_enter(self,key):
        pass

listener = InputListener()

with keyboard.Listener(on_press = listener.on_press,on_release = listener.on_release) as l:
    l.join()
