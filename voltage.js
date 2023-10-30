Screen 12
minx = -10
miny = -10
maxx = 10
maxy = 15
ar = .75

Window (minx, miny * ar)-(maxx, maxy * ar)
q = 5
qx = 1
qy = 0
x = -2
y = -6
k = 1
Locate 1, 1

For i = 1 To 10000000
  x = 20 * Rnd(1)-10
  y = 20 * Rnd(1)-10
  dx = x - qx
  dy = y - qy
  r = ((dx ^ 2) + (dy ^ 2))^0.5
  v = (k *q)/r
  Circle(qx, qy), .1, 1
  PSet(x, y), v * 10
  Locate 1, 1
Next i
