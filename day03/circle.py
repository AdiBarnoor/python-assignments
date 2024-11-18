import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('radius',type=int)
args = parser.parse_args()

area = math.pi* args.radius * args.radius
circumference = math.pi * 2 * args.radius

print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")