# Logika dan komparasi

# membuat gabungan area rentang dari angka 
# \n adalah enter dalam program 
# alt + click (memilih bagian dari beberapa kata yang ingin diedit)

#gabungan dari 
# +++3-------10+++++

inputUser = float(input("masukkan angka dibawah 3 atau diatas 10 :"))

# +++3
inputKurang = (inputUser < 3)

print("angka dibawah dari 3 =", inputKurang)

# 10+++++
inputLebih = (inputUser > 10)
print("angka diatas dari 10 =", inputLebih)

#gabungan 
isCorrect = inputKurang or inputLebih
print("angka yang anda masukkan =", isCorrect)

inputUser = float(input("masukkan angka diatas 3 atau dibawah 10 :"))

#irisan dari
#-----3+++++10-----

#----3+++++
inputLebih = (inputUser > 3)

print("angka diatas dari 3 =", inputLebih)

# ++++10-----
inputKurang = (inputUser < 10)
print("angka dibawah dari 10 =", inputKurang)

# Irisan 
isCorrect = inputLebih and inputKurang
print("angka yang anda masukkan =", isCorrect)
