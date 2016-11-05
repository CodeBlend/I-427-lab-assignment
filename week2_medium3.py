#Find Angle MBC
#https://www.hackerrank.com/challenges/find-angle


# -*- coding: utf-8 -*-

import math

AB = int(raw_input())
BC = int(raw_input())

angle = round(math.degrees(math.atan2(AB, BC)))

print str(int(angle)) + "°"
