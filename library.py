import os
import json
from models import Book, Novel, Magazine, User
# library.py
# Library sınıfı burada yazılacak (kaydetme/yükleme dahil).

# ---------------------------------------------------------
# class Library
#   __init__(name)
#       # books = [], users = []
#   add_book(book)
#   add_user(user)
#   show_all_books()
#   login(name, password)
#   save(file)
#       # TODO: kitapları + kullanıcıları JSON'a yaz
#       #       (data/ klasörü yoksa oluştur)
#   load(file)
#       # TODO: dosya yoksa boş başla
#       # 1) kitaplar ("type" alanına göre Novel / Magazine)
#       # 2) kullanıcılar
#       # 3) ilişkiler (borrowed_books listelerini geri kur)
# ---------------------------------------------------------
class Library():
    def __init__(self,name,books=None,users=None):
        self.name=name
        self.books = books if books is not None else [] 
        self.users = users if users is not None else []
    def add_book(self,book):
        self.books.append(book)
    def add_user(self,user):
        self.users.append(user)
    def show_all_books(self):
        if not self.books:
            print("Kütüphanede hiç kitap yok.")
        else:
            print(f"--- {self.name} Kitap Listesi ---")
            for book in self.books:
                book.show_info()
    def login(self, name, password):
        for user in self.users:
            if user.name == name and user.password == password:
                return user
        return None
    
    def save(self, file_path):
        books_data = [book.to_dict() for book in self.books]
        users_data = [user.to_dict() for user in self.users]

        data = {
            "books": books_data,
            "users": users_data
        }

        klasor = os.path.dirname(file_path)
        if klasor and not os.path.exists(klasor):
            os.makedirs(klasor)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def kitaplari_yukle(self, file):
        if not os.path.exists(file):
            self.books = []
            self.users = []
            return

        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 1) Kitapları oluştur
        self.books = []
        for kitap_verisi in data["books"]:
            tur = kitap_verisi["type"]
            if tur == "novel":
                kitap = Novel(
                    kitap_verisi["title"],
                    kitap_verisi["author"],
                    kitap_verisi["publication_year"],
                    kitap_verisi["genre"],
                    kitap_verisi["is_borrowed"],
                    kitap_verisi["borrowed_by"]
                )
            elif tur == "magazine":
                kitap = Magazine(
                    kitap_verisi["title"],
                    kitap_verisi["author"],
                    kitap_verisi["publication_year"],
                    kitap_verisi["issue"],
                    kitap_verisi["is_borrowed"],
                    kitap_verisi["borrowed_by"]
                )
            else:
                kitap = Book(
                    kitap_verisi["title"],
                    kitap_verisi["author"],
                    kitap_verisi["publication_year"],
                    kitap_verisi["is_borrowed"],
                    kitap_verisi["borrowed_by"]
                )
            self.books.append(kitap)

        # 2) Kullanıcıları oluştur
        self.users = []
        for kullanici_verisi in data["users"]:
            isim = kullanici_verisi["name"]
            sifre = kullanici_verisi["password"]
            kullanici = User(isim, sifre)
            self.users.append(kullanici)

        # 3) İlişkileri geri kur (borrowed_books)
        for i, kullanici_verisi in enumerate(data["users"]):
            baslik_listesi = kullanici_verisi["borrowed_books"]
            kullanici = self.users[i]
            for baslik in baslik_listesi:
                for kitap in self.books:
                    if kitap.title == baslik:
                        kullanici.borrowed_books.append(kitap)
                        break