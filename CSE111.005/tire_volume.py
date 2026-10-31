from datetime import datetime
import math

width = int(input("Enter the width of the tire in mm(ex 205) "))

a_ratio = int(input("Enter the aspect ratio of the tire (ex 60) "))

diameter = int(input("Enter the diameter of the wheel in inches (ex 15) "))

volume = math.pi * (width ** 2) * a_ratio * (width * a_ratio + 2540 * diameter) / 10 ** 10

print(f"The approximate volume is {volume:.2f} liters")
