
# Nama  : Maret Ismoyo
# NIM   : 1911502084

data_act = [
            2045, 1696, 1341, 1181, 1613, 2242, 6161, 10437, 9590, 5291, 3081, 2147,
            1767, 1466, 1090, 1070, 1355, 5324, 7167, 13780, 10629, 7725, 3284, 2400
            ]

data_norm = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
            ]

n_max = data_act[0]
n_min = data_act[0]

for i in range(24):

    if data_act[i] > n_max:
        n_max = data_act[i]

    else:
        if data_act[i] < n_min:
            n_min = data_act[i]

for i in range(24):
    data_norm[i] = (0.8 * (data_act[i] - n_min) / (n_max - n_min)) + 0.1

for i in range(24):
    print(round(data_norm[i], 4), end=' ')
