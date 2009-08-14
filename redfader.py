from colorstream import ColorStream
from utils import *
from random import *

def genRandomStream(cs, length, col):
  cs.setColor((128 * (col & 1),128 * ((col / 2) & 1),128 * ((col / 4) & 1)))
  cs.wait(1000)
  lastval = 128
  while cs.time < length:
    nextval = randint(max(0, lastval - 128), min(255, lastval + 128))
    time = randint(1000, 1500)
    cs.fadeColor((nextval * (col & 1), nextval * ((col / 2) & 1) / 2, nextval * ((col / 4) & 1)), time)
    lastval = nextval

def genHighlights(cs, length):
  while cs.time < length:
    cs.wait(randint(5000, 10000))
    cs.fadeColor((0,255,255), 100)

# Orange wobbling stuff, individual for each LED
seed()
ids = list('ABCDEFGHIJKLMNO')
final = {}
for id in ids:
  stream = ColorStream(id)
  genRandomStream(stream, 110000, 3)
  final = interweave(final, stream.commands)

# Blueish highlights
ids = list('123')
for id in ids:
  stream = ColorStream(id)
  genHighlights(stream, 110000)
  final = interweave(final, stream.commands)
makeprogram(final)
