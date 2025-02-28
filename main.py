class Book:
    def __init__(self, name: str, author: str):
        """
        Базовый класс для всех типов книг.

        :param name: Название книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Свойство для получения названия книги (только для чтения)."""
        return self._name

    @property
    def author(self) -> str:
        """Свойство для получения автора книги (только для чтения)."""
        return self._author

    def __str__(self):
        """
        Возвращает строковое представление книги.
        Формат: "{Название} - {Автор}"
        """
        return f"{self.name} - {self.author}"

    def __repr__(self):
        """
        Возвращает формальное строковое представление объекта.
        Формат: "Book(name={название}, author={автор})"
        """
        return f"Book(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        Класс для бумажных книг.

        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц
        """
        super().__init__(name, author)
        self._pages = None  # Инициализация атрибута
        self.pages = pages  # Вызов setter для проверки значения

    @property
    def pages(self) -> int:
        """Свойство для получения количества страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """
        Свойство для установки количества страниц с проверкой типа и значения.

        :param value: Новое значение количества страниц
        :raises TypeError: Если переданное значение не является целым числом
        :raises ValueError: Если переданное значение меньше или равно нулю
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        """
        Переопределение метода __str__ для бумажной книги.
        Формат: "{Название} - {Автор} (Бумажная книга, {Количество страниц} страниц)"
        """
        return f"{super().__str__()} (Бумажная книга, {self.pages} страниц)"

    def __repr__(self):
        """
        Переопределение метода __repr__ для бумажной книги.
        Формат: "PaperBook(name={название}, author={автор}, pages={количество страниц})"
        """
        return f"PaperBook(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Класс для аудиокниг.

        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность в часах
        """
        super().__init__(name, author)
        self._duration = None  # Инициализация атрибута
        self.duration = duration  # Вызов setter для проверки значения

    @property
    def duration(self) -> float:
        """Свойство для получения продолжительности."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """
        Свойство для установки продолжительности с проверкой типа и значения.

        :param value: Новое значение продолжительности
        :raises TypeError: Если переданное значение не является числом с плавающей запятой
        :raises ValueError: Если переданное значение меньше или равно нулю
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        """
        Переопределение метода __str__ для аудиокниги.
        Формат: "{Название} - {Автор} (Аудиокнига, {Продолжительность} часов)"
        """
        return f"{super().__str__()} (Аудиокнига, {self.duration} часов)"

    def __repr__(self):
        """
        Переопределение метода __repr__ для аудиокниги.
        Формат: "AudioBook(name={название}, author={автор}, duration={продолжительность})"
        """
        return f"AudioBook(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Пример использования
if __name__ == "__main__":
    # Создание экземпляров
    paper_book = PaperBook(name="Война и мир", author="Лев Толстой", pages=1225)
    audio_book = AudioBook(name="1984", author="Джордж Оруэлл", duration=10.5)

    # Печать строкового представления
    print(paper_book)  # Вывод: Война и мир - Лев Толстой (Бумажная книга, 1225 страниц)
    print(audio_book)  # Вывод: 1984 - Джордж Оруэлл (Аудиокнига, 10.5 часов)

    # Печать формального представления
    print(repr(paper_book))  # Вывод: PaperBook(name='Война и мир', author='Лев Толстой', pages=1225)
    print(repr(audio_book))  # Вывод: AudioBook(name='1984', author='Джордж Оруэлл', duration=10.5)

    # Попытка изменить защищенные атрибуты
    try:
        paper_book.name = "Новое название"
    except AttributeError as e:
        print(e)  # Вывод: can't set attribute

    # Попытка установить недопустимые значения
    try:
        paper_book.pages = -100
    except ValueError as e:
        print(e)  # Вывод: Количество страниц должно быть положительным числом

    try:
        audio_book.duration = "не число"
    except TypeError as e:
        print(e)  # Вывод: Продолжительность должна быть числом