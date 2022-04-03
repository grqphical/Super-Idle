import threading as th
import keyboard
import pydirectinput

stopThread = False

def mainFunction():
    global stopThread
    i = 0
    while True:
        pydirectinput.typewrite('wasd', interval=0.5)
        i += 1
        if stopThread == True:
            break 

def main():
    scriptThread = th.Thread(target=mainFunction)
    print('Press SPACE to start. Press DEL to exit')
    keyboard.wait('space')
    scriptThread.start()
    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'delete':
            print('Ending Script')
            global stopThread
            stopThread = True
            scriptThread.join()
            break

if __name__ == '__main__':
    main()

            