
# Nama  : Maret Ismoyo
# NIM   : 1911502084

import math
import random

# Bagian training atau learning
# (menghitung / mencari bobot)
# -------------------

x1 = [1, 1, 0, 0]
x2 = [1, 0, 1, 0]
t  = [0, 1, 1, 0]
b  = 1

e = 2.7182
alpha = 0.4

v10 = (round(random.uniform(-1, 1), 3))
v11 = (round(random.uniform(-1, 1), 3))
v12 = (round(random.uniform(-1, 1), 3))
w10 = (round(random.uniform(-1, 1), 3))
w13 = (round(random.uniform(-1, 1), 3))

v20 = (round(random.uniform(-1, 1), 3))
v21 = (round(random.uniform(-1, 1), 3))
v22 = (round(random.uniform(-1, 1), 3))
w11 = (round(random.uniform(-1, 1), 3))

v30 = (round(random.uniform(-1, 1), 3))
v31 = (round(random.uniform(-1, 1), 3))
v32 = (round(random.uniform(-1, 1), 3))
w12 = (round(random.uniform(-1, 1), 3))

print('PELATIHAN / TRAINING')
print('--------------------\n\n')

print('Bobot awal (dirandom):')
print('v10: ', v10,'\tv20: ',v20,'\tv30: ',v30)
print('v11: ', v11,'\tv21: ',v21,'\tv31: ',v31)
print('v12: ', v12,'\tv22: ',v22,'\tv32: ',v32)
print('w10: ', w10,'\tw11: ',w11,'\tw12: ',w12,'\tw13: ',w13)

maxiter = 1000

# Perulangan Luar
# Kondisi berhenti epoch (maxiterasi)


count = 0;

while count < maxiter:
    count += 1
    
    # Perulangan dalam data
    for i in range(4):

        # Langkah 4: Hitung keluaran unit tersembunyi (zj)
        z_net1 = b * v10 + x1[i] * v11 + x2[i] * v12
        z_net2 = b * v20 + x1[i] * v21 + x2[i] * v22
        z_net3 = b * v30 + x1[i] * v31 + x2[i] * v32

        #print('\niterasi ', count)
        #print('z_net1 ',z_net1)
        #print('z_net2 ',z_net2)
        #print('z_net3 ',z_net3)

        z1 = 1 / (1 + pow(e, -z_net1))
        z2 = 1 / (1 + pow(e, -z_net2))
        z3 = 1 / (1 + pow(e, -z_net3))

        #print('z1 ',z1)
        #print('z2 ',z2)
        #print('z3 ',z3)

        # Langkah 5: Hitung keluaran unit (yk)
        y_net = b * w10 + z1 * w11 + z2 * w12 + z3 * w13

        #print('y_net ',y_net)

        y = 1 / (1 + pow(e, -y_net))

        #print('y ',y)

        # Langkah 6: Hitung delta (perubahan bobot) antara hidden layer dengan output layer
        teta = (t[i] - y) * y * (1 - y)

        #print('teta ',teta)

        dw10 = alpha * teta * b
        dw11 = alpha * teta * z1
        dw12 = alpha * teta * z2
        dw13 = alpha * teta * z3

        #print('dw10 ',dw10)
        #print('dw11 ',dw11)
        #print('dw12 ',dw12)
        #print('dw13 ',dw13)

        # Langkah 7: Hitung delta (perubahan bobot) antara input layer dengan hidden layer
        t_net1 = teta * w11
        t_net2 = teta * w12
        t_net3 = teta * w13

        #print('t_net1 ',t_net1)
        #print('t_net2 ',t_net2)
        #print('t_net3 ',t_net3)

        ta1 = t_net1 * z1 * (1 - z1)
        ta2 = t_net2 * z2 * (1 - z2)
        ta3 = t_net3 * z3 * (1 - z3)

        #print('ta1 ',ta1)
        #print('ta2 ',ta2)
        #print('ta3 ',ta3)

        dv10 = alpha * ta1 * b
        dv20 = alpha * ta2 * b
        dv30 = alpha * ta3 * b
        dv11 = alpha * ta1 * x1[i]
        dv21 = alpha * ta2 * x1[i]
        dv31 = alpha * ta3 * x1[i]
        dv12 = alpha * ta1 * x2[i]
        dv22 = alpha * ta2 * x2[i]
        dv32 = alpha * ta3 * x2[i]

        #print('dv10 ',dv10)
        #print('dv20 ',dv20)
        #print('dv30 ',dv30)
        #print('dv11 ',dv11)
        #print('dv21 ',dv21)
        #print('dv31 ',dv31)
        #print('dv12 ',dv12)
        #print('dv22 ',dv22)
        #print('dv32 ',dv32)

        #Langkah 8: Hitung semua perubahan bobot
        w10 = w10 + dw10
        w11 = w11 + dw11
        w12 = w12 + dw12
        w13 = w13 + dw13

        #print('w10 ',w10)
        #print('w11 ',w11)
        #print('w12 ',w12)
        #print('w13 ',w13)

        v10 = v10 + dv10
        v20 = v20 + dv20
        v30 = v30 + dv30
        v11 = v11 + dv11
        v21 = v21 + dv21
        v31 = v31 + dv31
        v12 = v12 + dv12
        v22 = v22 + dv22
        v32 = v32 + dv32

        #print('v10' ,v10)
        #print('v20' ,v20)
        #print('v30' ,v30)
        #print('v11' ,v11)
        #print('v21' ,v21)
        #print('v31' ,v31)
        #print('v12' ,v12)
        #print('v22' ,v22)
        #print('v32' ,v32)

print('\n\nBobot setelah proses algoritma Backpropagation iterasi ke-',count)
print('v10: ',round(v10, 3),'\tv20: ',round(v20, 3),'\tv30: ',round(v30, 3))
print('v11: ',round(v11, 3),'\tv21: ',round(v21, 3),'\tv31: ',round(v31, 3))
print('v12: ',round(v12, 3),'\tv22: ',round(v22, 3),'\tv32: ',round(v32, 3))
print('w10: ',round(w10, 3),'\tw11: ',round(w11, 3),'\tw12: ',round(w12, 3),'\tw13: ',round(w13, 3))

# Bagian testing
# (menguji apakah bobot yang didapatkan melalui proses training apakah sudah sesuai
# diharapkan akurasi mendekati 100%)

print('\n\n\nPENGUJIAN / TESTING')
print('-------------------\n\n')

print(' x1 x2  y')
print('---------')

for i in range(4):

    # hitung proses di neuron z1
    z_net1 = b * v10 + x1[i] * v11 + x2[i] * v12
    z1 = 1 / (1 + pow(e, -z_net1))

    # hitung proses di neuron z2
    z_net2 = b * v20 + x1[i] * v21 + x2[i] * v22
    z2 = 1 / (1 + pow(e, -z_net2))

    # hitung proses di neuron z3
    z_net3 = b * v30 + x1[i] * v31 + x2[i] * v32
    z3 = 1 / (1 + pow(e, -z_net3))

    # hitung proses di neuron y
    y_net = b * w10 + z1 * w11 + z2 * w12 + z3 * w13
    y = 1 / (1 + pow(e, -y_net))

    #print(x1[i], x2[i], y)
    print('%d'%x1[i], '%d'%x2[i], '%d'%round(y))

print('---------')
