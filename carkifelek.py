import random
from datetime import datetime
import os
import winsound  # Ses

print("""** Kullanıcı Girişi
      Kurallar:
            1. Oyuncular sırayla çarkı çevirirler.
            2. Çarkın üzerinde farklı puanlar ve "iflas" seçeneği bulunmaktadır.
            3. Oyuncular bir harf tahmin edebilir ya da kelimeyi tahmin edebilirler.
            4. Eğer "iflas" gelirse, oyuncunun puanı sıfırlanır.
            5. Doğru tahmin edilen harf sayısı kadar puan kazanılır.
            6. Sistem tarafından verilen harfler tekrar kullanılamaz.
            7. Oyun sonunda en yüksek puanı toplayan oyuncu kazanır.
            8. Oyuncuların doğum tarihi ve isimleri gereklidir.
*******************""")

skorlar = {}

if os.path.exists("skorlar.txt"):
    with open("skorlar.txt", "r", encoding="UTF-8") as file:
        for line in file:
            ad, skor = line.strip().split(":")
            skorlar[ad] = int(skor)

def cevir_cark():
    puanlar = ["iflas", 0, 50, 100, 200, 250, 300, 400, 500, 1000]
    return random.choice(puanlar)

while True:
    try:
        kullanici_sayisi = int(input("Kaç kişi yarışmaya katılacak?: "))
        if kullanici_sayisi < 1:
            print("En az bir kişi olmalı!")
        else:
            break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")

kullanicilar = []

def dogum_tarihi_al():
    while True:
        kullanici_dogumtarihi = input("Lütfen Doğum tarihinizi (YYYY-AA-GG) giriniz: ")
        try:
            dogum_tarihi = datetime.strptime(kullanici_dogumtarihi, "%Y-%m-%d")
            break
        except ValueError:
            print("Lütfen geçerli bir tarih formatı (YYYY-AA-GG) giriniz.")

for i in range(kullanici_sayisi):
    while True:
        kullanici_adi = input(f"\n{i+1}. Yarışmacı - İsim ve Soyisim: ").strip()
        if kullanici_adi:
            dogum_tarihi_al()
            kullanicilar.append(kullanici_adi)
            break
        else:
            print("Lütfen geçerli bir isim giriniz!")

sorular = {
    "Makine öğrenmesinde kullanılan en yaygın programlama dili nedir?": ("Python", 100),
    "Hangi makine öğrenmesi yöntemi, verilerin gruplandırılması için kullanılır ve etiketlenmemiş verilerle çalışır?": ("Kümeleme", 200),
    "Makine öğrenmesinde 'overfitting' sorununu azaltmak için kullanılan yöntemlerden biri nedir?": ("Dropout", 300)
}

skorlar = {kullanici: skorlar.get(kullanici, 0) for kullanici in kullanicilar}

automatic_harfler = ["b", "c", "d", "y", "z", "ü"]

def guncelle_gizli_cevap(cevap, acilan_harfler):
    return " ".join(harf if harf in acilan_harfler else "_" for harf in cevap)

def goster_harfler(kullanilan_harfler, cevap):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    renkli_harfler = []

    for harf in alfabe:
        if harf in kullanilan_harfler:
            if harf in cevap:
                renkli_harfler.append(f"\033[92m{harf}\033[0m")  # Yeşil renk
            else:
                renkli_harfler.append(f"\033[91m{harf}\033[0m")  # Kırmızı renk
        elif harf in automatic_harfler:
            renkli_harfler.append(f"\033[91m{harf}\033[0m")
        else:
            renkli_harfler.append(harf)

    print("Size verilen harfler:", " ".join(f"\033[91m{harf}\033[0m" for harf in sorted(automatic_harfler)))
    print("Verilen harfler:", " ".join(renkli_harfler))

for soru, (cevap, soru_puani) in sorular.items():
    print(f"\nSoru: {soru} (Bu sorunun puanı: {soru_puani})\n")
    
    cevap = cevap.lower()
    acilan_harfler = set(harf for harf in automatic_harfler if harf in cevap)
    kullanilan_harfler = set()
    oyuncu_index = 0
    oyun_devam = True
    
    while oyun_devam:
        oyuncu = kullanicilar[oyuncu_index]
        print(f"\nSıradaki oyuncu: {oyuncu}")
        goster_harfler(kullanilan_harfler, cevap)
        
        puan = cevir_cark()
        print(f"Çark çevirildi! Gelen puan: {puan}")

        if puan == "iflas":
            print(f"{oyuncu} iflas etti! Puanı 0'a düşüyor.")
            skorlar[oyuncu] = 0
            oyuncu_index = (oyuncu_index + 1) % kullanici_sayisi
            continue

        if puan == 0:
            print(f"{oyuncu}, 0 puan geldi! Sıra diğer oyuncuya geçiyor.")
            oyuncu_index = (oyuncu_index + 1) % kullanici_sayisi
            continue

        print(f"Gizli cevap: {guncelle_gizli_cevap(cevap, acilan_harfler)}")
        tahmin = input("Kelimeyi tahmin etmek ister misiniz? (Y/N): ").lower()
        
        if tahmin == "y":
            kelime_tahmini = input("Kelime tahmininizi girin: ").lower()
            if kelime_tahmini == cevap:
                print(f"Tebrikler {oyuncu}, doğru tahmin ettiniz!")
                skorlar[oyuncu] += soru_puani
                print(f"{oyuncu}'nun güncel skoru: {skorlar[oyuncu]}")

                # Skor hatırlatması yap
                print("\nSkorlar:")
                for oyuncu, skor in sorted(skorlar.items(), key=lambda item: item[1], reverse=True):
                    print(f"{oyuncu}: {skor} puan")
                    
                oyun_devam = False
                continue
            else:
                print("Yanlış tahmin! Sıra diğer oyuncuya geçiyor.")
                winsound.Beep(2000, 500)
                oyuncu_index = (oyuncu_index + 1) % kullanici_sayisi
                continue
        
        harf = input("Bir harf söyleyin: ").lower()

        # Geçerli harf kontrolü
        if len(harf) != 1 or not harf.isalpha() or harf in kullanilan_harfler or harf in automatic_harfler:
            print("Geçersiz veya tekrar eden harf! Sıra diğer oyuncuya geçiyor.")
            oyuncu_index = (oyuncu_index + 1) % kullanici_sayisi
            continue

        kullanilan_harfler.add(harf)

        if harf in cevap:
            adet = cevap.count(harf)  # Harfin sayısını al
            print(f"\033[92mDoğru!\033[0m {adet} adet '{harf}' harfi var.")
            acilan_harfler.add(harf)
            skorlar[oyuncu] += puan * adet
        else:
            print(f"\033[91mYanlış!\033[0m '{harf}' harfi yok. Sıra diğer oyuncuya geçiyor.")
            oyuncu_index = (oyuncu_index + 1) % kullanici_sayisi



with open("skorlar.txt", "w", encoding="UTF-8") as file:
    for oyuncu, skor in skorlar.items():
        file.write(f"{oyuncu}:{skor}\n")

print("\n\033[1mOyun sona erdi. Kazanan oyuncu:\033[0m")
en_yuksek_puanli_oyuncu = max(skorlar.items(), key=lambda item: item[1])
print(f"{en_yuksek_puanli_oyuncu[0]} ({en_yuksek_puanli_oyuncu[1]} puan)\n")