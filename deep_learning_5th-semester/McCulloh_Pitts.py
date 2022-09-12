
# Nama  : Maret Ismoyo
# NIM   : 1911502084

#Program McCullohPitts
 
#1. input layer (x1,x2)
x1=0; x2=0;
 
#2. Bobot
w1=2; w2=2;
 
#3. proses di neutron y
# a. hitung y_in
y_in=x1*w1+x2*w2;
 
#b. fungsi aktivasi (hitung y)
if (y_in>=2): 
  y=1
if (y_in<2) :
  y=0
 
#4. cetak
print("\nx1: ",x1)
print("\nx2: ",x2)
print("\ny: ",y)