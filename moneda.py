import requests

url = "https://api.exchangerate-api.com/v4/latest/EUR"

respuesta = requests.get(url)
datos = respuesta.json()

monedas = datos["rates"]

moneda_mas_barata = None
valor_mas_bajo = float("inf")

for moneda, valor in monedas.items():
    if valor < valor_mas_bajo:
        valor_mas_bajo = valor
        moneda_mas_barata = moneda

print(f"Moneda más económica: {moneda_mas_barata}")
print(f"Valor: {valor_mas_bajo}")