# (a = 10) a adalah variable dari nilai 10
# tipe data adalah macam-macam nilai 
# phyton memiliki 5 tipe data (int, string, float, Boolean, dan kompleks)
# untuk menutup kekurangan,  Bahasa pemrograman C bisa dimasukkan ke Phyton (karena Phyton dasarnya dari bahasa C)
# command type(variable), menunjukkan tipe data dari suatu value (variable) sesuai dengan nama variable yang dibuat)

# tipe data int atau integer adalah tipe data angka
data_int = 10
print("data int=", data_int, "-data bertipe", type(data_int)) 

# tipe data str atau string adalah tipe data yang harus memiliki simbol 2 kutip, kebanyakan menyatakan suatu kata
# jika angka di tambah dua kutip maka akan menjadi string
data_str = "Nama"
print("data str=", data_str, "-data bertipe", type(data_str)) 

# tipe data float adalah decimal
data_float = 1.5
print("data float=", data_float, "-data bertipe", type(data_float)) 

# tipe data bool adalah data biner (010101) atau true/false
data_bool = True
print("data bool=", data_bool, "-data bertipe", type(data_bool)) 

# tipe data kompleks dikhususkan untuk operasi matematika
data_complex = complex(5+6)
print("data complex=", data_complex, "-data bertipe", type(data_complex)) 

# cara memanggil tipe data dari bahasa pemrograman C
# setelah perintah import adalah tipe data yang diambil dari bahasa C
from ctypes import c_double, c_char

# cara menggunakan bahasa C di Phyton

data_c_double = c_double(10.5)
print("data double=", data_c_double, "-data bertipe", type(data_c_double)) 

# judul sebuah class bisa bebas untuk penamaannya tetapi harus mengikuti episode 4

