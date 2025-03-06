Çarkıfelek Oyunu

Bu oyun, klasik çarkıfelek tarzı oynanış ile makine öğrenmesi konusundaki soruların cevaplanmasını bir araya getiriyor. Oyuncular sırayla çarkı çevirir, harf tahminleri yapar veya doğrudan kelime tahmininde bulunarak puan toplamaya çalışırlar. Oyuncuların isim ve doğum tarihi bilgileri alınır, doğru cevaplanan sorulara göre puan eklenir ve oyun sonunda en yüksek puana sahip oyuncu kazanır.

İçindekiler

- Genel Bakış
- Özellikler
- Kurulum ve Gereksinimler
- Oyunun Çalıştırılması
- Oyun Kuralları ve Nasıl Oynanır?
- Dosya ve Veri Yönetimi
- Notlar ve İyileştirme Önerileri

Genel Bakış:
Bu Python tabanlı oyun, oyuncuların sırasıyla çarkı çevirdikleri, harf ve kelime tahminleri yaptıkları bir yarışmadır. Her turda oyuncuların alacağı puan, çarkın döndürülmesiyle belirlenir. Oyuncuların topladığı puanlar, soru bazında belirlenen ödül puanlarıyla çarpılarak eklenir. Yanlış tahminlerde veya "iflas" sonucunda puan sıfırlanabilir.

Özellikler:
- Çark Çevirme: Oyuncuların puanlarını belirlemek için rastgele puan ya da "iflas" sonucu üretir.
- Soru-Cevap: Makine öğrenmesi ile ilgili sorular üzerinden oyun oynanır.
- Harf Tahmini: Oyuncular, verilen otomatik harfler dışında harf seçerek kelimeyi açmaya çalışır.
- Kelime Tahmini: Oyuncular, tam kelimeyi tahmin ederek soruyu kazanabilirler.
- Skor Takibi: Oyun sonunda tüm oyuncuların skorları hesaplanır ve en yüksek puanı alan oyuncu kazanan ilan edilir.
- Ses Efekti: Yanlış kelime tahminlerinde ses efekti (winsound modülü) çalar.
- Dosya Kaydı: Oyuncuların skorları, skorlar.txt dosyasına kaydedilir.

Kurulum ve Gereksinimler

Gereksinimler:
- Python 3.11: Oyun, Python 3.11 ile yazılmıştır. Python'un resmi sitesinden uygun sürümü indirebilirsiniz.
- İşletim Sistemi: winsound modülü Windows işletim sistemine özgüdür. (Linux veya macOS kullanıyorsanız, winsound yerine alternatif bir modül kullanmanız gerekebilir veya winsound satırlarını yoruma alabilirsiniz.)

Gerekli Python Kütüphaneleri:
- random
- datetime
- os
- winsound
Bu modüller Python ile birlikte geldiğinden ekstra bir yükleme yapmanıza gerek yoktur.

Dosya İçi:
- carkilefek.py: Bu dosya, oyunun ana kodunu içerir.
- skorlar.txt: Oyuncuların skorlarını kaydeden dosya. (Oyun ilk çalıştırıldığında otomatik olarak oluşturulur.)

Oyunun Çalıştırılması:
- Python'u Kurun: Bilgisayarınızda Python 3.11 yüklü değilse, Python'un indirme sayfasından uygun sürümü indirin ve kurun.
- Kod Dosyasını İndirin: Kodunuzu içeren carkilefek.py dosyasını bilgisayarınıza kaydedin.
- Komut Satırı veya Terminal Açın:
Windows’da Komut İstemi veya PowerShell kullanabilirsiniz.
Dosyanın bulunduğu dizine geçmek için cd komutunu kullanın.
- Oyunu Başlatın: Terminale aşağıdaki komutu yazarak oyunu çalıştırın:
    - bash
    - Copy
    - Edit
    - python carkilefek.py
- Oyun Başlasın: Komut satırındaki yönergeleri takip edin. Oyuna katılacak kişi sayısını, oyuncu isimlerini ve doğum tarihlerini girerek oyuna başlayabilirsiniz.

Oyun Kuralları ve Nasıl Oynanır?
Oyunun başında ekrana kuralların detayları yazılır. İşte temel kurallar:

- Oyuncu Sırası: Oyuncular sırayla çarkı çevirir.
- Çarkın Puanları: Çark, farklı puanlar (0, 50, 100, vb.) veya "iflas" sonucu verir.
- Harf ve Kelime Tahmini: Oyuncular, harf tahmin edebilir veya kelimeyi doğrudan tahmin edebilir.
- "İflas" Durumu: Eğer çark "iflas" sonucu verirse, o oyuncunun puanı sıfırlanır.
- Doğru Harf Tahmini: Doğru tahmin edilen her harf için oyuncuya, çarkın puanı kadar puan eklenir.
- Harflerin Kullanımı: Sistem tarafından verilen bazı harfler (örneğin, otomatik verilen "b", "c", "d", "y", "z", "ü") tekrar kullanılamaz.
- Kazanan: Oyun sonunda en yüksek puanı toplayan oyuncu oyunu kazanır.

Dosya ve Veri Yönetimi
- Skor Kaydı: Her oyun sonunda, oyuncuların skorları skorlar.txt dosyasına kaydedilir. Böylece bir sonraki oyun başladığında önceki skorlar da okunabilir.
- Doğrulama: Oyuncu isimlerinin ve doğum tarihlerinin doğru formatta girilmesi sağlanır.

Notlar ve İyileştirme Önerileri
- Platform Uyumluluğu:
Winsound modülü sadece Windows'ta çalışır. Eğer farklı bir işletim sistemi kullanıyorsanız, ses efektleri için alternatif kütüphane araştırabilirsiniz.
- Harf Girişleri: 
Harf girişleri için girilen verilerin kontrolü yapılmaktadır; kullanıcıdan gelen hatalı girişlerde sıra otomatik olarak sonraki oyuncuya geçer.


