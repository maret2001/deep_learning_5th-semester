
# Nama  : Maret Ismoyo
# NIM   : 1911502084

#bagian training - Algoritma Hebb

#Deklarasi variabel
data = [
        [1,1,1,1],
        [1,-1,1,-1],
        [-1,1,1,-1],
        [-1,-1,1,-1]
       ]

w = [1,2,3]
dw = [1,2,3]

for i in range(3):
    w[i]=0

for b in range(4):
    for k in range(3):
        dw[k]=data[b][k]*data[b][3]
        w[k]=w[k]+dw[k]

print('PELATIHAN/TRAINING')
print('------------------')
print('Setelah algoritma Hebb selesai dieksekusi, maka didapat bobot sebagai berikut:')

for i in range(3):
    print('w',i+1,':',w[i])
    
print('\n\nPENGUJIAN/TESTING')
print('-----------------\n\n')

print('x1 x2 y')
print('**********')

for b in range(4):
    y_in = 0
    
    for k in range(3):
        y_in=y_in+data[b][k]*w[k]
    
    for k in range(2):
        if data[b][k] > 0:
            print(' %d'%data[b][k], end=' ')
        else:
            print('%d'%data[b][k], end=' ')
    
    if y_in>=0:
        y=1
    if y_in<0:
        y=-1
    
    if y > 0:
        print(' %d'%y)
    else:
        print('%d'%y)
        
print('---------')