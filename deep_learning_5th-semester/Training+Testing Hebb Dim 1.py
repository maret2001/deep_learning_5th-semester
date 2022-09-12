
# Nama  : Maret Ismoyo
# NIM   : 1911502084

# Bagian training - Algoritma Hebb
# --------------------------------

# deklarasi variabel
x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
t  = [-1, 1, -1, -1]
b  = 1

# 1. Inisialisasi bobot, semua bobot diberi harga 0
w1, w2, wb = 0, 0, 0

# 2. Untuk setiap pasangan vektor-masukan dan target keluaran (diulang / loop sebanyak)
# jumlah pasangan data input dan target)

for i in range(4):

    # a. Hitung perubahan bobot (delta w)
    dw1 = x1[i] * t[i]
    dw2 = x2[i] * t[i]
    dwb = b * t[i]

    # b. Perbaharui nilai bobot (w)
    w1 = w1 + dw1
    w2 = w2 + dw2
    wb = wb + dwb

print('PELATIHAN / TRAINING')
print('--------------------\n\n')
print('Setelah algoritma Hebb selesai dieksekusi, maka didapat bobot sebagai berikut:')
print('w1 :',w1)
print('w2 :',w2)
print('wb :',wb)

# Bagian testing - Algoritma Hebb
# -------------------------------

print('\n\n\nPENGUJIAN / TESTING')
print('-------------------\n\n')

print('x1 x2  y')
print('=========')

for i in range(4):
    y_in = x1[i] * w1 + x2[i] * w2 + b * wb

    if y_in >= 0:
        y = 1

    if y_in < 0:
        y = -1

    # print section
    if x1[i] > 0:
        print(' %d'%x1[i], end=' ')
    else:
        print('%d'%x1[i], end=' ')
    if x2[i] > 0:
        print(' %d'%x2[i], end=' ')
    else:
        print('%d'%x2[i], end=' ')
    if y > 0:
        print(' %d'%y)
    else:
        print('%d'%y)

print('=========')
