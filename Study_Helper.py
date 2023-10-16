from _datetime import datetime
from playsound import playsound


import time
import winsound
not_defteri=dict({})


zaman=datetime.now()
zaman_str=str(zaman)
#while dongusu olsuturcam ve dongu hata da alsa hep bir kullanicidan ne istedigini soracak
while True:
    print("1)Not defteri icin 1 i tuşlayın")
    print("2)Zaman,Tarih veya Gun bilgisi icin 2 yi tuslayın")
    print("3)Kronometre icin 3 ü tuslayın")
    print("4)Alarm icin 4 tuslayın")
    x=input("Seciminiz=")
    if x=="1":
        while True:
            print("1)Not Eklemek icin 1 i tuşlayın")
            print("2)Notları Görüntülemek icin 2 tuşlayın")
            print("3)Çıkış için 3 tuşlayın")

            secim = input("Bir seçenek seçin= ")

            if secim == "1":
                baslik = input("Not Başlığı: ")
                not_icerik = input("Not İçeriği: ")
                not_defteri[baslik] = not_icerik
                print("Not eklenmiştir.")

            elif secim == "2":
                print("Notlar:")
                for baslik, not_icerik in not_defteri.items():
                    print(f"{baslik}: {not_icerik}")
            elif secim == "3":
                print("Not defterinden çıkılıyor.")
                break
            else:
                print("Geçersiz seçenek. Lütfen tekrar deneyin.")
    if x=="2":
        while True:
            print("Tarih için 1 i tuşlayın")
            print("Saat için 2 yi tuşayin")
            print("Gün için 3 ü tuslayın")
            print("Çikiş için 4 ü tuşlayın")
            secim_2=input("Bir seçenek seçin=")
            if secim_2=="1":
                k=(str(datetime.today()))
                print(k[0:10:])
            elif secim_2=="2":
                k = (str(datetime.today()))
                print(k[11:19:])
            elif secim_2=="3":
                print(datetime.today().strftime("%A"))
            elif secim_2=="4":
                print("Zaman gosteriminden çikiş yapiliyor")
                break
            else:
                print("Geçersiz seçenek. Lütfen tekrar deneyin.")
    if x=="3":
        while True:
            print("Kronometreyi baslatmak icin 1 i tuslayin")
            print("Kronometreden cikmak icin 2 yi tuslayın")
            secim_3=input("Bir seçenek seçin=")

            if secim_3=="1":
                print("Kronometre baslatildi,bitirmek icin entera basin")
                baslangic_zamani=time.time()
                input()
                bitis_zamani=time.time()
                x=bitis_zamani - baslangic_zamani
                print(f"Kronometre sonlandi,Geçen süre={x}")


            elif secim_3=="2":
                print("kronometreden çikiliyor")
                break
            else:
                print("Geçersiz seçenek. Lütfen tekrar deneyin.")
    if x=="4":
        while True:
            print("Alarm kurmak için 1 i tuslayin")
            print("Alarm dan cikmak icin 2 e basin")
            secim_4 = input("Bir seçenek seçin=")
            if secim_4=="1":

                ö=input("Alarmı kaca kurmak ıstersınız sifir ve bosluga dikkat ediniz ör:02.10=")
                print("Alarm kuruldu ve süreçte")
                alarm_bitis=ö[0:2:]+ö[3:5:]
                i = (str(datetime.today()))
                anlik_zaman = i[11:13:] + i[14:16:]
                while alarm_bitis!=anlik_zaman:
                    i=(str(datetime.today()))
                    anlik_zaman=i[11:13:]+i[14:16:]
                playsound("Alarm-Sesi.mp3")
                print("Alarim bitti")


            elif secim_4=="2":
                print("Alarımdan çıkılıyor")
                break
            else:
                print("Geçersiz seçenek. Lütfen tekrar deneyin.")


    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")























































