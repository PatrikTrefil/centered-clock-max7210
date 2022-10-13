# gpio pins are specified by the luma library
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop

def get_device():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=90,
                     rotate=2, blocks_arranged_in_reverse_order=True)
    return device
