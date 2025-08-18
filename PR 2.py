#Mencari

#------0+++++++5---------8+++++++11---------
#++++0-----------5++++++8-----------11+++++


print("irisan")
inputUser1 = float(input("Masukkan data lebih dari 0 atau kurang dari 5 dan lebih dari 8 atau kurang dari 11 "))

inputLebih1 = inputUser1 > 0
inputLebih2 = inputUser1 > 8

inputKurang1 = inputUser1 < 5
inputKurang2 = inputUser1 < 11 

isCorrect = inputLebih1 and inputKurang1 or inputLebih2 and inputKurang2

print("angka yang anda masukkan =", isCorrect)

print("Gabungan")


inputUser1 = float(input("Masukkan data kurang dari 0 atau lebih dari 5 dan kurang dari 8 atau lebih dari 11 "))

inputKurang1 = inputUser1 < 0
inputKurang2 = inputUser1 < 8

inputLebih1 = inputUser1 > 5
inputLebih2 = inputUser1 > 11 

isCorrect = inputKurang1 or inputLebih1 and inputKurang2 or inputLebih2

print("angka yang anda masukkan =", isCorrect)
