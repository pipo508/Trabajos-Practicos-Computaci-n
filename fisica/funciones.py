import math

ira = 1.33
irb = 1.52
ta_g = 60
ta_r = (ta_g * math.pi) / 180
tb_r = (ira / irb) * math.sin(ta_r)
tb_g = (tb_r * 180) / math.pi
print(tb_g)