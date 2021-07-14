from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-2,8) # x에 -2~8 까지 저장
y = -x**2 + 5*x + 1

plt.plot(x,y,marker='o',linestyle = '--', color='r') # 그래프가 그려짐.

plt.grid() # 눈금선이 그려짐
plt.show()
