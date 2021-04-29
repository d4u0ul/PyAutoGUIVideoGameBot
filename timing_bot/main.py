import pyautogui
import time
# Press Ctrl+F8 to toggle the breakpoint.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def holdKey(key, seconds =1.00):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key )
    time.sleep(DELAY_BETWEEN_COMANDS)

def initializePyAutoGUI():
    #Initialized PyautoGUI
    pyautogui.FAILSAFE = True

def  countdownTimer():
    #Countdown timer
    print("Starting")
    for i in range(0,5):
        print(".", end="")
        time.sleep(1)
    print("Go")

def main():
    initializePyAutoGUI()
    countdownTimer()
    #Move backwards
    holdKey('s',6.00)
    #Face the entrance
    holdKey('a',0.10)

    #Done
    print("done")
DELAY_BETWEEN_COMANDS=1.00

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
