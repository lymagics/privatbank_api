from dataclasses import dataclass


@dataclass
class ExchangeRate:
    """
    Information on cash exchange rates.

    :param currency: Валюта угоди
    :sale_rate_nb: Курс продажу НБУ
    :purchase_rate_nb: Курс купівлі НБУ
    :sale_rate: Курс продажу ПриватБанку
    :purchase_rate: Курс купівлі ПриватБанку
    """
    currency: str
    sale_rate_nb: float
    purchase_rate_nb: float
    sale_rate: float
    purchase_rate: float
