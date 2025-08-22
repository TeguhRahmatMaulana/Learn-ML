# Pengenalan data String 
data = "ini adalah string"
print(data)
print(type(data))

#cara membuat string
#bisa menggunakan single quotes ('A')
#dan juga menggunakan double quotes ("A")

data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

#memiliki 2 tipe quote karena kedua simbol tersebut akan dipakai 
#di situasi tertentu

data="'halo apa kabar ?'"
print(data)
data='"halo apa kabar ?"'
print(data)
data="sekarang hari Jum'at"
print(data)

#simbol (\) bisa digunakan dalam beberapa hal
#merubah single quote didalam string agar tidak di kira pembuka dan penutup string

print('sekarang hari Jum\'at')

#mengubah simbol (\) menjadi string

print("C:\\data\\print")

#memberikan tab (\t)

print("data\tcamp")

#memberikan perintah enter (\n) (\r) (\r\n)

print("data\nenter") #LF 
print("data\renter") #CR
print("data\r\nenter") #CRLF

#Mac linux pasti LF 
#windows pasti CRLF 
#cek informasi pojok kanan bawah

#String literal atau raw

#(**r**"A/")

#digunakan untuk merubah simbol yang digunakan 
#dalam perintah string menjadi string tanpa menambah slash (\)
print(r'C:\Data\Camp')

#multiline literal string

print("""
      Adam
      Warlock
      Jamet
      """)

#multiline literal string memakai raw

print(r"""
      https:\\adam.com
      C:\user\adam
      """)

