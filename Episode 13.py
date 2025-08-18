#Bitwise Operator

#Bitwise adalah operasi masing masing biner 
#bilangan biner adalah bilangan 00000000 (hanya bisa diisi angka 0 dan 1)
#nilai masing-masing bilangan biner adalah 2^a 
#biner pertama memilikin ^0, biner kedua memiliki ^1 dan seterusnya sampai biner ke delapan

#untuk melihat kode biner diperlukan perintah "08b"

#bitwise operator memiliki 6 perintah, or (|), and (&), xor (^), not (~), Shift right (>>), Shift left (<<)


a = 10
b = 5

#bitwise or (penjelasan sama dengan episode 11)
c = a | b 
print("\n===bitwise OR===")
print("nilai =", a, ", binary =", format(a, "08b", ))
print("nilai =", b, ", binary =", format(b, "08b", ))
print("------------------------------- (|)")
print("nilai =", c, ", binary =", format(c, "08b", ))

#bitwise and 
c = a & b 
print("\n===bitwise and===")
print("nilai =", a, ", binary =", format(a, "08b", ))
print("nilai =", b, ", binary =", format(b, "08b", ))
print("------------------------------- (&)")
print("nilai =", c, ", binary =", format(c, "08b", ))

#bitwise xor
c = a ^ b 
print("\n===bitwise xor===")
print("nilai =", a, ", binary =", format(a, "08b", ))
print("nilai =", b, ", binary =", format(b, "08b", ))
print("------------------------------- (^)")
print("nilai =", c, ", binary =", format(c, "08b", ))

#bitwise not merupakan operasi mirroring 
#dimulai dari -1 
#contoh jika bilangan 0 maka not nya akan menjadi -1
#dan jika bilangannya 1 maka not nya akan menjadi -2 dan seterusnya

print("\n=====bitwise not=====")
c = ~a 
print("nilai =", a, ", binary =", format(a, "08b", ))
print("------------------------------- (~)")
print("nilai =", c, ", binary =", format(c, "08b", ))

#bitwise shift right (menggeser bilangan biner kekanan)

print("\n=====bitwise Shift right=====")
d = b >> 3
print("nilai =", b, ", binary =", format(a, "08b", ))
print("------------------------------- (~)")
print("nilai =", d, ", binary =", format(d, "08b", ))

#bitwise shift left (menggeser bilangan biner kekiri)

print("\n=====bitwise Shift left=====")
d = b << 3
print("nilai =", b, ", binary =", format(a, "08b", ))
print("------------------------------- (~)")
print("nilai =", d, ", binary =", format(d, "08b", ))




