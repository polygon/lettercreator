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
    self.commands[self.time] = ('set', color)
    self.time += 10

  def fadeColor(self, color, time):
    speed = speedcalc(self.lastcolor, color, time)
    if speed > 1000:
      print('Warning, resulting speed is bigger than 1000')
      speed = 1000
    self.commands[self.time] = ('fade', color, speed)
    self.time += time

  def createCommands(self):
    cmds = {}
    for e in self.commands:
      time = e
      cmd = self.commands[time]
      if cmd[0] == 'set':
        cstring = 'C ' + self.id + ' ' + asciicolor(cmd[1])
      else:
        cstring = 'F ' + self.id + ' ' + asciicolor(cmd[1]) + ' ' + str(cmd[2])
      cmds[time] = cstring
    return cmds
