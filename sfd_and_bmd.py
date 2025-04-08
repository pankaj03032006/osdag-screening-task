import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('SFS_Screening_SFDBMD.xlsx')  # Make sure this file is in the same folder

# Define the correct column names
distance_col = 'Distance (m)'
shear_col = 'SF (kN)'
moment_col = 'BM (kN-m)'

# Extract data
distance = df[distance_col]
shear = df[shear_col]
moment = df[moment_col]

# Create the plot
plt.figure(figsize=(12, 5))

# Bending Moment Diagram
plt.subplot(1, 2, 1)
plt.plot(distance, moment, 'b-o', linewidth=2)
plt.title('Bending Moment Diagram')
plt.xlabel('Distance (m)')
plt.ylabel('BM (kN-m)')
plt.grid(True)

# Shear Force Diagram
plt.subplot(1, 2, 2)
plt.plot(distance, shear, 'r-x', linewidth=2)
plt.title('Shear Force Diagram')
plt.xlabel('Distance (m)')
plt.ylabel('SF (kN)')
plt.grid(True)

# Layout and show plot
plt.tight_layout()
plt.show()
