# Kütüphane Yönetim Sistemi

Python ile yazılmış basit bir Kütüphane Yönetim Sistemi. Kullanıcılar kitap
ödünç alıp iade edebilir. Veriler JSON dosyasında saklanır, program kaldığı
yerden devam eder.

## Dosya Yapısı

```
kutuphane_projesi/
├── main.py            # Giriş noktası (menüler, kullanıcı etkileşimi)
├── models.py          # Book, Novel, Magazine, User sınıfları
├── library.py         # Library sınıfı (kaydetme/yükleme dahil)
├── data/
│   └── library.json   # Kalıcı veri (program ilk kayıtta oluşturur)
└── README.md
```

## Çalıştırma

```
python main.py
```

## Menü

1. Tüm kitapları listele
2. Kitap ödünç al
3. Kitap iade et
4. Ödünç aldığım kitapları göster
5. Kaydet ve çık
