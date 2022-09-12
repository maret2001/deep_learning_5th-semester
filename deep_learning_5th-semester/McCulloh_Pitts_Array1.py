
# Nama  : Maret Ismoyo
# NIM   : 1911502084

x1 = [1, 1, 0, 0]
x2 = [1, 0, 1, 0]

w1 = 2
w2 = 2

print('x1 x2  y')
print('--------')

for i in range(4):
    y_in = x1[i] * w1 + x2[i] * w2

    if y_in >= 2:
        y = 1

    if y_in < 2:
        y = 0

    print(' %d  %d  %d'% (x1[i], x2[i], y))

print('--------')
