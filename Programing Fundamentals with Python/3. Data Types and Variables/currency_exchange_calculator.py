from forex_python.converter import CurrencyRates
from decimal import Decimal
input_money = Decimal(input('Въведете сумата:  '))
input_money_currency_symbol = input('Въведете индекса на входящата валута:  ')
output_money_currency_symbol = input('Въведете индекса на изходящата валута:  ')
c = CurrencyRates()
exchange_rate = float(c.get_rate(input_money_currency_symbol, output_money_currency_symbol))
output_money = Decimal(exchange_rate) * Decimal(input_money)
print(f"Дневният курс {input_money_currency_symbol} -> {output_money_currency_symbol} e: {exchange_rate:.4f}")
print(f"{input_money:.2f} {input_money_currency_symbol} = {output_money:.2f} {output_money_currency_symbol}")

