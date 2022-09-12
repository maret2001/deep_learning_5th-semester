
# Nama  : Maret Ismoyo
# NIM   : 1911502084

# Bagian training - Algoritma Hebb
# --------------------------------

# deklarasi variabel
x = [
    [ 1, 1],
    [ 1,-1],
    [-1, 1],
    [-1,-1]
    ]

t = [1,-1,-1,-1]
bias = 1
w = [1, 2]
dw = [1, 2]

# 1. Inisialisasi bobot, semua bobot diberi harga 0
for i in range(2):
    w[i] = 0

wb = 0

# 2. Untuk setiap pasangan vektor-masukan dan target keluaran (diulang/loop sebanyak)
# jumlah pasangan data input dan target
for b in range(4):
    for k in range(2):

        # a. Hitung perubahan bobot (delta w)
        dw[k] = x[b][k] * t[b]

        # b. Perbaharui nilai bobot (w)
        w[k] = w[k] + dw[k]

    # Hitung perubahan dan perbaharui bobot untuk bias
    dwb = bias * t[b]
    wb = wb + dwb

print('PELATIHAN / TRAINING')
print('--------------------')
print('Setelah algoritma Hebb selesai dieksekusi, maka didapat bobot sebagai berikut:')

for i in range(2):
    print('w',i+1,':', w[i])
print('wb  :',wb)

# Bagian testing - Algoritma Hebb
# -------------------------------

print('\n\nPENGUJIAN / TESTING')
print('-------------------\n\n')

print(' x1 x2  y')
print('---------')

for b in range(4):
    y_in = bias * wb

    for k in range(2):
        y_in = y_in + x[b][k] * w[k]

        # print section
        if x[b][k] > 0:
            print(' %d'%x[b][k], end=' ')
        else:
            print('%d'%x[b][k], end=' ')
        
    if y_in >= 0:
        y = 1
    if y_in < 0:
        y = -1

    # print section
    if y > 0:
        print(' %d'%y)
    else:
        print('%d'%y)
        
print('---------')
