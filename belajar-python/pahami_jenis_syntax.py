# CONTOH BOOLEAN + DICTIONARY + FUNCTION SEDERHANA

# DICTIONARY
dog_sizes = {
    "pitbull": 5,
    "husky": 5,
    "chihuahua": 3
}

# FUNCTION SEDERHANA
def is_big_dog(dogbreed):
    return dog_sizes[dogbreed] > 4  # Anjing besar jika ukuran lebih dari 4

# CONTOH PENGGUNAAN BOOLEAN
# Memeriksa ukuran setiap anjing
for dogbreed in dog_sizes:
    if is_big_dog(dogbreed):
        print(f"{dogbreed} is a big dog.")
    else:
        print(f"{dogbreed} is a small dog.")

# SPACING BARIS
print()

# CONTOH TUPLE + F-STRING
name = ("Agus", "Edi", "Tim")
print(f"hello {name[1]}")

# SPACING BARIS
print()

# TES MEMBUAT PIRAMIDA

# Jumlah baris piramida
height = 5

# Membuat setengah piramida yang menghadap ke atas
for i in range(1, height + 1):
    # Mencetak spasi untuk mengatur bentuk piramida
    print(" " * (height - i) + "□" * (2 * i - 1))
