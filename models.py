# models.py
# Book, Novel, Magazine ve User sınıfları burada yazılacak.

# ---------------------------------------------------------
# class Book
#   __init__(title, author, publication_year)
#       # is_borrowed = False, borrowed_by = None
#   show_info()
#       # TODO: bilgiyi ve durumu yazdır
#   borrow(user)
#       # TODO: zaten alınmışsa uyar, değilse durumu güncelle
#   return_book()
#       # TODO: durumu sıfırla
#   to_dict()
#       # TODO: sözlük döndür ("type" alanı dahil)

class Book():
    def __init__(self,title,author,publication_year,is_borrowed=False,borrowed_by=None):
        self.title=title
        self.author=author
        self.publication_year=publication_year
        self.is_borrowed=is_borrowed
        self.borrowed_by=borrowed_by
    def show_info(self):
        durum = f"Ödünç alındı ({self.borrowed_by})" if self.is_borrowed else "Rafta mevcut"
        print(f"\"{self.title}\" - {self.author} ({self.publication_year}) | {durum}")
    def borrow(self, user):#burada user bilgisini alarak yapmayı tercih ettik.
                           #çünkü borrewed by bilgisi user ile alakalı bir bilgi
        if self.is_borrowed == False:
            self.is_borrowed = True
            self.borrowed_by = user.name
            return True
        else:
            print("Bu kitap zaten alinmiş")
            return False
    def return_book(self):
        self.is_borrowed=False
        self.borrowed_by=None
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
        }

# ---------------------------------------------------------
# class Novel(Book)
#   __init__(title, author, publication_year, genre)
#       # TODO: super() çağır, genre ekle
#   to_dict()
#       # TODO: ana sözlüğe genre ekle
# ---------------------------------------------------------
class Novel(Book):
    def __init__(self, title, author, publication_year, genre, is_borrowed=False, borrowed_by=None):
        super().__init__(title, author, publication_year,is_borrowed, borrowed_by)
        self.genre=genre
    def to_dict(self):
        data = super().to_dict()
        data["genre"] = self.genre
        data["type"] = "novel"
        return data
# class Magazine(Book)
#   __init__(title, author, publication_year, issue)
#       # TODO: super() çağır, issue ekle
#   to_dict()
#       # TODO: ana sözlüğe issue ekle
# ---------------------------------------------------------
class Magazine(Book):
    def __init__(self, title, author, publication_year, issue, is_borrowed=False, borrowed_by=None):
        super().__init__(title, author, publication_year, is_borrowed, borrowed_by)
        self.issue=issue
    def to_dict(self):
        data = super().to_dict()
        data["issue"] = self.issue
        data["type"] = "magazine"
        return data
# class User
#   __init__(name, password)
#       # borrowed_books = []
#   borrow_book(book)
#       # TODO
#   return_book(book)
#       # TODO
#   list_borrowed_books()
#       # TODO
#   to_dict()
#       # TODO: kitapları başlıkla sakla
# ---------------------------------------------------------
class User():
    def __init__(self,name,password,borrowed_books=None):#eğer borrowed_books'a default liste verseydim şu senaryodu sıkıntı yaşardım.
                                                         #.2 farklı kullanıcı oluşturdum ve ikisindede sadece name ve password parametrelerini verdim
                                                         #oluşturulan iki nesne default listeyi ortak kullanıyor olurdu!!
                                                         #Bu yüzden default liste oluşturmayı parametre kısmında değil aşşağıda hallediyorum
        self.name=name
        self.password=password
        #self.borrowed_books = borrowed_books if borrowed_books is not None else []  ternary if-else
        if borrowed_books is not None:
            self.borrowed_books = borrowed_books
        else:
            self.borrowed_books = []
    def borrow_book(self, book):
        if book.borrow(self):
            self.borrowed_books.append(book)
    def return_book(self, book):
        try:
            self.borrowed_books.remove(book)
            book.return_book()
        except ValueError:
            print(f"{self.name} bu kitabi zaten almamis.")
    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} hiçbir kitap ödünç almamis.")
        else:
            print(f"{self.name} adli kullanicinin ödünç aldigi kitaplar:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": [book.title for book in self.borrowed_books]
                            # [book.title for book in self.borrowed_books]
                            # ─────┬───── ───┬─── ──────────┬──────────
                            #      │         │              │
                            # ne koyulacak  her eleman    hangi liste
                            # (sonuç)       için          üzerinde geziliyor
        }