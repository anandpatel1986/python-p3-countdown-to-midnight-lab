# your code goes here!

def countdown (count):    
    while(count > 0):
        print(f"{count} SECOND(S)!")
        count= count-1
    print("HAPPY NEW YEAR!")
import time
def countdown_with_sleep (count):
    while ( count > 0):
        print(f"{count} SECOND(S)!")
        time.sleep(1)
        count= count-1
    print("HAPPY NEW YEAR!")

countdown_with_sleep (5)