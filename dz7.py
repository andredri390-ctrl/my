import requests

def currency_converter():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
    response = requests.get(url)
    data = response.json()
    usd_rate = data[0]['rate']
    print(f"--- Актуальний курс: {usd_rate} UAH за 1 USD ---")
    uah_amount = float(input("Введіть суму в гривнях (UAH): "))
    usd_result = uah_amount / usd_rate
    print(f"Результат: ${usd_result:.2f}")
if __name__ == "__main__":
    currency_converter()