import matplotlib.pyplot as plt
import math

g = 9.81 # Standard gravity (m/s^2)

print("Engineering Projectile Simulator v1.0")
print("-------------------------------------")

while True:
    try:
       # 1. Inputs (Initial Conditions)

      v0 = float(input("\nEnter " \
      "initial velocity (m/s): "))
    angle = float(input("Enter " \
       "launch angle (degrees): "))
      except Valueerror:
 print("Error: Please enter numerical values. ")
         continue
      
       
         
         angel_rad = math.radians(angle)

         # 2. Calculate Total Flight Time
         # Formula: t = (2 * v0 *
 sin(theta)) / g
     total_time = (2 * v0 *
 math.sin(angle_rad)) / g

      x_values = []
      y_values = []
      t = 0

      # 3. Dynamic Time-Step (Ensures 100 points for a smooth curve)
      dt = total_time / 100 if
  total_time > 0 else 0.1

      # 4. Numerical Integration Loop 
    while t <= total_time:
        x = v0 * math.cos(angle_rad)
     * t
         y = v0 * math.sin(angle_rad) *
      t - 0.5 * g * t**2

      # Ground constraint
      (preventing negative height)   
              if y < 0: y = 0

              x_values.append(x)
              y_values.append(y)   
              t += dt  

      # 5. Data Visualization
      (The Graph)   
            plt.figure(figsize=(10, 6))  
            plt.plot(x_values, y_values,
        label=f"Trajectory: {v0}m/s at {angle}  
        ˚", color='blue', linewidth=2)

             plt.title("Projectile Motion Simulation", fontsize=14)
             plt.xlabel("Horizontal Distance (m)")  
             plt.ylabel1("Vertical Height (m)")
             plt.axhline(0, color= 'black',)
        linewidth=1.5 # The Ground
             plt.grid(True, linestyle='--',
        alpha=0.6)
             plt.legend()

             print("Generating graph... Close window to restart.")
             plt.show()
             
             if input("\nRun another simulation? (y/n): ").lower() 1= 'y':
                      break                 
       

