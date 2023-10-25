#list mobil
mobil = ["A-Class","Mobil","1900","Merah","4"]
print(mobil)
mobil.append("Rp 100.000.000")
mobil.append("Hatchback")
print(mobil)
mobil.insert(2,"Mercedez")
print(mobil)

#match case hitung luas bangun datar
print("Anda mau menghitung luas apa? Ketik 1 untuk persegi, 2 untuk lingkaran, 3 untuk segitiga.")
pilih = int(input ( ))
match pilih:
    case 1:
        print("Luasnya adalah", int(input ("Masukkan Sisinya: ")) ** 2)
    case 2:
        print("Luasnya adalah", int(3.14 * int(input ("Masukkan Jari-Jarinya: ")) ** 2))
    case 3:
        print("Luasnya adalah", int(1/2 * int(input ("Masukkan Alasnya: ")) * int(input ("Masukkan Tingginya: "))))
    case _:
        print("salah pilih angka")