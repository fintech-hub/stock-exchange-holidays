from datetime import date
from functools import lru_cache
from typing import Dict, Set, List, Tuple, Optional


class StockExchange:
    """Base class for stock exchanges with optimized holiday lookups"""
    
    def __init__(self):
        # Armazena feriados em um dicionário indexado por ano para acesso O(1)
        self._holidays_by_year: Dict[int, List[Tuple[date, str]]] = {}
        # Set de datas para verificação rápida O(1) se uma data é feriado
        self._holiday_dates: Set[date] = set()
        self._initialize_holidays()

    def _add_holiday(self, holiday_date: date, description: str) -> None:
        """Adiciona um feriado aos índices internos"""
        year = holiday_date.year
        if year not in self._holidays_by_year:
            self._holidays_by_year[year] = []
        self._holidays_by_year[year].append((holiday_date, description))
        self._holiday_dates.add(holiday_date)

    @property
    def holidays(self) -> List[Tuple[date, str]]:
        """Retorna todos os feriados ordenados por data"""
        all_holidays = []
        for year_holidays in self._holidays_by_year.values():
            all_holidays.extend(year_holidays)
        return sorted(all_holidays, key=lambda x: x[0])

    @lru_cache(maxsize=128)
    def get_holidays_by_year(self, year: int) -> List[Tuple[date, str]]:
        """Retorna feriados de um ano específico com cache"""
        return sorted(self._holidays_by_year.get(year, []), key=lambda x: x[0])

    def is_holiday(self, check_date: date) -> bool:
        """Verifica se uma data é feriado em O(1)"""
        return check_date in self._holiday_dates


class NYSE(StockExchange):
    """
    New York Stock Exchange (NYSE)
    Source: https://www.nyse.com/markets/hours-calendars

    """
    def _initialize_holidays(self) -> None:
        # 2020
        self._add_holiday(date(2020, 1, 1), 'New year')
        self._add_holiday(date(2020, 1, 20), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2020, 2, 17), "Washington's Birthday")
        self._add_holiday(date(2020, 4, 10), 'Good Friday')
        self._add_holiday(date(2020, 5, 25), 'Memorial Day')
        self._add_holiday(date(2020, 7, 4), 'Independence Day')
        self._add_holiday(date(2020, 9, 7), 'Labor Day')
        self._add_holiday(date(2020, 11, 26), 'Thanksgiving Day')
        self._add_holiday(date(2020, 12, 25), 'Christmas Day')
        self._add_holiday(date(2020, 12, 31), 'Last day of year')

        # 2021
        self._add_holiday(date(2021, 1, 1), 'New year')
        self._add_holiday(date(2021, 1, 18), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2021, 2, 15), "Washington's Birthday")
        self._add_holiday(date(2021, 4, 2), 'Good Friday')
        self._add_holiday(date(2021, 5, 31), 'Memorial Day')
        self._add_holiday(date(2021, 7, 4), 'Independence Day')
        self._add_holiday(date(2021, 9, 6), 'Labor Day')
        self._add_holiday(date(2021, 11, 25), 'Thanksgiving Day')
        self._add_holiday(date(2021, 12, 25), 'Christmas Day')
        self._add_holiday(date(2021, 12, 31), 'Last day of year')

        # 2022
        self._add_holiday(date(2022, 1, 1), 'New year')
        self._add_holiday(date(2022, 1, 17), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2022, 2, 21), "Washington's Birthday")
        self._add_holiday(date(2022, 4, 15), 'Good Friday')
        self._add_holiday(date(2022, 5, 30), 'Memorial Day')
        self._add_holiday(date(2022, 6, 20), 'Juneteenth National Independence Day')
        self._add_holiday(date(2022, 7, 4), 'Independence Day')
        self._add_holiday(date(2022, 9, 5), 'Labor Day')
        self._add_holiday(date(2022, 11, 24), 'Thanksgiving Day')
        self._add_holiday(date(2022, 12, 25), 'Christmas Day')
        self._add_holiday(date(2022, 12, 31), 'Last day of year')

        # 2023
        self._add_holiday(date(2023, 1, 1), 'New year')
        self._add_holiday(date(2023, 1, 16), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2023, 2, 20), "Washington's Birthday")
        self._add_holiday(date(2023, 4, 7), 'Good Friday')
        self._add_holiday(date(2023, 5, 29), 'Memorial Day')
        self._add_holiday(date(2023, 6, 19), 'Juneteenth National Independence Day')
        self._add_holiday(date(2023, 7, 4), 'Independence Day')
        self._add_holiday(date(2023, 9, 4), 'Labor Day')
        self._add_holiday(date(2023, 11, 23), 'Thanksgiving Day')
        self._add_holiday(date(2023, 12, 25), 'Christmas Day')
        self._add_holiday(date(2023, 12, 31), 'Last day of year')

        # 2024
        self._add_holiday(date(2024, 1, 1), 'New year')
        self._add_holiday(date(2024, 1, 15), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2024, 2, 19), "Washington's Birthday")
        self._add_holiday(date(2024, 3, 29), 'Good Friday')
        self._add_holiday(date(2024, 5, 27), 'Memorial Day')
        self._add_holiday(date(2024, 6, 19), 'Juneteenth National Independence Day')
        self._add_holiday(date(2024, 7, 4), 'Independence Day')
        self._add_holiday(date(2024, 9, 2), 'Labor Day')
        self._add_holiday(date(2024, 11, 28), 'Thanksgiving Day')
        self._add_holiday(date(2024, 12, 25), 'Christmas Day')
        self._add_holiday(date(2024, 12, 31), 'Last day of year')

        # 2025
        self._add_holiday(date(2025, 1, 1), 'New year')
        self._add_holiday(date(2025, 1, 20), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2025, 2, 17), "Washington's Birthday")
        self._add_holiday(date(2025, 4, 18), 'Good Friday')
        self._add_holiday(date(2025, 5, 26), 'Memorial Day')
        self._add_holiday(date(2025, 6, 19), 'Juneteenth National Independence Day')
        self._add_holiday(date(2025, 7, 4), 'Independence Day')
        self._add_holiday(date(2025, 9, 1), 'Labor Day')
        self._add_holiday(date(2025, 11, 27), 'Thanksgiving Day')
        self._add_holiday(date(2025, 12, 25), 'Christmas Day')
        self._add_holiday(date(2025, 12, 31), 'Last day of year')


class CME(StockExchange):
    """
    Chicago Mercantile Exchange (CME)
    Source: https://www.cmegroup.com/tools-information/holiday-calendar.html

    """
    def _initialize_holidays(self) -> None:
        # 2020
        self._add_holiday(date(2020, 1, 1), 'New year')
        self._add_holiday(date(2020, 1, 20), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2020, 2, 17), "Washington's Birthday")
        self._add_holiday(date(2020, 4, 10), 'Good Friday')
        self._add_holiday(date(2020, 5, 25), 'Memorial Day')
        self._add_holiday(date(2020, 7, 4), 'Independence Day')
        self._add_holiday(date(2020, 9, 7), 'Labor Day')
        self._add_holiday(date(2020, 11, 26), 'Thanksgiving Day')
        self._add_holiday(date(2020, 12, 25), 'Christmas Day')
        self._add_holiday(date(2020, 12, 31), 'Last day of year')

        # 2021
        self._add_holiday(date(2021, 1, 1), 'New year')
        self._add_holiday(date(2021, 1, 18), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2021, 2, 15), "Washington's Birthday")
        self._add_holiday(date(2021, 4, 2), 'Good Friday')
        self._add_holiday(date(2021, 5, 31), 'Memorial Day')
        self._add_holiday(date(2021, 7, 4), 'Independence Day')
        self._add_holiday(date(2021, 9, 6), 'Labor Day')
        self._add_holiday(date(2021, 11, 25), 'Thanksgiving Day')
        self._add_holiday(date(2021, 12, 25), 'Christmas Day')
        self._add_holiday(date(2021, 12, 31), 'Last day of year')

        # 2022
        self._add_holiday(date(2022, 1, 1), 'New year')
        self._add_holiday(date(2022, 1, 17), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2022, 2, 21), "Washington's Birthday")
        self._add_holiday(date(2022, 4, 15), 'Good Friday')
        self._add_holiday(date(2022, 5, 30), 'Memorial Day')
        self._add_holiday(date(2022, 6, 20), 'Juneteenth National Independence Day')
        self._add_holiday(date(2022, 7, 4), 'Independence Day')
        self._add_holiday(date(2022, 9, 5), 'Labor Day')
        self._add_holiday(date(2022, 11, 24), 'Thanksgiving Day')
        self._add_holiday(date(2022, 12, 25), 'Christmas Day')
        self._add_holiday(date(2022, 12, 31), 'Last day of year')

        # 2023
        self._add_holiday(date(2023, 1, 1), 'New year')
        self._add_holiday(date(2023, 1, 16), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2023, 2, 20), "Washington's Birthday")
        self._add_holiday(date(2023, 4, 7), 'Good Friday')
        self._add_holiday(date(2023, 5, 29), 'Memorial Day')
        self._add_holiday(date(2023, 6, 19), 'Juneteenth National Independence Day')
        self._add_holiday(date(2023, 7, 4), 'Independence Day')
        self._add_holiday(date(2023, 9, 4), 'Labor Day')
        self._add_holiday(date(2023, 11, 23), 'Thanksgiving Day')
        self._add_holiday(date(2023, 12, 25), 'Christmas Day')
        self._add_holiday(date(2023, 12, 31), 'Last day of year')

        # 2024
        self._add_holiday(date(2024, 1, 1), 'New year')
        self._add_holiday(date(2024, 1, 15), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2024, 2, 19), "Washington's Birthday")
        self._add_holiday(date(2024, 3, 29), 'Good Friday')
        self._add_holiday(date(2024, 5, 27), 'Memorial Day')
        self._add_holiday(date(2024, 6, 19), 'Juneteenth National Independence Day')
        self._add_holiday(date(2024, 7, 4), 'Independence Day')
        self._add_holiday(date(2024, 9, 2), 'Labor Day')
        self._add_holiday(date(2024, 11, 28), 'Thanksgiving Day')
        self._add_holiday(date(2024, 12, 25), 'Christmas Day')
        self._add_holiday(date(2024, 12, 31), 'Last day of year')

        # 2025
        self._add_holiday(date(2025, 1, 1), 'New year')
        self._add_holiday(date(2025, 1, 20), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2025, 2, 17), "Washington's Birthday")
        self._add_holiday(date(2025, 4, 18), 'Good Friday')
        self._add_holiday(date(2025, 5, 26), 'Memorial Day')
        self._add_holiday(date(2025, 6, 19), 'Juneteenth National Independence Day')
        self._add_holiday(date(2025, 7, 4), 'Independence Day')
        self._add_holiday(date(2025, 9, 1), 'Labor Day')
        self._add_holiday(date(2025, 11, 27), 'Thanksgiving Day')
        self._add_holiday(date(2025, 12, 25), 'Christmas Day')
        self._add_holiday(date(2025, 12, 31), 'Last day of year')


class B3(StockExchange):
    """
    Sao Paulo Stock exchange (B3) formerly BM&F-BOVESPA
    Source: http://www.b3.com.br

    """
    def _initialize_holidays(self) -> None:
        # 2020
        self._add_holiday(date(2020, 1, 1), 'New year')
        self._add_holiday(date(2020, 2, 24), 'Carnaval Monday')
        self._add_holiday(date(2020, 2, 25), 'Carnaval')
        self._add_holiday(date(2020, 4, 10), 'Good Friday')
        self._add_holiday(date(2020, 4, 21), "Tiradentes' Day")
        self._add_holiday(date(2020, 5, 1), 'Labour Day')
        self._add_holiday(date(2020, 6, 11), 'Corpus Christi')
        self._add_holiday(date(2020, 7, 9), 'Constitutional Revolution of 1932')
        self._add_holiday(date(2020, 9, 7), 'Independence Day')
        self._add_holiday(date(2020, 10, 12), 'Our Lady of Aparecida')
        self._add_holiday(date(2020, 11, 2), "All Souls' Day")
        self._add_holiday(date(2020, 11, 15), 'Republic Day')
        self._add_holiday(date(2020, 12, 25), 'Christmas Day')
        self._add_holiday(date(2020, 12, 31), 'Last day of year')

        # 2021
        self._add_holiday(date(2021, 1, 1), 'New year')
        self._add_holiday(date(2021, 1, 25), 'Anniversary of the city of São Paulo')
        self._add_holiday(date(2021, 2, 15), 'Carnaval Monday')
        self._add_holiday(date(2021, 2, 16), 'Carnaval')
        self._add_holiday(date(2021, 4, 2), 'Good Friday')
        self._add_holiday(date(2021, 4, 21), "Tiradentes' Day")
        self._add_holiday(date(2021, 5, 1), 'Labour Day')
        self._add_holiday(date(2021, 6, 3), 'Corpus Christi')
        self._add_holiday(date(2021, 7, 9), 'Constitutional Revolution of 1932')
        self._add_holiday(date(2021, 9, 7), 'Independence Day')
        self._add_holiday(date(2021, 10, 12), 'Our Lady of Aparecida')
        self._add_holiday(date(2021, 11, 2), "All Souls' Day")
        self._add_holiday(date(2021, 11, 15), 'Republic Day')
        self._add_holiday(date(2021, 12, 25), 'Christmas Day')
        self._add_holiday(date(2021, 12, 31), 'Last day of year')

        # 2022
        self._add_holiday(date(2022, 1, 1), 'New year')
        self._add_holiday(date(2022, 2, 28), 'Carnaval Monday')
        self._add_holiday(date(2022, 3, 1), 'Carnaval')
        self._add_holiday(date(2022, 4, 15), 'Good Friday')
        self._add_holiday(date(2022, 4, 21), "Tiradentes' Day")
        self._add_holiday(date(2022, 5, 1), 'Labour Day')
        self._add_holiday(date(2022, 6, 16), 'Corpus Christi')
        self._add_holiday(date(2022, 9, 7), 'Independence Day')
        self._add_holiday(date(2022, 10, 12), 'Our Lady of Aparecida')
        self._add_holiday(date(2022, 11, 2), "All Souls' Day")
        self._add_holiday(date(2022, 11, 15), 'Republic Day')
        self._add_holiday(date(2022, 12, 25), 'Christmas Day')
        self._add_holiday(date(2022, 12, 31), 'Last day of year')

        # 2023
        self._add_holiday(date(2023, 1, 1), 'New year')
        self._add_holiday(date(2023, 2, 21), 'Carnaval Monday')
        self._add_holiday(date(2023, 2, 22), 'Carnaval')
        self._add_holiday(date(2023, 4, 7), 'Good Friday')
        self._add_holiday(date(2023, 4, 21), "Tiradentes' Day")
        self._add_holiday(date(2023, 5, 1), 'Labour Day')
        self._add_holiday(date(2023, 6, 8), 'Corpus Christi')
        self._add_holiday(date(2023, 9, 7), 'Independence Day')
        self._add_holiday(date(2023, 10, 12), 'Our Lady of Aparecida')
        self._add_holiday(date(2023, 11, 2), "All Souls' Day")
        self._add_holiday(date(2023, 11, 15), 'Republic Day')
        self._add_holiday(date(2023, 12, 25), 'Christmas Day')
        self._add_holiday(date(2023, 12, 31), 'Last day of year')

        # 2024
        self._add_holiday(date(2024, 1, 1), 'New year')
        self._add_holiday(date(2024, 2, 12), 'Carnaval Monday')
        self._add_holiday(date(2024, 2, 13), 'Carnaval')
        self._add_holiday(date(2024, 3, 29), 'Good Friday')
        self._add_holiday(date(2024, 4, 21), "Tiradentes' Day")
        self._add_holiday(date(2024, 5, 1), 'Labour Day')
        self._add_holiday(date(2024, 5, 30), 'Corpus Christi')
        self._add_holiday(date(2024, 9, 7), 'Independence Day')
        self._add_holiday(date(2024, 10, 12), 'Our Lady of Aparecida')
        self._add_holiday(date(2024, 11, 2), "All Souls' Day")
        self._add_holiday(date(2024, 11, 15), 'Republic Day')
        self._add_holiday(date(2024, 12, 25), 'Christmas Day')
        self._add_holiday(date(2024, 12, 31), 'Last day of year')

        # 2025
        self._add_holiday(date(2025, 1, 1), 'New year')
        self._add_holiday(date(2025, 3, 3), 'Carnaval Monday')
        self._add_holiday(date(2025, 3, 4), 'Carnaval')
        self._add_holiday(date(2025, 4, 18), 'Good Friday')
        self._add_holiday(date(2025, 4, 21), "Tiradentes' Day")
        self._add_holiday(date(2025, 5, 1), 'Labour Day')
        self._add_holiday(date(2025, 6, 19), 'Corpus Christi')
        self._add_holiday(date(2025, 9, 7), 'Independence Day')
        self._add_holiday(date(2025, 10, 12), 'Our Lady of Aparecida')
        self._add_holiday(date(2025, 11, 2), "All Souls' Day")
        self._add_holiday(date(2025, 11, 15), 'Republic Day')
        self._add_holiday(date(2025, 12, 25), 'Christmas Day')
        self._add_holiday(date(2025, 12, 31), 'Last day of year')


class Holidays:
    """
    Holidays methods

    """
    def __init__(self, exchange=None):
        self.stock_exchange = exchange

    def get_holidays(self):
        return self.stock_exchange.holidays

    def get_holidays_by_year(self, year):
        return self.stock_exchange.get_holidays_by_year(year)

    def is_date_holiday(self, date):
        return self.stock_exchange.is_holiday(date)
