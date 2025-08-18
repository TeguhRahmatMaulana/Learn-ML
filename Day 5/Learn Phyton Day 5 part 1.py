#Operasi Aritmatika



a = 24
b = 5

# Pertambahan mempunyai simbol "+"
 
hasil = a + b

print("a", "+", "b", "=", hasil)

# Pengurangan mempunyai simbol "-"
# Sama seperti matematika pada umumnya, 
# jika nilai utama lebih kecil dari nilai kedua hasilnnya akan menjadi negatif

hasil = a - b

print("a", "-", "b", "=", hasil)

#Pembagian mempunyai simbol "/"


hasil = a / b

print("a", "/", "b", "=", hasil)

# Perkalian mempunyai simbol "*"

hasil = a * b

print("a", "*", "b", "=", hasil)

# Eksponen atau perpangkatan mempunyai simbol "**"

hasil = a ** b

print("a", "**", "b", "=", hasil)

# Modulus atau sisa bagi (sisa nilai saat dibagi) memiliki simbol "%"
hasil = a % b

print("a", "%", "b", "=", hasil)

#  Floor division adalah pembulatan kebawah pada pembagian 
# Memiliki simbol "//"
# Walaupun desimal melebihi angka 5 akan dibulatkan kebawah

hasil = a // b

print("a", "//", "b", "=", hasil)

# Operational precedence atau operasi prioritas
# Suatu Operasi yang di dahulukan 
# Urutan Operasi
# "(x+y)" > Pangkat atau eksponen "**" > Perkalian "*" > Pembagian "/" > Modulus "%" > Floor Division "//" >
# Penjumlahan "+" > Pengurangan "-"

x = 7
y = 8
z = 9 

hasil = x * y ** z / z // x % y - x + z * (x + y - z)

print(x, '*', y, '**', z, '/', z, '//', x, '%', y, '-', x, '+', z, '(', x, "+", y, "-", z, '=', hasil)

#contoh penggunaan "()"
#Dengan "()"
hasil = (x / y) * z

print('(', x, '+', y, ')', '*', z, '=', hasil)
#Tanpa "()"

hasil = x / y * z

print( x, '+', y,  '*', z, '=', hasil)
