matriks1 = []
matriks2 = []

print("masukkan elemen untuk matriks pertama (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"masukkan elemen  baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks1.append(baris)

print("\nmasukkan elemen untuk matriks kedua (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks2.append(baris)

operasi = input("\npilih operasi (penjumlahan/pengurangan/perkalian): ").lower()

hasil = []
if operasi == 'penjumlahan':
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matriks1[i][j] + matriks2[i][j])
        hasil.append(baris)
elif operasi == 'pengurangan':
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matriks1[i][j] - matriks2[i][j])
        hasil.append(baris)
elif operasi == 'perkalian':
    for i in range(3):
        baris = []
        for j in range(3):
            nilai = 0
            for k in range(3):
                nilai += matriks1[i][k] * matriks2[k][j]
            baris.append(nilai)
        hasil.append(baris)

else:
    print("operasi tidak valid.")

if hasil:
    print(f"\nhasil {operasi} matriks:") 
    for baris in hasil:
        print(baris)   