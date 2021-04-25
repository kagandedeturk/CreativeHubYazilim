
import sqlite3

con = sqlite3.connect("SIFRE_YONETIM.db") # Veritabani varsa baglanir, yoksa olusturur ve baglanir

cursor = con.cursor()



def tablo_olustur(sql):
    cursor.execute(sql)
    con.commit()
    print("Tablo olusturuldu")

def veri_ekle(websitesi, kullanici_adi, sifre):
    sql = f"INSERT INTO SIFRELER(WebSitesi,KullaniciAdi,Sifre) VALUES('{websitesi}','{kullanici_adi}','{sifre}')"
    cursor.execute(sql)
    con.commit()

def tum_verileri_getir():
    sql = "SELECT * FROM SIFRELER" # Tablodaki tum sutunlari getirmek istiyorsam * isaretini kullanabilirim
    # sql = "SELECT Id,WebSitesi,KullaniciAdi,Sifre FROM SIFRELER"
    # sql = "SELECT WebSitesi FROM SIFRELER"
    # sql = "SELECT WebSitesi,KullaniciAdi,Sifre FROM SIFRELER"
    cursor.execute(sql)
    veriler = cursor.fetchall()
    for item in veriler:
        for eleman in item:
            print(eleman, end="\t")
        print()


def veri_getir(websitesi):
    sql = f"SELECT * FROM SIFRELER WHERE WebSitesi = '{websitesi}'"
    cursor.execute(sql)
    veriler = cursor.fetchall()
    for i in veriler:
        print(i)


def veri_getir2(id):
    sql = f"SELECT * FROM SIFRELER WHERE Id = {id}"
    cursor.execute(sql)
    veriler = cursor.fetchall()
    print(veriler)
    for i in veriler:
        print(i)


def sifre_guncelle(web,sifre):
    sql = f"UPDATE SIFRELER SET Sifre='{sifre}' WHERE WebSitesi='{web}'"
    #"UPDATE SIFRELER SET Sifre='12345' WHERE WebSitesi='www.hepsiburada.com'"
    cursor.execute(sql)
    con.commit()

def sifre_guncelle2(id,sifre):
    sql = f"UPDATE SIFRELER SET Sifre='{sifre}' WHERE Id={id}"
    #"UPDATE SIFRELER SET Sifre='12345' WHERE WebSitesi='www.hepsiburada.com'"
    cursor.execute(sql)
    con.commit()

def sifre_guncelle3(id,sifre,kullanici_adi):
    sql = f"UPDATE SIFRELER SET KullaniciAdi='{kullanici_adi}', Sifre='{sifre}'  WHERE Id={id}"
    #"UPDATE SIFRELER SET Sifre='12345' WHERE WebSitesi='www.hepsiburada.com'"
    cursor.execute(sql)
    con.commit()


def veri_sil(websitesi):
    sql = f"DELETE FROM SIFRELER WHERE WebSitesi='{websitesi}'"
    cursor.execute(sql)
    con.commit()


def veri_sil2(id):
    sql = f"DELETE FROM SIFRELER WHERE Id={id}"
    cursor.execute(sql)
    con.commit()

def tum_verileri_sil():
    sql = "DELETE FROM SIFRELER"
    cursor.execute(sql)
    con.commit()

tablo_sql = '''CREATE TABLE IF NOT EXISTS SIFRELER(
    Id INTEGER Primary Key AUTOINCREMENT,
    WebSitesi TEXT,
    KullaniciAdi Text,
    Sifre Text
)'''

# tablo_olustur(tablo_sql)

# Tabloya yeni veri ekleme, tabloya satir ekleme





# veri_ekle('www.trendyol.com','kagandedeturk@gmail.com','Python135')
# veri_ekle('www.garantibbva.com.tr','25199255234','Python12345')
# veri_ekle('www.hepsiburada.com','kagandedeturk@gmail.com','Python246')
# veri_ekle('www.morhipo.com','bkdedeturk','xyz357')


# sifre_guncelle("www.hepsiburada.com","1234567")
# sifre_guncelle2(5, "abc111*222")
# sifre_guncelle3(3, sifre='PxCDabc235', kullanici_adi='kagandedeturk@hotmail.com')

# veri_sil("www.garantibbva.com.tr")
# veri_sil2(4)

tum_verileri_sil()

tum_verileri_getir()


# veri_getir("www.hepsiburada.com")
# veri_getir2(12)

con.close() # Veritabanina acilan baglantiyi kapatir.