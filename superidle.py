import threading as th
import keyboard
import pydirectinput
import click
import time


# Basic variables
stopThread = False
timedRun = False
timedAmount = 5

# This is the function that does the inputs
def mainFunction():
    global stopThread
    # Checks if the user used the timed run option if so, runs a for loop rather than a while loop
    if timedRun:
        for i in range(timedAmount):
            pydirectinput.typewrite('wasd', interval=0.5)
            time.sleep(1)
        print('Script Finished. Press DEL to exit the process')
        return
    else:
        i = 0
        while True:
            pydirectinput.typewrite('wasd', interval=0.5)
            i += 1
            if stopThread == True:
                break 
# Uses click for CLI options
@click.command()
@click.option('--timed', default=5, show_default=True, help='Set a certain amoutn of seconds for the script to run')
def main(timed):
    # Checks if the user used the timed option and sets the variables accordingly
    if timed != None:
        global timedRun, timedAmount
        timedRun = True
        timedAmount = timed
    # Creates a thread to run the input function on
    scriptThread = th.Thread(target=mainFunction)
    print('Press SPACE to start. Press DEL to exit')
    keyboard.wait('space')
    time.sleep(1)
    scriptThread.start()
    # Main loop
    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        # If the user pressed delete then stop the script
        if event.event_type == keyboard.KEY_DOWN and event.name == 'delete':
            print('Ending Script')
            global stopThread
            stopThread = True
            scriptThread.join()
            break


if __name__ == '__main__':
    main()

            