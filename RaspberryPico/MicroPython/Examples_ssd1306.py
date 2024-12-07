# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ssd1306-oled-micropython/

from machine import Pin, SoftI2C
import ssd1306

#You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
display1 = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=0x3c)
display2 = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=0x3d)

display1.fill(0)                         # fill entire screen with colour=0
display1.pixel(0, 10)                    # get pixel at x=0, y=10
display1.pixel(0, 10, 1)                 # set pixel at x=0, y=10 to colour=1
display1.hline(0, 8, 4, 1)               # draw horizontal line x=0, y=8, width=4, colour=1
display1.vline(0, 8, 4, 1)               # draw vertical line x=0, y=8, height=4, colour=1
display1.line(0, 0, 127, 63, 1)          # draw a line from 0,0 to 127,63
display1.rect(10, 10, 107, 43, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
display1.fill_rect(10, 10, 107, 43, 1)   # draw a solid rectangle 10,10 to 117,53, colour=1
display1.text('Hello World', 30, 0, 1)    # draw some text at x=0, y=0, colour=1

if False:
    display.scroll(20, 0)                   # scroll 20 pixels to the right
    display.fill_rect(0,0,19,63,0)

# draw another FrameBuffer on top of the current one at the given coordinates
import framebuf
fbuf = framebuf.FrameBuffer(bytearray(8 * 8 * 1), 8, 8, framebuf.MONO_VLSB)
fbuf.line(0, 0, 7, 7, 1)
#display1.blit(fbuf, 10, 10, 0)           # draw on top at x=10, y=10, key=0
display1.show()

display1.contrast(255)
 
if True:
    display2.fill(0)
    display2.fill_rect(0, 0, 32, 32, 1)
    display2.fill_rect(2, 2, 28, 28, 0)
    display2.vline(9, 8, 22, 1)
    display2.vline(16, 2, 22, 1)
    display2.vline(23, 8, 22, 1)
    display2.fill_rect(26, 24, 2, 4, 1)
    display2.text('MicroPython', 40, 0, 1)
    display2.text('SSD1306', 40, 12, 1)
    display2.text('OLED 128x64', 40, 24, 1)
    display2.show()



