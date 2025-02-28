import doctest


class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        >>> glass.capacity_volume
        500
        >>> glass.occupied_volume
        0
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError("Количество жидкости не может превышать объем стакана")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Проверяет, является ли стакан пустым

        :return: True, если стакан пустой, иначе False

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        True
        >>> glass.add_water_to_glass(100)
        >>> glass.is_empty_glass()
        False
        """
        return self.occupied_volume == 0

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.

        :param water: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане

        Примеры:
        >>> glass = Glass(500, 200)
        >>> glass.add_water_to_glass(200)
        >>> glass.occupied_volume
        400
        >>> glass.add_water_to_glass(200)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: Недостаточно места в стакане для добавления такой水量.
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")
        free_space = self.capacity_volume - self.occupied_volume
        if water > free_space:
            raise ValueError("Недостаточно места в стакане для добавления такой水量.")
        self.occupied_volume += water

    def remove_water_from_glass(self, estimate_water: float) -> float:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане
        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 300)
        >>> glass.remove_water_from_glass(200)
        200
        >>> glass.occupied_volume
        100
        >>> glass.remove_water_from_glass(200)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: Недостаточно воды в стакане для извлечения такого объема.
        """
        if not isinstance(estimate_water, (int, float)):
            raise TypeError("Извлекаемая жидкость должна быть типа int или float")
        if estimate_water < 0:
            raise ValueError("Извлекаемая жидкость должна быть положительным числом")
        if estimate_water > self.occupied_volume:
            raise ValueError("Недостаточно воды в стакане для извлечения такого объема.")
        removed_water = estimate_water
        self.occupied_volume -= removed_water
        return removed_water


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации
