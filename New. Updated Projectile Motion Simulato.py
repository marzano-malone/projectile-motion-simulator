import matplotlib.pyplot as plt
import math 

g = 9.81 # Standard gravity

print("Engineering Projectile Simulator v1.0")
print("-------------------------------------")

while True:
    # 1. Inputs
    try:
      velocity = float(input("\nEnter velocity (m/s): "))
      angle = float(input("Enter angle (degrees): "))
    except ValueError:
      print("Please enter numbers only.")
    continue

    # 2. Setup Variables (MUST happen before the loop)
    angle_rad = math.radians(angle)
    total_time = (2 * velocity * math.sin(angle_rad)) / g

    x_values = []
    y_values = []
    t = 0
    dt = 0.05 #The 'time step' - smaller means a smoother curve

    print("--- DEBUG 1: Starting the Physics Loop ---")

    # 3. The Physics Engine (The Loop)
    while t <= total_time:
     x = velocity * math.cos(angle_rad) * t
     y = velocity * math.sin(angle_rad) * t - 0.5 * g * t**2

    # Don't let the projectile go below ground level
    if y < 0: y = 0

    x_values.append(x)
    y_values.append(y)

    t += dt # This moves the clock forward

    print(f"--- DEBUG 2: Physics Loop Finished! Total points: {len(x_values)} ---")

    # 4. Data Visualization (The Graph)
    print("--- DEBUG 3: Opening Graph Window now... ---")
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, color='blue', linewidth=2)
    plt.title(f"Projectile Trajectory ({velocity} m/s at {angle} degrees)")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.grid(True)
    plt.show() # <--- This will pause the script until you close the window

    #5 Exit Check
    again = input("\Run again? (y/n): ")
    if again.lower() != 'y':
     break


    print("Program closed. Good luck with your scholarship!")