import numpy as np
import matplotlib.pyplot as plt

file = open('istherecorrelation.csv','r')
readings = file.readlines()
readings.pop(0)
W0 = []
liters = []
years = []
for reading in readings:
    y, W, hl = reading.strip('\r\n').split(';')
    W0.append(W)
    liters.append(hl)
    years.append(y)

for i in range(0, len(W0)):
    goede = float(W0[i].replace(',','.'))
    goedehecto = int(liters[i])
    liters[i] = goedehecto / 100
    W0[i] = goede

plt.plot(W0, years, label = "W0 [x1000]")
plt.plot(liters, years, label = "Liters [x1000]")
plt.legend()
plt.show()
