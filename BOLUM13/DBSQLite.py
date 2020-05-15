import sqlite3 as sql
try:
    db = sql.connect(r"IK.sqlite")
    cur = db.cursor()
    cur.execute("SELECT personel_id,adi,soyadi,email FROM personeller LIMIT 5")
    print(*cur.fetchmany(6),sep="\n")
    lokasyon = input("Lokasyon Giriniz:")
    adi = input("Departman Adı Giriniz:")
    sorgu =  f"""
                INSERT INTO departmanlar (
                lokasyon_id,
                departman_adi
                )
                VALUES (
                {lokasyon},
                '{adi}'
                );
            """
    cur.execute(sorgu)
    db.commit()
except Exception as hata:
    print(hata)
finally:
    db.close()