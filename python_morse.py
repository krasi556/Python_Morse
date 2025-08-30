from pynput import keyboard
import time

morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
              '.-.': 'R',
              '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
              '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4','.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9'}

class InputListener:
    def __init__(self):
        self.space_time = None
        self.press_time = None
        self.sentence = ''
        self.final_sentence = []

    def on_press(self,key):
        if key == keyboard.Key.space and self.press_time is None:
            self.press_time = time.time()

    def on_release(self,key):
        if key == keyboard.Key.space and self.press_time is not None:
            duration = time.time() - self.press_time
            if duration < 0.3:
                self.sentence += ('.')
                print('.',end = '')
            elif 0.3 <= duration <= 0.9:
                self.sentence += ('-')
                print('-', end='')
            else:
                self.space_and_seperate()
            self.press_time = None

        elif key == keyboard.Key.enter:
            space_time = time.time()
            if self.space_time is not None and space_time - self.space_time <= 0.3:
                self.final_sentence.append(' ')
                print('Word separator added ')
                self.sentence = ''
                self.space_time = None
                
            else:
                self.space_and_seperate()
                print(f'Sentence: {"".join(self.final_sentence)}\n')
                self.space_time = space_time

        elif key == keyboard.Key.esc:
            print(f'The sentence is: {"".join(self.final_sentence)}\nExiting.....')
            exit()
    def space_and_seperate(self):
        if self.sentence:
            is_found = False
            for code in morse_code:
                if self.sentence == code:
                    letter = morse_code[code]
                    self.final_sentence.append(letter)
                    is_found = True
                    break
            if not is_found:
                letter = '?'
                self.final_sentence.append(letter)
            print(f'Letter: [{letter}]\n')
            self.sentence = ''
listener = InputListener()

print('This script is a Morse code interpreter using the spacebar to input Morse\nIf the duration is < 0.3 seconds, it\''
      's a dot (.)\nIf the duration is between 0.3 and 0.9 seconds, it\'s a dash (-)\nIf the duration is > 0.9 seconds,'
      ' it\'s treated as a space between letters, and the current Morse code string is translated.\n\nPressing Enter'
      ' translates the current Morse character (if any) and prints the full sentence so far\nPressing Esc ends the'
      ' program and prints the final sentence')

with keyboard.Listener(on_press = listener.on_press,on_release = listener.on_release) as l:
    l.join()
