
# Nama  : Maret Ismoyo
# NIM   : 1911502084

data_norm = [
            0.1614,0.1394,0.1171,0.1070,0.1342,0.1738,0.4204,0.6896,0.6363,0.3657,0.2266,0.1678,
            0.1439,0.1249,0.1013,0.1000,0.1179,0.3678,0.4838,0.9000,0.7017,0.5189,0.2394,0.1837
            ]

data_act = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
            ]

n_max = 13780
n_min = 1070

for i in range(24):
    data_act[i] = (((data_norm[i] - 0.1) * (n_max - n_min)) / 0.8) + n_min

for i in range(24):
    #print(int(data_act[i]), end=' ')
    print(round(data_act[i]), end=' ')
    if i == 11:
        print('\n')