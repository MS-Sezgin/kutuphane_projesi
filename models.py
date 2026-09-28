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
# ---------------------------------------------------------
# class Novel(Book)
#   __init__(title, author, publication_year, genre)
#       # TODO: super() çağır, genre ekle
#   to_dict()
#       # TODO: ana sözlüğe genre ekle
# ---------------------------------------------------------
# class Magazine(Book)
#   __init__(title, author, publication_year, issue)
#       # TODO: super() çağır, issue ekle
#   to_dict()
#       # TODO: ana sözlüğe issue ekle
# ---------------------------------------------------------
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
