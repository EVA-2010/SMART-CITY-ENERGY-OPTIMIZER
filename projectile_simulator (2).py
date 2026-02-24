import math

g = 9.8

velocity = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter launch angle (degrees): "))

angle_rad = math.radians(angle)

time = (2 * velocity * math.sin(angle_rad)) / g
range = (velocity**2 * math.sin(2 * angle_rad)) / g

print("Time of flight:", round(time, 2), "seconds")
print("Range:", round(range, 2), "meters")