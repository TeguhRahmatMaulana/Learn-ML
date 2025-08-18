# logic or boolean operation

# memiliki 4 perintah 
# or, not, and dan xor 

# not adalah perintah penegasan jika suatu variable tidak sema dengan variable lain 

print("-----NOT-----")

a = False
c = not a 
print("= not =")
print("data c =", c)

# OR (jika salah satu variable true, maka hasilnya true) 
# (jika semua variable false, maka hasilnya false)

print("-----OR-----")
a = False
b = True
c = a or b

print(a, "or", b, "=", c)
a = True
b = False
c = a or b

print(a, "or", b, "=", c)
a = False
b = False
c = a or b

print(a, "or", b, "=", c)
a = True
b = True
c = a or b


print(a, "or", b, "=", c)

# And (hanya yang memiliki variable true yang memiliki nilai true)

print("-----AND----")
a = False
b = True
c = a and b

print(a, "and", b, "=", c)
a = True
b = False
c = a and b

print(a, "and", b, "=", c)
a = False
b = False
c = a and b

print(a, "and", b, "=", c)
a = True
b = True
c = a and b

print(a, "and", b, "=", c)

# XOR harus memakai simbol "^"
# dia bisa true jika hanya salah satu saja yang true

print("-----XOR----")
a = False
b = True
c = a ^ b

print(a, "xor", b, "=", c)
a = True
b = False
c = a ^ b

print(a, "xor", b, "=", c)
a = False
b = False
c = a ^ b

print(a, "xor", b, "=", c)
a = True
b = True
c = a ^ b

print(a, "xor", b, "=", c)

