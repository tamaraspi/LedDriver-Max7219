#This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.




import spidev
from enum import IntEnum


class LedDriver:
    def __init__(self):
        self.initialized = False
        self.rowValue = [0,0,0,0,0,0,0,0]
        try:
            self.maxdriver = Max7219Driver()
        except:
            print('Error in LedDriver: Could not create SPI driver. Try using sudo')
            return
        self.initialized = True
        self.maxdriver.enableTestMode(False)
        self.maxdriver.setScanLimit(7)
        self.setIntensity(3)
        self.clear()
        self.maxdriver.setPowerMode(True)
        

    def clear(self):
        """Turns off all LEDS of the display"""
        if self.initialized:
            self.rowValue = [0,0,0,0,0,0,0,0]
            for n in range(0, 8):
                self.maxdriver.setDigit(n, 0)

    def setLed(self, row, col, enable):
        """Turns a single LED on or off"""
        if self.initialized:
            if enable: self.rowValue[row] |= (1 << col)
            else: self.rowValue[row] &= ~(1 << col)
            self.maxdriver.setDigit(row, self.rowValue[row])

    def setRow(self, row, value):
        """Turns LEDs on a single row on or off"""
        if self.initialized:
            self.rowValue[row] = value
            self.maxdriver.setDigit(row, self.rowValue[row])

    def setIntensity(self, value):
        """Set the brightness of the display. 0 = lowest, 15 = highest"""
        if self.initialized:
            self.maxdriver.setIntensity(value)




class Max7219Driver:
    def __init__(self):
        self.spi = self.__initSpi()

    def enableTestMode(self, enable):
        self.__set(self.spi, Max7219Driver.Reg.DisplayTest, enable)

    def setPowerMode(self, enable):
        self.__set(self.spi, Max7219Driver.Reg.Shutdown, enable)

    def setScanLimit(self, value):
        self.__set(self.spi, Max7219Driver.Reg.ScanLimit, value)

    def setDigit(self, digit, value):
        if digit < 0: digit = 0
        if digit > 7: digit = 7
        self.__set(self.spi, digit + 1, value)

    def setIntensity(self, value):
        self.__set(self.spi, Max7219Driver.Reg.Intensity, value)

    def __set(self, spi, address, value):
        spi.xfer([address & 0x0f, value & 0xff])

    def __initSpi(self):
        spi = spidev.SpiDev()
        spi.open(0, 0)
        spi.max_speed_hz = 100000
        return spi

    class Reg(IntEnum):
        DecodeMode = 9
        Intensity = 10
        ScanLimit = 11
        Shutdown = 12
        DisplayTest = 15

