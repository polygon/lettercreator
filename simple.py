from colorstream import ColorStream
from utils import *

# First letter starts black, then fades red, white, green, black
C1 = ColorStream('1')
C1.setColor((0,0,0))
C1.wait(1000)
C1.fadeColor((255,0,0),2000)
C1.fadeColor((255,255,255),4000)
C1.fadeColor((0,255,0),1000)
C1.fadeColor((0,0,0),8000)
C1.setColor((0,0,0))

# The other letters do the same, just with different timings
C2 = ColorStream('2')
C2.setColor((0,0,0))
C2.wait(2000)
C2.fadeColor((255,0,0),3000)
C2.fadeColor((255,255,255),1000)
C2.fadeColor((0,255,0),2000)
C2.fadeColor((0,0,0),5000)
C2.setColor((0,0,0))

C3 = ColorStream('3')
C3.setColor((0,0,0))
C3.wait(500)
C3.fadeColor((255,0,0),8000)
C3.fadeColor((255,255,255),5000)
C3.fadeColor((0,255,0),1000)
C3.fadeColor((0,0,0),6000)
C3.setColor((0,0,0))

# Interweave (serialize) this commands
final = interweave(C1.commands, C2.commands)
final = interweave(final, C3.commands)

# Finally generate the program (this will insert wait-
# instructions and write the program to stdout)
makeprogram(final)
