import matplotlib.pyplot as plt
import numpy as np

#x = ['Linear Regression', 'Decision Tree Regressor','Random Forest Regressor','Bagging Regressor', 'Gradient Boosting Tree', 'Multi-Layer Perceptron']
x = ['LR', 'DTR','RFR','BGR', 'GBR', 'MLP']
y_rsme = [[1.4937, 1.6224, 1.5138, 1.5187, 1.4577 , 1.4652], [1.9422, 2.010, 1.9156, 1.9219, 1.8682,  1.9042], [2.1266, 2.1615, 2.0665, 2.0675, 2.0195, 2.0734]]
y_mae = [[1.1007, 1.2209, 1.1270, 1.130, 1.0589, 1.0692], [1.4851, 1.5469, 1.4648, 1.4701, 1.4024, 1.4410], [1.6524, 1.6739, 1.5845, 1.5860, 1.5365, 1.5925]]
y_mape = [[0.0421, 0.0482, 0.0440, 0.0441, 0.0405, 0.0418], [0.0580, 0.0615,  0.0583, 0.0584, 0.0548, 0.0572], [0.0652, 0.0669, 0.0639, 0.0640, 0.0610, 0.0640]]
y_r2 = [[0.8676, 0.8701, 0.8688, 0.8673, 0.8779, 0.8916], [0.7609, 0.8041, 0.7778, 0.7771,  0.7897, 0.8201], [0.6995, 0.7745, 0.7407, 0.7407, 0.7519, 0.7872]]
fig = plt.figure(figsize=(8, 7.5))

plt.subplot(2, 2, 1)
plt.plot(x, y_rsme[0], marker='o', color='skyblue')
plt.plot(x, y_rsme[1], marker='o', color='lightcoral')
plt.plot(x, y_rsme[2], marker='o', color='yellowgreen')
plt.title("RSME")

plt.subplot(2, 2, 2)
plt.plot(x, y_mae[0], marker='o', color='skyblue')
plt.plot(x, y_mae[1], marker='o', color='lightcoral')
plt.plot(x, y_mae[2], marker='o', color='yellowgreen')
plt.title("MAE")

plt.subplot(2, 2, 3)
plt.plot(x, y_mape[0], marker='o', color='skyblue')
plt.plot(x, y_mape[1], marker='o', color='lightcoral')
plt.plot(x, y_mape[2], marker='o', color='yellowgreen')
plt.title("MAPE")

plt.subplot(2, 2, 4)
plt.plot(x, y_r2[0], marker='o', color='skyblue')
plt.plot(x, y_r2[1], marker='o', color='lightcoral')
plt.plot(x, y_r2[2], marker='o', color='yellowgreen')
plt.title("R2")

fig.legend(['1-Day Ahead', '2-Day Ahead', '3-Day Ahead'], 
           loc='upper center', ncol=3, bbox_to_anchor=(0.5, 0.99))

fig.tight_layout(rect=[0, 0.95, 0, 0])
plt.show()
