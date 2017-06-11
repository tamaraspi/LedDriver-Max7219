#!/usr/bin/python3

from leddriver import LedDriver
import time

 
def main():
    print('Create the driver object')
    driver = LedDriver()
    time.sleep(3)

    print('Turn on the led with row number 3 and column number 5')
    driver.setLed(3, 5, True)
    time.sleep(3)

    print('Turn the led off')
    driver.setLed(3, 5, False)
    time.sleep(3)

    print('Move a dot over the display')
    for col in range(0, 8):
        for row in range(0, 8):
            driver.setLed(row, col, True)
            time.sleep(0.03)
            driver.setLed(row, col, False)
    time.sleep(3)
    
    print('Turn all leds on')
    for row in range(0, 8):
        driver.setRow(row, 0xFF)
    time.sleep(3)
    
    print('Change the brightness')
    for m in range(0, 5):
        for n in range(0, 16, 1):
            driver.setIntensity(n)
            time.sleep(0.01)   
        for n in range(15, -1, -1):
            driver.setIntensity(n)
            time.sleep(0.01)   
    time.sleep(3)
    
    print('Turn all leds off')
    driver.clear()
   
    print('Done')


if __name__ == "__main__":
    main()



