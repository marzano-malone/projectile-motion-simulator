import math 

g= 9.8

print("Projectile Motion Simulator")
print("---------------------------")

while True:
 velocity = float(input("\nEnter velocity (m/s): "))
 angle = float(input("Enter angle (degrees): "))

 angle_rad = math.radians(angle)



 time = (2 * velocity * math.sin(angle_rad)) / g
 range_distance = (velocity**2 * math.sin(2 * angle_rad)) / g
 height = (velocity**2 * (math.sin(angle_rad))**2) / (2 * g)

 print("\n--- Results ---")
 print(f"Time in air: {time:.2f} seconds")
 print(f"Range: {range_distance:.2f} meters")
 print(f"Maximum height: {height:.2f} meters")

 again = input("\nRun again? (y/n): ")
 if again. lower() != 'y':
    break
