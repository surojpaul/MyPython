import numpy as np 
import matplotlib.pyplot as plt
# Data as Numpy Arrays
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
pm25_levels = np.array([95, 105, 98, 100, 105, 97])
stubble_burning_incidents = np.array([80, 95, 75, 60, 55, 45])
who_threshold = np.array([5])
# Compute the correlation coefficient between PM2.5 levels and stubble burning incidents
correlation = np.corrcoef(pm25_levels, stubble_burning_incidents)[0, 1]
# Plotting
fig, ax1 = plt.subplots()
# Primary Axis: PM2.5
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('PM2.5 Levels (μg/m³)', color=color)
ax1.plot(years, pm25_levels, color=color, marker='o', label='PM2.5 Levels')
# WHO threshold line
ax1.axhline(y=who_threshold, color='green', linestyle='--', label='WHO Threshold (5 μg/m³)')
ax1.tick_params(axis='y', labelcolor=color)
# Secondary Axis: Stubble burning incidents
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Stubble Burning Incidents', color=color)
ax2.bar(years, stubble_burning_incidents, color=color, alpha=0.2, width=0.3, label='Stubble Burning Incidents')
ax2.tick_params(axis='y', labelcolor=color)
# Title & Merging Legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.title(f"Delhi Pollution vs. Stubble Burning (2020-2025)\nData Correlation: {correlation:.2f}", fontsize=14)
plt.tight_layout()
plt.grid(True)
plt.show()