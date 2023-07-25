import pyperclip
import time

prcc = ""

while True:

    while True:
        cucc = pyperclip.paste()

        if cucc != prcc:
            with open("clipboard.txt", 'a', encoding='utf-8') as file:
                file.write('\n' + cucc)
            prcc = cucc
        time.sleep(0.1)