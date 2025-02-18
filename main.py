from abc import ABC, abstractmethod


class SocialNetwork(ABC):
    """
    Абстрактный базовый класс для социальных сетей.
    """

    def __init__(self, name: str, users_count: int, country: str):
        """
        Инициализация атрибутов социальной сети.

        :param name: Название социальной сети.
        :param users_count: Количество пользователей (в миллионах).
        :param country: Страна происхождения.
        """
        self._name = name  # Инкапсулируем название, так как оно не должно меняться после создания объекта
        self.users_count = users_count  # Открытое свойство, количество пользователей может меняться
        self.country = country  # Открытое свойство, страна также может меняться

    def __str__(self) -> str:
        """
        Возвращает читаемое представление объекта.

        :return: Строка с информацией о социальной сети.
        """
        return f"{self._name} — социальная сеть из {self.country} с {self.users_count} млн пользователей."

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Формальное представление объекта.
        """
        return f"SocialNetwork(name={self._name}, users_count={self.users_count}, country={self.country})"

    @abstractmethod
    def post_message(self, message: str) -> str:
        """
        Метод для публикации сообщения в социальной сети.

        :param message: Сообщение для публикации.
        :return: Результат публикации.
        """
        ...


class VK(SocialNetwork):
    """
    Дочерний класс для социальной сети VK.
    """

    def __init__(self, users_count: int, country: str = "Russia"):
        """
        Инициализация атрибутов VK.

        :param users_count: Количество пользователей (в миллионах).
        :param country: Страна происхождения (по умолчанию Россия).
        """
        super().__init__(name="VK", users_count=users_count, country=country)
        self._features = ["Stories", "Marketplace", "Groups"]  # Приватный список возможностей VK

    def __str__(self) -> str:
        """
        Переопределение метода __str__ для добавления информации о возможностях VK.

        :return: Расширенное читаемое представление объекта.
        """
        features_str = ", ".join(self._features)
        return f"{super().__str__()} Основные возможности: {features_str}."

    def __repr__(self) -> str:
        """
        Переопределение метода __repr__ для более подробного формального представления объекта.

        :return: Расширенное формальное представление объекта.
        """
        return f"VK(users_count={self.users_count}, country={self.country}, features={self._features})"

    def post_message(self, message: str) -> str:
        """
        Публикация сообщения в VK. Добавлены специфические для VK особенности.

        :param message: Сообщение для публикации.
        :return: Результат публикации с уведомлением о платформе.
        """
        return f"Сообщение опубликовано в VK: '{message}'."

    def create_group(self, group_name: str) -> str:
        """
        Создание группы в VK.

        :param group_name: Название группы.
        :return: Уведомление о создании группы.
        """
        return f"Группа '{group_name}' успешно создана в VK."


class Facebook(SocialNetwork):
    """
    Дочерний класс для социальной сети Facebook.
    """

    def __init__(self, users_count: int, country: str = "USA"):
        """
        Инициализация атрибутов Facebook.

        :param users_count: Количество пользователей (в миллионах).
        :param country: Страна происхождения (по умолчанию США).
        """
        super().__init__(name="Facebook", users_count=users_count, country=country)
        self._advertising_platform = True  # Приватный флаг для указания наличия рекламной платформы

    def __str__(self) -> str:
        """
        Переопределение метода __str__ для добавления информации о рекламной платформе Facebook.

        :return: Расширенное читаемое представление объекта.
        """
        ad_info = "с рекламной платформой" if self._advertising_platform else "без рекламной платформы"
        return f"{super().__str__()} ({ad_info})."

    def __repr__(self) -> str:
        """
        Переопределение метода __repr__ для более подробного формального представления объекта.

        :return: Расширенное формальное представление объекта.
        """
        return f"Facebook(users_count={self.users_count}, country={self.country}, advertising_platform={self._advertising_platform})"

    def post_message(self, message: str) -> str:
        """
        Публикация сообщения в Facebook. Добавлены специфические для Facebook особенности.

        :param message: Сообщение для публикации.
        :return: Результат публикации с уведомлением о платформе.
        """
        return f"Сообщение опубликовано в Facebook: '{message}'. Доступно для всех друзей."

    def run_advertisement(self, ad_text: str) -> str:
        """
        Запуск рекламы в Facebook.

        :param ad_text: Текст рекламы.
        :return: Уведомление о запуске рекламы.
        """
        if not self._advertising_platform:
            raise ValueError("Рекламная платформа недоступна.")
        return f"Реклама '{ad_text}' успешно запущена в Facebook."


if __name__ == "__main__":
    # Пример использования классов
    vk = VK(users_count=90, country="Russia")
    print(vk)  # Вывод через __str__
    print(repr(vk))  # Вывод через __repr__

    facebook = Facebook(users_count=2900, country="USA")
    print(facebook)  # Вывод через __str__
    print(repr(facebook))  # Вывод через __repr__

    # Пример использования методов
    print(vk.post_message("Привет от VK!"))
    print(vk.create_group("Python Developers"))

    print(facebook.post_message("Привет от Facebook!"))
    print(facebook.run_advertisement("Купите наш новый продукт!"))