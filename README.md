# Kütüphane Yönetim Sistemi: Proje Planı

Bu plan, "Kütüphane Yönetim Sistemi" mini proje ödevine göre hazırlanmıştır. Kod içermez; sadece adımlar, şablon ve dosya şeması vardır.

---

## 1. Dosya Şeması

```
kutuphane_projesi/
│
├── main.py            # Programın giriş noktası (menüler, kullanıcı etkileşimi)
├── models.py          # Book, Novel, Magazine, User sınıfları
├── library.py         # Library sınıfı (kaydetme/yükleme dahil)
├── data/
│   └── library.json   # Kalıcı veri dosyası (program oluşturur)
└── README.md          # Kısa açıklama ve çalıştırma talimatı
```

Basit tutmak istersen `models.py` ve `library.py` dosyalarını tek dosyada birleştirebilirsin. Ödev bunu zorunlu kılmıyor.

---

## 2. Yapılacak Adımlar

**Adım 1: Klasörü ve dosyaları oluştur**
- Yukarıdaki şemaya göre boş dosyaları aç.

**Adım 2: `Book` sınıfı**
- Özellikler: `title`, `author`, `publication_year`, `is_borrowed` (başlangıçta False), `borrowed_by` (başlangıçta None)
- `show_info()`: kitap bilgisini ve durumunu yazdırır
- `borrow(user)`: kitap zaten alınmışsa reddeder, değilse durumu ve `borrowed_by` alanını günceller
- `return_book()`: durumu sıfırlar
- `to_dict()`: tüm alanları sözlük olarak döndürür

**Adım 3: `Novel` ve `Magazine` sınıfları**
- `Book`'tan kalıtım alır, `super()` ile ana kurucuyu çağırır
- `Novel` ek olarak `genre`, `Magazine` ek olarak `issue` tutar
- `to_dict()` içinde ek alanı da ekle
- JSON'da kitabın türünü ayırt etmek için bir `"type"` alanı ekle ("novel" veya "magazine"). Yüklerken hangi sınıftan nesne üreteceğini buradan anlarsın.

**Adım 4: `User` sınıfı**
- Özellikler: `name`, `password`, `borrowed_books` (liste)
- `borrow_book(book)`: kitabı ödünç alır ve kendi listesine ekler
- `return_book(book)`: kitabı iade eder ve listeden çıkarır
- `list_borrowed_books()`: ödünç alınanları yazdırır
- `to_dict()`: kullanıcının bilgilerini döndürür. `borrowed_books` için kitap nesnelerini değil, sadece **başlıklarını** (veya kimliklerini) sakla.

**Adım 5: `Library` sınıfı (temel metotlar)**
- Özellikler: `name`, `books` (liste), `users` (liste)
- `add_book(book)` ve `add_user(user)`
- `show_all_books()`: her kitabın `show_info()` çıktısını gösterir
- `login(name, password)`: eşleşen kullanıcıyı döndürür, yoksa None

**Adım 6: `save(file)` metodu**
- Tüm kitapları ve kullanıcıları `to_dict()` ile sözlüğe çevir
- Tek bir JSON yapısında dosyaya yaz (`data/` klasörü yoksa oluştur)

**Adım 7: `load(file)` metodu**
- Dosya yoksa boş bir kütüphane ile başla (program çökmemeli)
- Önce kitapları `"type"` alanına göre doğru sınıftan yeniden oluştur
- Sonra kullanıcıları oluştur
- En son ilişkileri geri kur: her kullanıcının kayıtlı kitap başlıklarına karşılık gelen kitap nesnesini bulup `borrowed_books` listesine koy

**Adım 8: `main.py` ve program akışı**
- Başlangıçta `load()` ile verileri yükle
- İlk çalıştırmada kütüphane boşsa örnek birkaç kitap ekle
- Giriş ekranı: giriş yap veya hesap oluştur
- Menü döngüsü (1-5) ve çıkışta `save()`

**Adım 9: Test et**
- Hesap oluştur, kitap al, çık, programı yeniden aç
- Kitabın ve kullanıcının durumunun korunduğunu kontrol et
- Hatalı durumları dene: yanlış şifre, zaten alınmış kitap, ödünç alınmamış kitabı iade etme, geçersiz menü seçimi

---

## 3. Kod Şablonu (Sadece İskelet)

### models.py

```
class Book:
    __init__(title, author, publication_year)
        # is_borrowed = False, borrowed_by = None
    show_info()
        # TODO: bilgiyi ve durumu yazdır
    borrow(user)
        # TODO: zaten alınmışsa uyar, değilse durumu güncelle
    return_book()
        # TODO: durumu sıfırla
    to_dict()
        # TODO: sözlük döndür ("type" alanı dahil)

class Novel(Book):
    __init__(title, author, publication_year, genre)
        # TODO: super() çağır, genre ekle
    to_dict()
        # TODO: ana sözlüğe genre ekle

class Magazine(Book):
    __init__(title, author, publication_year, issue)
        # TODO: super() çağır, issue ekle
    to_dict()
        # TODO: ana sözlüğe issue ekle

class User:
    __init__(name, password)
        # borrowed_books = []
    borrow_book(book)
        # TODO
    return_book(book)
        # TODO
    list_borrowed_books()
        # TODO
    to_dict()
        # TODO: kitapları başlıkla sakla
```

### library.py

```
class Library:
    __init__(name)
        # books = [], users = []
    add_book(book)
    add_user(user)
    show_all_books()
    login(name, password)
    save(file)
        # TODO: kitapları + kullanıcıları JSON'a yaz
    load(file)
        # TODO: 1) kitaplar  2) kullanıcılar  3) ilişkiler
```

### main.py

```
def giris_ekrani(library):
    # TODO: giriş yap / hesap oluştur, User döndür

def menu(library, user):
    # TODO: 1-5 döngüsü

def main():
    # 1. Library oluştur
    # 2. load()
    # 3. giris_ekrani()
    # 4. menu()
    # 5. save() (çıkışta)

if __name__ == "__main__":
    main()
```

---

## 4. Dikkat Edilecek Noktalar

- **En kritik kısım `load()`.** İlişkileri geri kurmak ödevin asıl zorluğu. Bu yüzden kitapları ve kullanıcıları bu sırayla yükle.
- **Ödünç alma iki taraflı çalışır.** `borrow` işleminde hem kitabın (`is_borrowed`, `borrowed_by`) hem de kullanıcının (`borrowed_books`) güncellenmesi gerekir. İkisini birden yapmayı unutma.
- **`borrowed_by` için** kullanıcı nesnesi yerine kullanıcı adını sakla. Böylece JSON'a yazarken sorun yaşamazsın.
- **Şifreyi** ödev düz metin olarak istiyor, o yüzden basit tutabilirsin.
- **Aynı kullanıcı adıyla** ikinci hesap açılmasını engelle.

Adım adım ilerlersen (önce `Book`, sonra `User`, sonra `Library`, en son `main.py`) her aşamayı ayrı ayrı test edebilirsin.
