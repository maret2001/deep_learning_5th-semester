
# Nama  : Maret Ismoyo
# NIM   : 1911502084

data_act = [
            2590,2260,870,1170,548,307,314,0,304,243,182,245,
			2176,2053,1080,810,326,210,523,235,124,1026,546,1524,
			2375,2140,1140,1110,360,846,364,236,0,0,504,639
            ]
data_norm = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
            ]

n_max = data_act[0]
n_min = data_act[0]

for i in range(36):
    if (data_act[i]>n_max):
        n_max=data_act[i]
    
    else:
        if (data_act[i]<n_min):
            n_min=data_act[i]

for i in range(36):
	data_norm[i]=(0.8*(data_act[i]-n_min)/(n_max-n_min))+0.1

for i in range (36):
    print(round(data_norm[i], 4), end=' ')