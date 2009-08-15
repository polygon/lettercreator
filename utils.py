def interweave(in1, in2, maxdelay=100):
  a = in1[:]
  b = in2[:]
  r = {}
  a_keys = a.keys()
  a_keys.sort()
  b_keys = b.keys()
  b_keys.sort()

  while (len(a_keys) > 0) or (len(b_keys) > 0):
    if (len(a_keys) > 0) and (len(b_keys) > 0):
      if a_keys[0] < b_keys[0]:
        time = a_keys.pop(0)
        value = a[time]
      else:
        time = b_keys.pop(0)
        value = b[time]
    elif len(a_keys) > 0:
      time = a_keys.pop(0)
      value = a[time]
    else:
      time = b_keys.pop(0)
      value = b[time]

    otime = time
    while r.keys().count(time) > 0:
      time = time + 10
      if time - otime > maxdelay:
        raise RuntimeError('Timeindex had to be moved further than maxdelay')

    r[time] = value

  return r

def speedcalc(color1, color2, time):
  factor = 256000 / 144.0 # The magic Speed-Time translation factor
  length = max(abs(color1[0]-color2[0]), abs(color1[1]-color2[1]), abs(color1[2]-color2[2]))
  speed = int((length * factor) / time)
  return speed

def asciicolor(color):
  colstr = '#'
  for c in color:
    colstr += hex(c / 16)[2]
    colstr += hex(c % 16)[2]
  return colstr

def makeprogram(cmdlist):
  times = cmdlist.keys()
  times.sort()
  lasttime = times[0]
  times.pop(0)
  for time in times:
    print(cmdlist[lasttime])
    if (time - lasttime) > 29:
      print('W ' + str(time - lasttime - 20))
    lasttime = time
