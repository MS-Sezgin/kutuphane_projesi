# main.py
# Programin giriş noktasi: giriş ekrani, menü ve kaydet/çik akişi.

# ---------------------------------------------------------
# def giris_ekrani(library):
#     # TODO: giriş yap / hesap oluştur, User döndür
#
# def menu(library, user):
#     # TODO: 1-5 döngüsü
#     # 1 - Tüm kitaplari listele
#     # 2 - Kitap ödünç al
#     # 3 - Kitap iade et
#     # 4 - Ödünç aldiğim kitaplari göster
#     # 5 - Kaydet ve çik
#
# def main():
#     # 1. Library oluştur
#     # 2. load()
#     # 3. giris_ekrani()
#     # 4. menu()
#     # 5. save() (çikişta)
#
# if __name__ == "__main__":
#     main()
# ---------------------------------------------------------
from models import Book, Novel, Magazine, User
from library import Library


def giris_ekrani(lib: Library):
    while True:
        print("\n1 - Giriş yap")
        print("2 - Hesap oluştur")
        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("Kullanici adi: ")
            sifre = input("Şifre: ")
            kullanici = lib.login(isim, sifre)
            if kullanici is not None:
                print(f"Hoş geldin, {kullanici.name}!")
                return kullanici
            else:
                print("İsim veya şifre hatali.")

        elif secim == "2":
            isim = input("Yeni kullanici adi: ")

            if any(u.name == isim for u in lib.users):
                print("Bu kullanici adi zaten alinmiş.")
                continue

            sifre = input("Şifre: ")
            yeni_kullanici = User(isim, sifre)
            lib.add_user(yeni_kullanici)
            print(f"Hesap oluşturuldu. Hoş geldin, {isim}!")
            return yeni_kullanici

        else:
            print("Geçersiz seçim.")


def menu(lib: Library, user: User):
    while True:
        print("\n1 - Tüm kitaplari listele")
        print("2 - Kitap ödünç al")
        print("3 - Kitap iade et")
        print("4 - Ödünç aldigim kitaplar")
        print("5 - Kaydet ve çik")
        secim = input("Seçiminiz: ")

        if secim == "1":
            lib.show_all_books()

        elif secim == "2":
            baslik = input("Almak istediğin kitabin adi: ")
            #kitap = next((k for k in lib.books if k.title == baslik), None)
            #        └┬─┘ └┬────────────────────────────────────────────┘  └┬─┘
            #         │     generator: lib.books içindeki her k için,   │
            #         │     k.title == baslik ise k'yı üret                 │
            #         │                                                     │
            #ilk eşleşen elemanı al                           eşleşme yoksa bu değeri döndür
            kitap = None
            for k in lib.books:
                if k.title == baslik:
                    kitap = k
                    break
            if kitap is None:   
                print("Böyle bir kitap bulunamadi.")
            else:
                user.borrow_book(kitap)

        elif secim == "3":
            baslik = input("İade etmek istediğin kitabin adi: ")
            kitap = next((k for k in user.borrowed_books if k.title == baslik), None)
            if kitap is None:
                print("Bu kitabi almamissin.")
            else:
                user.return_book(kitap)

        elif secim == "4":
            user.list_borrowed_books()

        elif secim == "5":
            lib.save("data/library.json")
            print("Veriler kaydedildi. Güle güle!")
            break

        else:
            print("Geçersiz seçim.")




if __name__ == "__main__":
    lib = Library("Şehir Kütüphanesi")
    lib.kitaplari_yukle("data/library.json")

    if not lib.books:
        lib.add_book(Novel("Sefiller", "Victor Hugo", 1862, "Dram"))
        lib.add_book(Novel("1984", "George Orwell", 1949, "Distopya"))
        lib.add_book(Magazine("National Geographic", "Çeşitli Yazarlar", 2024, "Ekim Sayisi"))

    kullanici = giris_ekrani(lib)#giris methoduna git ve bana bir kullanıcı geri dondur
    menu(lib, kullanici)