import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import random


y = [3.3, 3.2, 3.5, 3.9, 4.0, 4.3, 4.1, 4.2, 4.4, 4.0]
x = [i for i in range(len(y))]

print(y)

plt.scatter(x, y)
plt.plot(y, color="g")
plt.xticks(x)
plt.title('Цены на 2-х комнатные квартиры в СПБ 11.19')
plt.ylabel('Цены в млн. руб.')

plt.show()
