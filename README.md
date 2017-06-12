# LedDriver-Max7219
Python driver for DotLedMatrix based on Max7219



Enable the SPI bus on the Raspberry-pi with:
sudo raspi-config

Check that the file /boot/config.txt contains the statement 'dtparam=spi-on'

Make sure Python has the driver for SPI with:
python3 -m pip install spidev

Connect the LedMatrix board to the Raspberry-pi:

MOSI (data-in)    Pin-19

SCLK    					Pin-23

CE0 (chip select)	Pin-24

VCC (5V)	   			Pin-02

GND     					Pin-06



Test demo:

sudo python3 demo.py
