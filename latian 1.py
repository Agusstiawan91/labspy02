# Meminta input dari pengguna
bilangan1 = input("Masukkan bilangan pertama: ")
bilangan2 = input("Masukkan bilangan kedua: ")
bilangan3 = input("Masukkan bilangan ketiga: ")

# Menentukan bilangan terbesar
if bilangan1 >= bilangan2 and bilangan1 >= bilangan3:
    terbesar = bilangan1
elif bilangan2 >= bilangan1 and bilangan2 >= bilangan3:
    terbesar = bilangan2
else:
    terbesar = bilangan3

# Menampilkan bilangan terbesar
print("Bilangan terbesar adalah:",terbesar)
