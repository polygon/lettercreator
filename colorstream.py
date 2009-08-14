from utils import speedcalc
from utils import asciicolor

class ColorStream:
  def __init__(self, id):
    self.time = 0
    self.commands = {}
    self.lastcolor = (0,0,0)
    self.id = id

  def wait(self, time):
    self.time += time

  def setColor(self, color):
    self.commands[self.time] = 'C ' + self.id + ' ' + asciicolor(color)
    self.time += 10

  def fadeColor(self, color, time):
    speed = speedcalc(self.lastcolor, color, time)
    if speed > 1000:
      print('# Warning, resulting speed is bigger than 1000')
      speed = 1000
    self.commands[self.time] = 'F ' + self.id + ' ' + asciicolor(color) + ' ' + str(speed)
    self.time += time
