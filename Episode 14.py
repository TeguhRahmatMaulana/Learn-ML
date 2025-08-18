#Operator asignment adalah operator penyingkatan
#semisal a = a + 1 bisa disingkat menjadi a += 1
#Operator assignment bisa dipakai di operasi aritmatika dan operasi bitwise

#Operasi tambah, kurang, bagi, kali

a = 5

a += 1

print('hasil dari a += 1 =', a)

a -= 3
print('hasil dari a -= 3 =', a)

a *= 3
print('hasil dari a *= 3 =', a)

a /= 9
print('hasil dari a /= 3 =', a)

#Operasi Modulus dan floor division

b = 10
b %= 3
print('hasil dari b %= 3 =', b)
 
b = 10
b //= 3
print('hasil dari b //= 3 =', b)

#Operasi Eksponen atau perpangkatan
b = 10
b **= 3
print('hasil dari b **= 3 =', b)

#Operasi Bitwise

print("\n Operasi bitwise")
print("\n Operasi OR")
c = True
print("\n Nilai C =", c)
c |= False
print("nilai C |= False", "Nilai C menjadi =", c)
c = True
print("\n Nilai C =", c)
c |= True
print("nilai C |= True", "Nilai C menjadi =", c)
c = False
print("\n Nilai C =", c)
c |= False
print("nilai C |= False", "Nilai C menjadi =", c)
c = False
print("\n Nilai C =", c)
c |= True
print("nilai C |= True", "Nilai C menjadi =", c)

print("\n Operasi AND")
c = True
print("\n Nilai C =", c)
c &= False
print("nilai C &= False", "Nilai C menjadi =", c)
c = True
print("\n Nilai C =", c)
c &= True
print("nilai C &= True", "Nilai C menjadi =", c)
c = False
print("\n Nilai C =", c)
c &= False
print("nilai C &= False", "Nilai C menjadi =", c)
c = False
print("\n Nilai C =", c)
c &= False
print("nilai C &= False", "Nilai C menjadi =", c)

print("\n Operasi XOR")
c = True
print("\n Nilai C =", c)
c ^= False
print("nilai C ^= False", "Nilai C menjadi =", c)
c = True
print("\n Nilai C =", c)
c ^= True
print("nilai C ^= True", "Nilai C menjadi =", c)
c = False
print("\n Nilai C =", c)
c ^= False
print("nilai C ^= False", "Nilai C menjadi =", c)
c = False
print("\n Nilai C =", c)
c ^= False
print("nilai C ^= False", "Nilai C menjadi =", c)

#Operasi Shifting

d = 0b0110
print("nilai d", format(d,"04b"))
print("shift kanan (>>)")
d >>= 2
print("Nilai d >>= 2 , Nilai d menjadi = ", d, format(d, "04b") )

d = 0b0100
print("nilai d", format(d,"04b"))
print("shift kiri (<<)")
d <<= 1
print("Nilai d <<= 1 , Nilai d menjadi = ", d, format(d, "04b") )


