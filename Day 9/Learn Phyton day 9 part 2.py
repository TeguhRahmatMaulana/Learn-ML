#Operasi dan manipulasi string

#menyambung string
A = "aku"
B = "kamu"
C = "kita"

data = A + " " + B + " " + C
print(data)

#menghitung panjang dari suatu string (len)

panjang = len(data)

print("panjang dari " + data + "adalah" + " " + str(panjang))

# operator untuk string

# 1. mengecek komponen dalam string

d = "a"

status = d in data
print("huruf" + " " + d +" "+ "yang ada di" + "" + data +" " + "adalah" + " " + str(status))

status = d not in data
print("huruf" + " " + d +" "+ "yang ada di" + "" + data +" " + "adalah" + " " + str(status))

# 2. Indexing

# mengambil dari kiri ke kanan
print("index ke-0 adalah " + data[0])
print("index ke-6 adalah " + data[6])

# mengambil dari kanan ke kiri
print("index ke-(-1) adalah " + data[-1])
print("index ke-(-6) adalah " + data[-6])

#mengambil dua atau lebih index
#harus dilebihkan 1 agar index yang diambil bisa sesuai
print("index ke-0 sampai 3 adalah " + data[0:3])

#mengambil index dua atau lebih dengan jeda
print("index ke-0 sampai 6 adalah " + data[0:6:2])

# 3. Mengulang String

print(10*"wk")
print("wk"*10)

# 4. Mengambil nilai karakter string paling kecil
# mengacu pada ASCII CODE

print("nilai karakter paling kecil adalah" + min(data))
print("nilai karakter paling kecil " + max(data))

#ASCII CODE 

ascii_code = ord("B")
print("nilai ascii code untuk karakter 'B' adalah " + str(ascii_code))
Nilai_ascii = 121
print("char untuk nilai ascii 121 adalah " + chr(ascii_code))

#Operator dalam bentuk method

data = "aku kamu kami dan kita"

jumlah = data.count("a")

print("jumlah huruf a dalam data adalah " + str(jumlah))

