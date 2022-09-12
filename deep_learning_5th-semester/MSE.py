
# Nama  : Maret Ismoyo
# NIM   : 1911502084

import math

data_target = [0.1614, 0.1394, 0.1171, 0.1070, 0.1342]
data_predict = [0.2450, 0.1178, 0.1171, 0.3001, 0.0901]

t_error = 0

for i in range(5):
    error = data_target[i] - data_predict[i]
    t_error = t_error + pow(error, 2)

mse = t_error / 5

print('MSE : ', round(mse, 4))
