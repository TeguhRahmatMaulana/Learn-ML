#input data dari user 
#data yang dimasukkan pasti menjadi string

data = input("Masukkan data=")
print("data=", data, "type =", type(data))
 
 #jika ingin menjadikan data menjadi integer atau float
data_int = int(input("Masukkan data="))
print("data=", data_int, "type =", type(data_int))

#float sama tinggal ganti perintah "int" menjadi "float"

#boolean berbeda

boool = bool(int(input("Masukkan data=")))
print("data=", boool, "type =", type(boool))

#perintah ini digunakan untuk memasukkan data dari user ke server 