from datetime import datetime

import requests

from .model import ExchangeRate


class PrivatBankAPIError(Exception):
    """
    Base privat bank client error.
    """
    pass


class PrivatBankAPI:
    """
    Client to interact with privat bank public api.
    https://api.privatbank.ua/
    """
    def __init__(self, api_url: str = 'https://api.privatbank.ua/p24api'):
        self.api_url = api_url

    def exchange_rates(self, date: str = None) -> list[ExchangeRate]:
        """
        Get information about the cash exchange rates of privat bank and the NBU.
        """
        if date is None:
            date = datetime.today().strftime('%d.%m.%Y')

        response = requests.get(f'{self.api_url}/exchange_rates?date={date}')
        if response.status_code != 200:
            raise PrivatBankAPIError
        
        response_data = response.json()
        exchange_rates_data = []
        for exchange_rate in response_data.get('exchangeRate', []):
            exchange_rate.pop('baseCurrency')
            exchange_rates_data.append(
                ExchangeRate(
                    currency=exchange_rate.get('currency', ''),
                    sale_rate_nb=exchange_rate.get('saleRateNB', 0.0),
                    purchase_rate_nb=exchange_rate.get('purchaseRateNB', 0.0),
                    sale_rate=exchange_rate.get('saleRate', 0.0),
                    purchase_rate=exchange_rate.get('purchaseRate', 0.0),
                )
            )

        return exchange_rates_data
