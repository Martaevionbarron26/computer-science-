from adafruit_circuitplayground import cp
import time


while True:
    temp_c = cp.temperature
    if temp_c < 78:
        cp.pixels[0] = (0,0,1)
    if temp_c > 78:
        cp.pixels[1] = (0,0,1)
    if temp_c > 79:
        cp.pixels[2] = (0,0,1)
    if temp_c > 80:
        cp.pixels[3] = (1,1,0)
    if temp_c > 81:
        cp.pixels[4] = (1,1,0)
    if temp_c > 82:
        cp.pixels[5] = (1,1,0)
    if temp_c > 83:
        cp.pixels[6] = (1,1,0)
    if temp_c > 84:
        cp.pixels[7] = (1,0,0)
    if temp_c > 85:
        cp.pixels[8] = (1,0,0)
    if temp_c < 86:
        cp.pixels[9] = (1,0,0)
    else:
        cp.pixels.fill ((0,0,0))
    time.sleep(0.238)
    