class Book:
    book_material = 'бумага'
    text_presence = True

    def __init__(self, book_title, author, page_count, isbn=None, is_reserved=False):
        self.book_title = book_title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = is_reserved

    def print_book_info(self):
        unreserved_txt = (
            f'Название: {self.book_title}, Автор: {self.author}, '
            f'страниц: {self.page_count}, материал: {self.book_material}'
        )
        reserved_txt = f'{unreserved_txt}, зарезервирована '

        return reserved_txt if self.is_reserved else unreserved_txt


book_1 = Book(book_title='Идиот', author='Достоевский', page_count=500)
book_2 = Book(book_title='Душа человека', author='Фромм', page_count=200, isbn=1234556)
book_3 = Book(book_title='Как стать счастливым', author='Элис', page_count=300, isbn=234)
book_4 = Book(book_title='Ораторское искусство', author='Карнеги', page_count=200)
book_5 = Book(book_title='Критика чистого разума', author='Кант', page_count=400, is_reserved=True)

book_1.is_reserved = True
print(book_1.print_book_info())
print(book_2.print_book_info())
print(book_3.print_book_info())
print(book_4.print_book_info())
print(book_5.print_book_info())


class SchoolBooks(Book):
    def __init__(self, book_title, author, page_count, subject, grade, has_assignment=False):
        super().__init__(book_title, author, page_count)
        self.subject = subject
        self.grade = grade
        self.has_assignment = has_assignment

    def print_school_book_info(self):
        unreserved_txt = (
            f'Название: {self.book_title}, Автор: {self.author}, '
            f'страниц: {self.page_count}, предмет: {self.subject}, класс: {self.grade}'
        )
        reserved_txt = f'{unreserved_txt}, зарезервирована '

        return reserved_txt if self.is_reserved else unreserved_txt


school_book_1 = SchoolBooks('Алгебра', 'Иванов', 200, 'Математика', 9)
school_book_2 = SchoolBooks('Физика', 'Петров', 250, 'Физика', 7)
school_book_1.is_reserved = True
print(school_book_1.print_school_book_info())
print(school_book_2.print_school_book_info())
