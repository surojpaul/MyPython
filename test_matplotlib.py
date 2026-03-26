import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
temperature = [30, 32, 28, 31, 29]
plt.plot(days, temperature)
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.title('Temperature over Days')
plt.show()