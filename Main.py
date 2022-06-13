#Tipe Data : Int, Str, Boolean, Float
Nilai_y = 9
Harga = 9.9
Buah = False
Berapa = "7"

#Integer
print("=====INTEGER=====")
print("Nilai y adalah = ", Nilai_y, ",bertipe : ", type(Nilai_y))
data_float = float(Nilai_y)
data_str = str(Nilai_y)
data_boolean = bool(Nilai_y)
print("Nilai y adalah = ", data_float, ",bertipe : ", type(data_float))
print("Nilai y adalah = ", data_str, ",bertipe : ", type(data_str))
print("Nilai y adalah = ", data_boolean, ",bertipe : ", type(data_boolean)) #False Jika Nilai Int = 0

#Float
print("=====FLOAT=====")
print("Nilai Harga adalah = ", Harga, ",bertipe : ", type(Harga))
data_int = int(Harga)
data_str = str(Harga)
data_boolean = bool(Harga)
print("Nilai Harga adalah = ", data_int, ",bertipe : ", type(data_int))
print("Nilai Harga adalah = ", data_str, ",bertipe : ", type(data_str))
print("Nilai Harga adalah = ", data_boolean, ",bertipe : ", type(data_boolean)) #False Jika Nilai Int = 0

#Boolean
print("=====BOOLEAN=====")
print("Nilai Buah adalah = ", Buah, ",bertipe : ", type(Buah))
data_int = int(Buah)
data_float = float(Buah)
data_str = str(Buah)
print("Nilai Buah adalah = ", data_int, ",bertipe : ", type(data_int))
print("Nilai Buah adalah = ", data_float, ",bertipe : ", type(data_float))
print("Nilai Buah adalah = ", data_str, ",bertipe : ", type(data_str)) 

#String
print("=====STRING=====")
print("Nilai Berapa adalah = ", Berapa, ",bertipe : ", type(Berapa))
data_int = int(Berapa)
data_float = float(Berapa)
data_boolean = bool(Berapa)
print("Nilai Berapa adalah = ", data_int, ",bertipe : ", type(data_int))
print("Nilai Berapa adalah = ", data_float, ",bertipe : ", type(data_float))
print("Nilai Berapa adalah = ", data_boolean, ",bertipe : ", type(data_boolean)) #False Jika = Kosong

