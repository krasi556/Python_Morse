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

def on_press(key):
    pass

def on_release(key):
    pass

with keyboard.Listener(on_press,on_release) as listener:
    listener.join()
