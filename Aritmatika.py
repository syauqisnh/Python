A = 20
B = 3

hasil = A + B
print(A, '+', B, '=',hasil)

C = 8
D = 2

hasil = C - D
print(C, '-', D, '=',hasil)

E = 10
F = 2

hasil = E * F
print(E, '*', F, '=',hasil)

G = 9
H = 3

hasil = G / H
print(G, '/', H, '=',hasil)

I = 20
J = 4

#Pangkat(Bahasa Lain Jarang ada)
hasil = I ** J
print(I, '**', J, '=',hasil)

K = 30
L = 4

#Modulus (Sisah Pembagian)
hasil = K % L
print(K, '%', L, '=',hasil)

#Floor Division (dibulatkan kebawah)
hasil = G // H
print(G, '//', H, '=',hasil)

#Prioritas Oprasi = 1.Dikerjakan Deluan (), 2.Exponen **, 3.Perkalian(Pembagian, dll), 4.Pertambahan(Pengurangan)
x = 7
y = 4
z = 6

hasil = x ** y * z + x / y-y % z // x 
print(x,'**',y,'*',z,'+',x, '/',y,'-',y,'%',z,'//',x, '=',hasil)

hasil = x - y * z
print(x,'-',y,'*',z, '=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,') *',z, '=',hasil)