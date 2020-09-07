# コッホ曲線
import math

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

p1 = Point(0, 0)
p2 = Point(100, 0)
sin60 = math.sin(math.radians(60))
cos60 = math.cos(math.radians(60))


def koch(d, a, b):
  if d == 0:
    return
  s_x = (2.0 * a.x + 1.0 * b.x) / 3.0
  s_y = (2.0 * a.y + 1.0 * b.y) / 3.0
  t_x = (1.0 * a.x + 2.0 * b.x) / 3.0
  t_y = (1.0 * a.y + 2.0 * b.y) / 3.0
  u_x = (t_x - s_x) * cos60 - (t_y - s_y) * sin60 + s_x
  u_y = (t_x - s_x) * sin60 + (t_y - s_y) * cos60 + s_y
  s = Point(s_x, s_y)
  t = Point(t_x, t_y)
  u = Point(u_x, u_y)

  koch(d-1, a, s)
  print(f"{s_x:.8f} {s_y:.8f}")
  koch(d-1, s, u)
  print(f"{u_x:.8f} {u_y:.8f}")
  koch(d-1, u, t)
  print(f"{t_x:.8f} {t_y:.8f}")
  koch(d-1, t, b)

print(f"{p1.x:.8f} {p1.y:.8f}")
N = int(input())
koch(N, p1,p2)
print(f"{p2.x:.8f} {p2.y:.8f}")