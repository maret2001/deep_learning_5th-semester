
# Nama  : Maret Ismoyo
# NIM   : 1911502084

x = [[1, 1], [1, 0], [0, 1], [0, 0]]
w = [2, 2]

print('x1 x2  y')
print('========')

for i in range(4):
    y_in = 0

    for j in range(2):
        y_in = y_in + x[i][j] * w[j]

        if y_in >= 2:
            y = 1

        if y_in < 2:
            y = 0

        print(x[i][j], end='  ')

    print(y)

print('========')
