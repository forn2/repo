from abc import ABC, abstractmethod


class PhysicalObject(ABC):
    """
    Абстрактный класс для материальных объектов.
    """

    def __init__(self, weight: float, material: str):
        """
        Инициализация атрибутов материального объекта.

        :param weight: Вес объекта в килограммах (должен быть положительным числом).
        :param material: Материал, из которого изготовлен объект.

        >>> obj = PhysicalObject(10.5, "дерево")
        >>> obj.weight
        10.5
        >>> obj.material
        'дерево'
        """
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        self.weight = weight
        self.material = material

    @abstractmethod
    def move(self, distance: float) -> str:
        """
        Перемещение объекта на указанное расстояние.

        :param distance: Расстояние в метрах (должно быть положительным числом).
        :return: Строка с описанием перемещения.

        >>> obj.move(5.0)
        'Объект перемещен на 5.0 метров.'
        """
        ...

    @abstractmethod
    def break_object(self) -> bool:
        """
        Попытка сломать объект.

        :return: True, если объект сломан, False в противном случае.

        >>> obj.break_object()
        False
        """
        ...


class DigitalObject(ABC):
    """
    Абстрактный класс для цифровых объектов.
    """

    def __init__(self, size: int, format_: str):
        """
        Инициализация атрибутов цифрового объекта.

        :param size: Размер файла в байтах (должен быть положительным числом).
        :param format_: Формат файла.

        >>> obj = DigitalObject(1024, "jpg")
        >>> obj.size
        1024
        >>> obj.format_
        'jpg'
        """
        if size <= 0:
            raise ValueError("Размер должен быть положительным числом.")
        self.size = size
        self.format_ = format_

    @abstractmethod
    def copy(self, destination: str) -> str:
        """
        Копирование цифрового объекта в указанное место.

        :param destination: Путь к месту назначения.
        :return: Строка с описанием результата копирования.

        >>> obj.copy("/path/to/destination")
        'Файл скопирован в /path/to/destination.'
        """
        ...

    @abstractmethod
    def delete(self) -> bool:
        """
        Удаление цифрового объекта.

        :return: True, если объект удален, False в противном случае.

        >>> obj.delete()
        True
        """
        ...


class AbstractConcept(ABC):
    """
    Абстрактный класс для нематериальных концепций.
    """

    def __init__(self, name: str, complexity: int):
        """
        Инициализация атрибутов абстрактной концепции.

        :param name: Название концепции.
        :param complexity: Сложность понимания концепции (от 1 до 10).

        >>> concept = AbstractConcept("свобода", 7)
        >>> concept.name
        'свобода'
        >>> concept.complexity
        7
        """
        if not (1 <= complexity <= 10):
            raise ValueError("Сложность должна быть в диапазоне от 1 до 10.")
        self.name = name
        self.complexity = complexity

    @abstractmethod
    def explain(self, audience: str) -> str:
        """
        Объяснение концепции для определенной аудитории.

        :param audience: Целевая аудитория (например, "дети", "ученые").
        :return: Строка с объяснением.

        >>> concept.explain("дети")
        'Свобода - это когда ты можешь делать то, что хочешь, но помнишь про правила.'
        """
        ...

    @abstractmethod
    def debate(self, opponent: str) -> str:
        """
        Дискуссия по концепции с оппонентом.

        :param opponent: Имя оппонента.
        :return: Строка с результатом дискуссии.

        >>> concept.debate("Иван")
        'Дискуссия с Иваном завершилась мирным соглашением.'
        """
        ...


if __name__ == "__main__":
    # Проверка работоспособности экземпляров класса с помощью doctest
    import doctest
    doctest.testmod()