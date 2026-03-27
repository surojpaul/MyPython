import matplotlib.pyplot as plt
# Sample data for PM2.5 levels and stubble burning incidents
years = [2020, 2021, 2022, 2023, 2024, 2025]
pm25_levels = [95, 105, 98, 100, 105, 97]
stubble_burning_incidents = [80, 95, 75, 60, 55, 45]
who_threshold = 5
# Create a figure and axis
fig, ax1 = plt.subplots()
# Plot PM2.5 levels on the primary y-axis
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('PM2.5 Levels (μg/m³)', color=color)
# Plot the WHO threshold as a horizontal line
ax1.axhline(y=who_threshold, color='green', linestyle='--', label='WHO Threshold (5 μg/m³)')
ax1.plot(years, pm25_levels, color=color, marker='o', label='PM2.5 Levels')
ax1.fill_between(years, 0, who_threshold, color='green', alpha=0.1)
ax1.tick_params(axis='y', labelcolor=color)
# Create a second y-axis for stubble burning incidents
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Stubble Burning Incidents', color=color)
ax2.bar(years, stubble_burning_incidents, color=color, alpha=0.2, width=0.3, label='Stubble Burning Incidents')
ax2.tick_params(axis='y', labelcolor=color)
# Add legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
# Show the plot
plt.show()