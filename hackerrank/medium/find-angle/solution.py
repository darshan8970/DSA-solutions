import math

ab = int(input())
bc = int(input())
mbc = round(math.degrees(math.atan(ab / bc)))
print(f"{mbc}\u00b0")
