'''uah = float(input("Введіть число:"))
doll = 41.65

sum = uah / doll

print("сума",sum)'''




'''import requests

class CurrencyExchange:

    def __init__(self, base_currency="USD"):
        self.base_currency = base_currency
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data["rates"]
            else:
                print("Помилка при отриманні даних.")
                return None
        except Exception as e:
            print(f"Сталася помилка: {e}")
            return None

    def get_rate(self, target_currency):
        """Повертає курс обміну для заданої валюти."""
        if self.exchange_rate:
            return self.exchange_rate.get(target_currency, None)
        else:
            return None


class CurrencyConverter:
    """Клас для конвертації валют."""

    def __init__(self, currency_exchange):
        self.currency_exchange = currency_exchange

    def convert(self, amount, from_currency, to_currency):
        """Конвертує суму з однієї валюти в іншу."""
        rate_from = self.currency_exchange.get_rate(from_currency)
        rate_to = self.currency_exchange.get_rate(to_currency)

        if rate_from and rate_to:
            amount_in_base_currency = amount / rate_from
            converted_amount = amount_in_base_currency * rate_to
            return converted_amount
        else:
            print("Не вдалося отримати курси валют.")
            return None

currency_exchange = CurrencyExchange(base_currency="USD")
currency_converter = CurrencyConverter(currency_exchange)

amount_uah = float(input("Введіть суму в гривнях: "))
converted_amount = currency_converter.convert(amount_uah, "UAH", "USD")

if converted_amount is not None:
    print(f"{amount_uah} грн = {converted_amount:.2f} USD")'''