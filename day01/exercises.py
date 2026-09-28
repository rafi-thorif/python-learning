# ==========================================
# 1. Operasi Aritmatika Dasar (Operands: 3 dan 4)
# ==========================================
print(3 + 4)             # Penjumlahan -> Output: 7
print(3 - 4)             # Pengurangan -> Output: -1
print(3 * 4)             # Perkalian -> Output: 12
print(3 % 4)             # Modulus (Sisa Bagi) -> Output: 3
print(3 / 4)             # Pembagian (Desimal) -> Output: 0.75
print(3 ** 4)            # Pemangkatan (3 pangkat 4) -> Output: 81
print(3 // 4)            # Floor Division (Pembagian Bulat Ke Bawah) -> Output: 0

# ==========================================
# 2. Mencetak String / Teks
# ==========================================
print("John")                           # Nama depan
print("Doe")                            # Nama belakang
print("Indonesia")                      # Negara
print("I am enjoying 30 days of python") # Kalimat latihan

# ==========================================
# 3. Memeriksa Tipe Data Menggunakan type()
# ==========================================
print(type(10))                                 # Output: <class 'int'>
print(type(9.8))                                # Output: <class 'float'>
print(type(3.14))                               # Output: <class 'float'>
print(type(4 - 4j))                             # Output: <class 'complex'>
print(type(['Asabeneh', 'Python', 'Finland']))  # Output: <class 'list'>
print(type("John"))                             # Output: <class 'str'>
print(type("Doe"))                              # Output: <class 'str'>
print(type("Indonesia"))                        # Output: <class 'str'>

# ========================================================================
# ========================================================================

# 1. Number Types
my_int = 42                  # Integer (bilangan bulat)
my_float = 3.14159           # Float (bilangan desimal)
my_complex = 2 + 3j          # Complex (bilangan kompleks)

# 2. String (Teks di dalam kutip tunggal/ganda)
my_string = "Hello, Python!"

# 3. Boolean (Nilai kebenaran: True atau False)
is_learning = True
is_finished = False

# 4. List (Koleksi terurut, nilai bisa diubah / mutable, menggunakan [])
my_list = [10, "Python", 3.14, True]

# 5. Tuple (Koleksi terurut, nilai tidak bisa diubah / immutable, menggunakan ())
my_tuple = ("Linux", "Windows", "macOS")

# 6. Set (Koleksi tidak terurut & tanpa nilai duplikat, menggunakan {})
my_set = {1, 2, 3, 3, 4}     # Hanya menyimpan {1, 2, 3, 4}

# 7. Dictionary (Pasangan Key-Value, menggunakan {})
my_dict = {
    "name": "Alex",
    "role": "Developer",
    "age": 20
}

# Verifikasi tipe data di terminal
print(type(my_int))
print(type(my_string))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dict))