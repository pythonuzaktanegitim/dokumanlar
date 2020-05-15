import sqlite3 as sql

class DBTool():

    def __init__(self,adres="Harcama.db"):
        self.adres = adres
        self.db = sql.connect(self.adres)
        self.cur = self.db.cursor()

    def select(self,**kwargs):
        sorgu = ""
        for key,value in kwargs.items():
            if key == "Tablo":
                sorgu += "SELECT * FROM {}".format(value)
            if key == "Sart":
                sorgu += "WHERE {}".format(value)
        return self.cur.execute(sorgu).fetchall()

    def insert(self,hrckalem,hrctip,hrcay,hrctutar):
        islemSonuc = ""
        try:
            sorgu = f"""
            INSERT INTO HRC_TAKIP (   HRC_KALEM,
                          HRC_TIP,
                          HRC_AY,
                          HRC_TUTAR
                      )
                      VALUES (
                          {hrckalem},
                          {hrctip},
                          {hrcay},
                          {hrctutar}
                      )"""
            self.cur.execute(sorgu)
            self.db.commit()
            islemSonuc = "1"
        except Exception as hata:
            islemSonuc = hata
        finally:
            return islemSonuc

    def update(self,hrckalem,hrctip,hrcay,hrctutar,hrcid):
        islemSonuc = ""
        try:
            sorgu = f"""
                UPDATE HRC_TAKIP
                SET HRC_KALEM = {hrckalem},
                HRC_TIP = {hrctip},
                HRC_AY = {hrcay},
                HRC_TUTAR = {hrctutar}
                WHERE HRC_ID = {hrcid}"""
            self.cur.execute(sorgu)
            self.db.commit()
            islemSonuc = "1"
        except Exception as hata:
            islemSonuc = hata
        finally:
            return islemSonuc

    def delete(self,hrcid):
        islemSonuc = ""
        try:
            sorgu = f"""
                DELETE FROM HRC_TAKIP where HRC_ID = {hrcid}"""
            self.cur.execute(sorgu)
            self.db.commit()
            islemSonuc = "1"
        except Exception as hata:
            islemSonuc = hata
        finally:
            return islemSonuc


