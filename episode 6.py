#Casting 
#Merubah tipe data 

## Integer

print("=Data Integer=")
data_integer = 9;
print("data =", data_integer, "Type =", type(data_integer) )

data_float = float(data_integer)
data_str = str(data_integer)
data_bool = bool(data_integer)

print("data =", data_float, "Type =", type(data_float) ) 
print("data =", data_str, "Type =", type(data_str) )
print("data =", data_bool, "Type =", type(data_bool) ) #value 0 pasti False, diatas 0 pasti true

## Float

print("=Data Float=")
data_float = 9.5;
print("data =", data_float, "Type =", type(data_float) )

data_integer = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data =", data_integer, "Type =", type(data_integer) ) #dibulatkan kebawah walau desimal 0.5 keatas
print("data =", data_str, "Type =", type(data_str) )
print("data =", data_bool, "Type =", type(data_bool) ) #value 0 pasti False, diatas 0 pasti true

#Boolean
print("=Data Boolean=")
data_bool = True;
print("data =", data_bool, "Type =", type(data_bool) )

data_integer = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)

print("data =", data_bool, "Type =", type(data_integer) ) 
print("data =", data_str, "Type =", type(data_str) ) #sama sesuai dengan data bool
print("data =", data_float, "Type =", type(data_float) ) #value 0 pasti False, diatas 0 pasti true

#String
print("=Data Boolean=")
data_str = "aduh";
print("data =", data_str, "Type =", type(data_str) )

data_integer = int(data_str)
data_str = str(data_str)
data_float = float(data_str)

print("data =", data_integer, "Type =", type(data_integer) ) #data integer harus angka, jika data string huruf akan terjadi eror
print("data =", data_bool, "Type =", type(data_bool) ) # diisi true dan jika tidak diisi false
print("data =", data_float, "Type =", type(data_float) ) #sama dengan data integer

# perintah float dan integer akan terjadi eror jika string merupakan suatu kata (harus angka) 
