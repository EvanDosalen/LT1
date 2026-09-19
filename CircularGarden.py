#Author: Evan Jane L. Dosalen
#Date: September 19, 2026

import math

radius=float(input("Please enter the radius of the circular garden: "))

area=math.pi + math.pow(radius,2)
circumference=2*math.pi*radius
areaSquareRoot=math.sqrt(area)
areaRoundedDown=math.floor(area)
areaRoundedUp=math.ceil(area)

print(f"Area of the circular garden is: {area:.f}")
print(f"Circumference of the circular garden is: {circumference:.f}")
print(f"Square root of area of the circular garden is: {areaSquareRoot:.f}")
print(f"Area rounded down of the circular garden is: {areaRoundedDown:.f}")
print(f"Area rounded up of the circular garden is: {areaRoundedUp:.f}")



