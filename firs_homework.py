import re


class ProductCard:
    """Класс для управления карточками товаров."""

    STATUSES = {
        "ожидание": "Ожидание приема",
        "учтено": "Состоит/принято к учету",
        "списано": "Списано",
    }

    def __init__(self) -> None:
        """Инициализация системы управления карточками."""

        self._cards = {}
        self._next_number = 1

    def _get_name(self, card_number: int) -> str:
        """Геттер для наименования.

        Args:
            card_number: Номер карточки.

        Returns:
            Наименование товара.
        """

        card = self.get_card(card_number)

        return card["name"]

    def _set_name(self, card_number: int, value: str) -> None:
        """Сеттер для наименования.

        Args:
            card_number: Номер карточки.
            value: Новое наименование.
        """

        if not value or len(value.strip()) < 2:
            raise ValueError("Наименование должно содержать не менее двух символов")
        self._cards[card_number]["name"] = value

    def _get_quantity(self, card_number: int) -> int:
        """Геттер для количества товара.

        Args:
            card_number: Номер карточки.

        Returns:
            Количество товара.
        """

        card = self.get_card(card_number)

        return card["quantity"]

    def _set_quantity(self, card_number: int, value: int) -> None:
        """Сеттер для количества.

        Args:
            card_number: Номер карточки.
            value: Новое количество.
        """

        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self._cards[card_number]["quantity"] = value

    def _get_status(self, card_number: int) -> str:
        """Геттер для статуса.

        Args:
            card_number: Номер карточки.

        Returns:
            Статус карточки.
        """

        card = self.get_card(card_number)

        return card["status"]

    def _set_status(self, card_number: int, value: str) -> None:
        """Сеттер для статуса.

        Args:
            card_number: Номер карточки.
            value: Новый статус.
        """

        status_lower = value.lower()
        if status_lower not in self.STATUSES:
            raise ValueError("Некорректное состояние")
        self._cards[card_number]["status"] = status_lower

    def _get_supplier(self, card_number: int) -> str:
        """Геттер для поставщика.

        Args:
            card_number: Номер карточки.

        Returns:
            Наименование поставщика.
        """

        card = self.get_card(card_number)

        return card["supplier"]

    def _set_supplier(self, card_number: int, value: str) -> None:
        """Сеттер для поставщика.

        Args:
            card_number: Номер карточки.
            value: Новое наименование поставщика.
        """

        if not value or len(value.strip()) < 2:
            raise ValueError("Поставщик должен быть указан")
        self._cards[card_number]["supplier"] = value

    def _get_cost(self, card_number: int) -> float:
        """Геттер для стоимости.

        Args:
            card_number: Номер карточки.

        Returns:
            Стоимость товара.
        """

        card = self.get_card(card_number)

        return card["cost"]

    def _set_cost(self, card_number: int, value: float) -> None:
        """Сеттер для стоимости.

        Args:
            card_number: Номер карточки.
            value: Новая стоимость.
        """

        if value < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        self._cards[card_number]["cost"] = value

    def _get_arrival_date(self, card_number: int) -> str:
        """Геттер для даты поступления.

        Args:
            card_number: Номер карточки.

        Returns:
            Дата поступления в формате ДД.ММ.ГГГГ.
        """

        card = self.get_card(card_number)

        return card["arrival_date"]

    def _set_arrival_date(self, card_number: int, value: str) -> None:
        """Сеттер для даты поступления.

        Args:
            card_number: Номер карточки.
            value: Новая дата в формате ДД.ММ.ГГГГ.
        """

        if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", value):
            raise ValueError("Дата поступления должна быть в формате ДД.ММ.ГГГГ")
        self._cards[card_number]["arrival_date"] = value

    def _get_article(self, card_number: int) -> str:
        """Геттер для артикула товара.

        Args:
            card_number: Номер карточки.

        Returns:
            Артикул товара.
        """

        card = self.get_card(card_number)

        return card["article"]

    def _set_article(self, card_number: int, value: str) -> None:
        """Сеттер для артикула товара.

        Args:
            card_number: Номер карточки.
            value: Новый артикул.
        """

        if not value or not value.strip():
            raise ValueError("Артикул должен быть указан")
        self._cards[card_number]["article"] = value.strip()

    def create_card(
        self,
        name: str,
        quantity: int,
        status: str,
        supplier: str,
        manufacturer: str,
        cost: float,
        location: str,
        article: str,
        responsible: str,
        arrival_date: str,
        notes: str = "",
    ) -> int:
        """Создает новую карточку товара.

        Args:
            name: Наименование товара (минимум 2 символа).
            quantity: Количество товара (неотрицательное).
            status: Статус товара (ожидание/учтено/списано).
            supplier: Поставщик (минимум 2 символа).
            manufacturer: Производитель.
            cost: Стоимость товара (неотрицательная).
            location: Местоположение товара.
            article: Артикул товара (обязательный).
            responsible: Ответственное лицо.
            arrival_date: Дата поступления в формате ДД.ММ.ГГГГ.
            notes: Примечания (опционально).

        Returns:
            Номер созданной карточки.
        """

        temp_number = self._next_number
        self._cards[temp_number] = {
            "number": temp_number,
            "name": "",
            "quantity": 0,
            "status": "ожидание",
            "supplier": "",
            "manufacturer": manufacturer,
            "cost": 0.0,
            "location": location,
            "arrival_date": "",
            "article": "",
            "responsible": responsible,
            "notes": notes,
        }

        try:
            self._set_name(temp_number, name)
            self._set_quantity(temp_number, quantity)
            self._set_status(temp_number, status)
            self._set_supplier(temp_number, supplier)
            self._set_cost(temp_number, cost)
            self._set_article(temp_number, article)
            self._set_arrival_date(temp_number, arrival_date)

        except ValueError as e:
            del self._cards[temp_number]

            raise ValueError(f"\nОшибка валидации данных: {e}")

        card_number = self._next_number
        self._next_number += 1

        return card_number

    def get_card(self, card_number: int) -> dict:
        """Получает карточку по номеру.

        Args:
            card_number: Номер карточки.

        Returns:
            Словарь с данными карточки.
        """

        if card_number not in self._cards:
            raise ValueError(f"\nКарточка с номером {card_number} не найдена")

        return self._cards[card_number]

    def write_off_card(self, card_number: int) -> bool:
        """Списывает карточку с учёта (только если статус 'учтено').

        Args:
            card_number: Номер карточки.

        Returns:
            True при успешном списании.
        """

        card = self.get_card(card_number)
        if card["status"] != "учтено":
            raise ValueError("\nСписание возможно только для карточек в состоянии: Состоит/принято к учету")

        card["status"] = "списано"
        card["quantity"] = 0
        return True

    def update_card(self, card_number: int, **kwargs) -> None:
        """Изменяет данные карточки с валидацией через сеттеры.

        Args:
            card_number: Номер карточки.
            **kwargs: Пары поле = значение для обновления.
        """

        card = self.get_card(card_number)
        old_card = card.copy()

        try:
            field_setters = {
                "name": self._set_name,
                "quantity": self._set_quantity,
                "status": self._set_status,
                "supplier": self._set_supplier,
                "cost": self._set_cost,
                "arrival_date": self._set_arrival_date,
                "article": self._set_article
            }

            for field, value in kwargs.items():
                if field in field_setters:
                    field_setters[field](card_number, value)
                elif field in card and field not in ["number"]:
                    card[field] = value

        except Exception as e:
            self._cards[card_number] = old_card

            raise ValueError(f"\nОшибка изменения: {e}")

    def display_card(self, card: dict) -> None:
        """Выводит данные карточки в удобочитаемом формате.

        Args:
            card: Словарь с данными карточки.
        """

        status = self.STATUSES.get(card["status"], card["status"])
        print(f"\nНомер: {card['number']} | Артикул: {card['article']}")
        print(f"Наименование: {card['name']}")
        print(f"Количество: {card['quantity']}")
        print(f"Состояние: {status}")
        print(f"Стоимость: {card['cost']:.2f} руб.")
        print(f"Поставщик: {card['supplier']}")
        print(f"Производитель: {card['manufacturer']}")
        print(f"Местоположение: {card['location']}")
        print(f"Дата поступления: {card['arrival_date']}")
        print(f"Ответственный: {card['responsible']}")
        print(f"Примечания: {card['notes']}")


def console() -> None:
    """Запускает консольный интерфейс для управления карточками товаров."""

    inventory = ProductCard()

    while True:
        print("СИСТЕМА УПРАВЛЕНИЯ КАРТОЧКАМИ ТОВАРОВ")
        print("1. Создать новую карточку")
        print("2. Просмотреть карточку по номеру")
        print("3. Изменить данные карточки")
        print("4. Списать карточку с учёта")
        print("5. Показать все карточки")
        print("0. Выход")

        try:
            choice = int(input("Выберите номер действия: ").strip())
        except ValueError:
            print("Ошибка: введите число от 0 до 5")

            input("\nНажмите Enter для продолжения.")
            continue

        if choice == 0:
            print("\nВыход из программы.")

            break

        elif choice == 1:
            try:
                name = input("Наименование товара: ").strip()
                quantity = int(input("Количество: "))
                status = input("Состояние: ").strip()
                supplier = input("Поставщик: ").strip()
                manufacturer = input("Производитель: ").strip()
                cost = float(input("Стоимость: "))
                location = input("Местоположение: ").strip()
                article = input("Артикул: ").strip()
                responsible = input("Ответственный: ").strip()
                arrival_date = input("Дата поступления (ДД.ММ.ГГГГ): ").strip()
                notes = input("Примечания (необязательно): ").strip()

                card_number = inventory.create_card(
                    name=name,
                    quantity=quantity,
                    status=status,
                    supplier=supplier,
                    manufacturer=manufacturer,
                    cost=cost,
                    location=location,
                    article=article,
                    responsible=responsible,
                    arrival_date=arrival_date,
                    notes=notes,
                )
                print(f"\nКарточка создана. Номер: {card_number}")
                inventory.display_card(inventory.get_card(card_number))

            except ValueError as e:
                print(f"\nОшибка: {e}")
            except Exception as e:
                print(f"\nНеожиданная ошибка: {e}")

        elif choice == 2:
            try:
                card_number = int(input("Введите номер карточки: ").strip())
                card = inventory.get_card(card_number)

                print("\nДанные карты:")
                inventory.display_card(card)
            except ValueError as e:
                print(f"\nОшибка: {e}")

        elif choice == 3:
            try:
                card_number = int(
                    input("Введите номер карточки для изменения: ").strip()
                )

                print("\nКакое поле изменить?")
                print("1. Наименование")
                print("2. Количество")
                print("3. Состояние")
                print("4. Стоимость")
                print("5. Местоположение")
                print("6. Примечания")

                field_choice = input("Выберите поле (1-6): ").strip()
                field_map = {
                    "1": "name",
                    "2": "quantity",
                    "3": "status",
                    "4": "cost",
                    "5": "location",
                    "6": "notes",
                }

                if field_choice not in field_map:
                    print("Некорректный выбор")
                else:
                    field = field_map[field_choice]
                    new_value = input(f"Новое значение для '{field}': ").strip()

                    if field == "quantity":
                        new_value = int(new_value)
                    elif field == "cost":
                        new_value = float(new_value)

                    inventory.update_card(card_number, **{field: new_value})

                    print("\nДанные успешно обновлены!")
                    inventory.display_card(inventory.get_card(card_number))

            except ValueError as e:
                print(f"\nОшибка: {e}")
            except Exception as e:
                print(f"\nОшибка: {e}")

        elif choice == 4:
            try:
                card_number = int(
                    input("Введите номер карточки для списания: ").strip()
                )
                card = inventory.get_card(card_number)

                if card["status"] != "учтено":
                    print("Ошибка: Списание разрешено только для карточек в состоянии учтено.")
                else:
                    inventory.write_off_card(card_number)

                    print("Карточка успешно списана!")
                    inventory.display_card(inventory.get_card(card_number))

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 5:
            cards = inventory.list_cards()
            if not cards:
                print("\nНет карточек в системе")
            else:
                print(f"\nВСЕ КАРТОЧКИ ({len(cards)})")
                for card in cards:
                    status = inventory.STATUSES.get(card["status"], card["status"])
                    print(
                        f"№{card['number']}: {card['name']} | "
                        f"{card['quantity']} | "
                        f"{status} | "
                        f"{card['article']} | "
                        f"{card['supplier']} | "
                        f"{card['cost']} | "
                        f"{card['location']} | "
                        f"{card['arrival_date']} | "
                        f"{card['responsible']}"
                    )

        else:
            print("\nНекорректный выбор. Выберите число от 0 до 5.")

        input("\nНажмите Enter для продолжения.")


if __name__ == "__main__":
    console()
