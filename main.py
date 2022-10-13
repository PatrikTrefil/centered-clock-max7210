#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import datetime
import os

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from monospace_numbers import monospace_numbers


def clock():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    # made for 4 cascaded displays
    device = max7219(serial, cascaded=4, block_orientation=90,
                     rotate=2, blocks_arranged_in_reverse_order=True)

    # choose from 0 to 15
    intensity = 1
    device.contrast(intensity * 16)

    # select font and starting pos based on chosen font
    fontIndex = 0
    if (fontIndex == 0):
        selFont = monospace_numbers(LCD_FONT)
        pos = (2, 0)
    elif (fontIndex == 1):
        selFont = monospace_numbers(CP437_FONT)
        pos = (1, 0)
    elif (fontIndex == 2):
        selFont = monospace_numbers(SINCLAIR_FONT)
        # no perfect position exists
        pos = (3, 0)

    # display time in selected font
    while True:
        with canvas(device) as draw:
            curr_time = datetime.datetime.now()

            hours = curr_time.strftime("%H")
            minutes = curr_time.strftime("%M")
            
            text(draw, (2, 0),hours, fill="white", font=selFont)
            text(draw, (19, 0),minutes, fill="white", font=selFont)
            # draw colon (:)
            draw.rectangle((8 * 2 - 1, 1, 8 * 2, 2), fill="white")
            draw.rectangle((8 * 2 - 1, 4, 8 * 2, 5), fill="white")

        # sleep for 10 seconds between updates
        time.sleep(10)





if __name__ == "__main__":
    try:
        clock()
    except KeyboardInterrupt:
        pass
