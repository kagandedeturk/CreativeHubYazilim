
# metin = "deneme :   calisma deneme    : 1 : 2"

# x = metin.split(":")
# # print(x)

# for eleman in x:
#     print(eleman.strip())


# metin = "deneme : calisma : 1 : 2"

# x = metin.split()
# print(x)


# metin = "deneme : calisma : 1 : 2"

# x = metin.replace("calisma","study")
# print(x)


# ana program

degisecek_str = "[isim]"

with open("./Ders-13/OtomatikMektup/Girdi/Isimler/isimler.txt",encoding="utf-8") as dosya:
    isimler = dosya.readlines()



with open("./Ders-13/OtomatikMektup/Girdi/Mektuplar/ornek_mektup.txt",encoding="utf-8") as dosya:
    ornek_mektup = dosya.read()
    for isim in isimler:
        bosluksuz_isim = isim.strip()
        yeni_mektup = ornek_mektup.replace(degisecek_str, bosluksuz_isim)
        with open(f"./Ders-13/OtomatikMektup/Cikti/mektup_{bosluksuz_isim}.txt", mode="w") as mektup_dosyasi:
            mektup_dosyasi.write(yeni_mektup)

