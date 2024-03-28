
from inputimeout import inputimeout, TimeoutOccurred
import time
import pyautogui
import threading
import os


current_state = False
action = False
status = False
exit_state = False

def crafting():
    global action
    global status
    while(True):
        print()
        for i in range(5,0,-1):
            print("crafting will start in", i ,"second")
            time.sleep(1)
            1
        for i in range(0,4):
            pyautogui.press('f12')
            time.sleep(1)
            print("spaming confirm...")
        
        pyautogui.press('1')
        for i in range(40):
            print("Crafting is on progress...")
            time.sleep(1)
        print("Prepare for everything done!")
        time.sleep(5)
        print("finish crafting")
        
def change_state():
    global current_state
    current_state = not current_state
    
def change_Exit_state():
    global exit_state
    exit_state = not exit_state
    print(exit_state)


def check_exit():
    while(True):
        try:
            print()
            exit = inputimeout(prompt='Press any key to exit any time', timeout=54)
            if(exit):
                change_Exit_state()
                break
        except TimeoutOccurred:
            continue
    return 



def main():
    input("Press any key to continue...")
    change_state()
    while(True):
        if(current_state):
            craft = threading.Thread(target=crafting)
            exit_check = threading.Thread(target=check_exit)
            change_state()
            exit_check.start()
            craft.start()
           
        if(exit_state):
            print("exit")
            os._exit(1)
main()
