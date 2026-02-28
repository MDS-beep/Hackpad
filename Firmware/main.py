import time
import board
import digitalio
import neopixel
from adafruit_matrixkeypad import Matrix_Keypad

# =========================
# MATRIX PINS 
# =========================

rows = [
    digitalio.DigitalInOut(board.A0),  # row0
    digitalio.DigitalInOut(board.A1),  # row1
    digitalio.DigitalInOut(board.A2),  # row2
    digitalio.DigitalInOut(board.A3),  # row3
]

cols = [
    digitalio.DigitalInOut(board.D6),   # column0
    digitalio.DigitalInOut(board.RX),   # column1
    digitalio.DigitalInOut(board.SCK),  # column2
    digitalio.DigitalInOut(board.MISO), # column3
]

# =========================
# KEY LAYOUT (4x4)
# =========================

keys = (
    (1,  2,  3,  4),
    (5,  6,  7,  8),
    (9, 10, 11, 12),
    (13,14, 15, 16),
)

keypad = Matrix_Keypad(rows, cols, keys)

# =========================
# NEOPIXELS (16 SK6812)
# =========================

NUM_PIXELS = 16
PIXEL_PIN = board.D10   # change if your LED pin is different

pixels = neopixel.NeoPixel(
    PIXEL_PIN,
    NUM_PIXELS,
    brightness=0.3,
    auto_write=False
)

# =========================
# STARTUP ANIMATION
# =========================

for i in range(NUM_PIXELS):
    pixels[i] = (0, 0, 50)
    pixels.show()
    time.sleep(0.03)

time.sleep(0.3)
pixels.fill((0, 0, 0))
pixels.show()

# =========================
# MAIN LOOP
# =========================

while True:
    pressed_keys = keypad.pressed_keys

    if pressed_keys:
        key = pressed_keys[0]
        index = key - 1

        print("Pressed:", key)

        # Light up corresponding LED
        pixels.fill((0, 0, 0))
        pixels[index] = (0, 255, 100)
        pixels.show()

        # Example macro actions
        # You can change these:
        if key == 1:
            print("Macro 1")
        elif key == 2:
            print("Macro 2")
        elif key == 3:
            print("Macro 3")
        elif key == 4:
            print("Macro 4")

        time.sleep(0.2)

    else:
        pixels.fill((0, 0, 0))
        pixels.show()

    time.sleep(0.01)