
import sqlite3


class DB:

    def __init__(self):
        self.con = sqlite3.connect("SIFRE_YONETIM.db") # Veritabani varsa baglanir, yoksa olusturur ve baglanir
        self.cursor = self.con.cursor()
        tablo_sql = '''CREATE TABLE IF NOT EXISTS SIFRELER(
                        Id INTEGER Primary Key AUTOINCREMENT,
                        WebSitesi TEXT,
                        KullaniciAdi Text,
                        Sifre Text
                    )'''
        
        self.tablo_olustur(tablo_sql)


    def tablo_olustur(self,sql):
        self.cursor.execute(sql)
        self.con.commit()
        print("Tablo olusturuldu")

    
    def kayit_ekle(self,websitesi,kullanici_adi,sifre):

        sql = f"SELECT * FROM SIFRELER WHERE WebSitesi='{websitesi}'"
        self.cursor.execute(sql)
        veriler = self.cursor.fetchall()
        if len(veriler) == 0:
            sql = f"INSERT INTO SIFRELER(WebSitesi,KullaniciAdi,Sifre) VALUES('{websitesi}','{kullanici_adi}','{sifre}')"
            self.cursor.execute(sql)
            self.con.commit()

        else:
            sql = f"UPDATE SIFRELER SET KullaniciAdi='{kullanici_adi}',Sifre='{sifre}' WHERE WebSitesi='{websitesi}'"
            self.cursor.execute(sql)
            self.con.commit()


    def baglati_kapat(self):
        self.con.close()