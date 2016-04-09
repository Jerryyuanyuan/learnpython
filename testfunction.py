# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):

    for x in [a,b,c]:
      if not isinstance(x,(int,float)):
          raise TypeError('bad operand type')
      if a == 0:
          if b ==0:
             if c == 0:
                return 0
             else:
                return "无解"
          else:
             return -c/b
      else:
          if b*b-4*a*c < 0:
             return "无实数解"
          else:
             return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)