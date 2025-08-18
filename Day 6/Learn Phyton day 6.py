# Operasi komparasi

# Operasi perbandingan, hasilnya akan selalu boolean "True/False"
# ada beberapa simbol 
# lebih dari ">", kurang dari "<", sama dengan "==", tidak sama dengan "=!", lebih dari sama dengan ">=", 
# kurang dari sama dengan "<=", is dan is not

# perbedaan ">" dan ">=" dan juga sebaliknya terletak pada angka pertama yang dibandingkan
# jika ">" dan "<" angka pertama akan dihilangkan, jadi bisa dimulai dengan angka pertama tetapi memiliki desimal 
# jika ">=" dan "<=" angka pertama akan diikutkan 

a = 12
b = 14

print("Operasi lebih dari dan kurang dari")

hasil = a > 3
print('hasil', '=', a, '>', 3, "adalah =", hasil)
hasil = a < 3
print('hasil', '=', a, '<', 3, "adalah =", hasil)
hasil = a > 4
print('hasil', '=', a, '>', 4, "adalah =", hasil)
hasil = a < 4
print('hasil', '=', a, '<', 4, "adalah =", hasil)
hasil = a > b
print('hasil', '=', a, '>', b, "adalah =", hasil)
hasil = a < b
print('hasil', '=', a, '<', b, "adalah =", hasil)

c = 15
d = 16
e = 15

print("Operasi lebih dan kurang dari sama dengan")
hasil = c >= 15
print('hasil', '=', c, '>=', 15, "adalah =", hasil)
hasil = c <= 15
print('hasil', '=', c, '<=', 15, "adalah =", hasil)
hasil = c >= 16
print('hasil', '=', c, '>=', 4, "adalah =", hasil)
hasil = c <= 16
print('hasil', '=', c, '<=', 4, "adalah =", hasil)
hasil = c >= e
print('hasil', '=', c, '>=', e, "adalah =", hasil)
hasil = c <= e
print('hasil', '=', c, '<=', e, "adalah =", hasil)
hasil = c >= d
print('hasil', '=', c, '>=', d, "adalah =", hasil)
hasil = c <= d
print('hasil', '=', c, '<=', d, "adalah =", hasil)


# Operasi Is dan is not 
# Operasi is dan is not tidak bisa dipakai di bilangan literal (tidak memiliki variable seperti, (a = 10) )
# biasanya dipakai di pemrograman oop
# (a = 10) ini akan disimpan ke memori jadi, is dan is not ini akan memanggil variable yang disimpan di memori tadi
# sebelumnya is dan is not bisa dipakai ke literal tapi sekarang tidak bisa
# pada phyton jika nilai variable sama, maka variable tersebut akan disimpan di memori yang sama 
# biasanya disimpan dalam bentuk heksadesimal (hex)



x = 5 
y = 5
z = 10

print("Operasi komparasi is dan is not")

#pemanggilan variable dalam bentuk heksadesimal "hex(id(variable))"

print("nilai dari x =", x, 'id =', hex(id(x)))
print("nilai dari y =", y, 'id =', hex(id(y)))
print("nilai dari z =", z, 'id =', hex(id(z)))

hasil = x is y
print("hasil x is y =", hasil)
hasil = x is z
print("hasil x is y =", hasil)
hasil = x is not y
print("hasil x is not y =", hasil)
hasil = x is not z
print("hasil x is not z =", hasil)
