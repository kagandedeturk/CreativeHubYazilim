# dosya = open("metin.txt")
# icerik = dosya.read()
# print(icerik)
# dosya.close()


# dosya = open("metin.txt", encoding="utf-8")
# icerik = dosya.read()
# print(icerik)
# dosya.close()




# with open("metin.txt") as dosya:
#     icerik = dosya.read()
#     print(icerik)


# with open("metin.txt",encoding="utf-8") as dosya:
#     icerik = dosya.read()
#     print(icerik)


'''
Eger mode yoksa, varsayilan olarak 'r' yani read(okuma) modundadir
okuma modunda dosyayi acar ve read() fonksiyonu ile dosyanin iceriginin tamamini 
string olarak donderir
'''

# with open("metin.txt") as f:  # f degisken ismi, istedigim degisken ismini verebilirim, yukarida dosya ismini vermistik
#     f.write("13. Python dersine hos geldiniz")

    


'''
Eger mode 'w' ise, yani write(yazma)  
dosya ismi yoksa o dosyayi olusturur ve yazilmak isteneni icine yazar
dosya ismi varsa o dosyanin icerigini tamamen siler ve yazilmak isteneni yazar
'''

# with open("metin.txt", mode="w", encoding="utf-8") as f:  # 
#     f.write("13. Python dersine hoş geldiniz")


# with open("metin2.txt", mode="w", encoding="utf-8") as f:  # 
#     f.write("13. Python dersine hoş geldiniz")


'''
Eger mode 'a' ise, yani append(ekleme) 
dosya ismi yoksa o dosyayi olusturur ve yazilmak isteneni icine yazar
dosya ismi varsa o dosyanin sonuna yazilmak isteneni ekler
'''

with open("metin.txt", mode="a", encoding="utf-8") as f:  # 
    f.write("\n13. Python dersine hoş geldiniz")