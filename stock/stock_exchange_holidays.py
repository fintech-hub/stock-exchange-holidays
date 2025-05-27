from datetime import date
from functools import lru_cache
from typing import Dict, Set, List, Tuple


class StockExchange:
    """Base class for stock exchanges with optimized holiday lookups"""

    def __init__(self):
        # Store holidays in a year-indexed dictionary for O(1) access
        self._holidays_by_year: Dict[int, List[Tuple[date, str]]] = {}
        # Set of dates for fast O(1) holiday checking
        self._holiday_dates: Set[date] = set()
        self._initialize_holidays()

    def _add_holiday(self, holiday_date: date, description: str) -> None:
        """Adds a holiday to internal indexes"""
        year = holiday_date.year
        if year not in self._holidays_by_year:
            self._holidays_by_year[year] = []
        self._holidays_by_year[year].append((holiday_date, description))
        self._holiday_dates.add(holiday_date)

    @property
    def holidays(self) -> List[Tuple[date, str]]:
        """Returns all holidays sorted by date"""
        all_holidays = []
        for year_holidays in self._holidays_by_year.values():
            all_holidays.extend(year_holidays)
        return sorted(all_holidays, key=lambda x: x[0])

    @lru_cache(maxsize=128)
    def get_holidays_by_year(self, year: int) -> List[Tuple[date, str]]:
        """Returns holidays for a specific year with cache"""
        return sorted(self._holidays_by_year.get(year, []), key=lambda x: x[0])

    def is_holiday(self, check_date: date) -> bool:
        """Checks if a date is a holiday in O(1)"""
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

        # 2026
        self._add_holiday(date(2026, 1, 1), 'New year')
        self._add_holiday(date(2026, 1, 19), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2026, 2, 16), "Washington's Birthday")
        self._add_holiday(date(2026, 4, 3), 'Good Friday')
        self._add_holiday(date(2026, 5, 25), 'Memorial Day')
        self._add_holiday(date(2026, 6, 19), 'Juneteenth National Independence Day')
        self._add_holiday(date(2026, 7, 4), 'Independence Day')
        self._add_holiday(date(2026, 9, 7), 'Labor Day')
        self._add_holiday(date(2026, 11, 26), 'Thanksgiving Day')
        self._add_holiday(date(2026, 12, 25), 'Christmas Day')
        self._add_holiday(date(2026, 12, 31), 'Last day of year')


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

        # 2026
        self._add_holiday(date(2026, 1, 1), 'New year')
        self._add_holiday(date(2026, 1, 19), 'Martin Luther King, Jr. Day')
        self._add_holiday(date(2026, 2, 16), "Washington's Birthday")
        self._add_holiday(date(2026, 4, 3), 'Good Friday')
        self._add_holiday(date(2026, 5, 25), 'Memorial Day')
        self._add_holiday(date(2026, 6, 19), 'Juneteenth National Independence Day')
        self._add_holiday(date(2026, 7, 4), 'Independence Day')
        self._add_holiday(date(2026, 9, 7), 'Labor Day')
        self._add_holiday(date(2026, 11, 26), 'Thanksgiving Day')
        self._add_holiday(date(2026, 12, 25), 'Christmas Day')
        self._add_holiday(date(2026, 12, 31), 'Last day of year')


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

        # 2026
        self._add_holiday(date(2026, 1, 1), 'New year')
        self._add_holiday(date(2026, 2, 16), 'Carnaval Monday')
        self._add_holiday(date(2026, 2, 17), 'Carnaval')
        self._add_holiday(date(2026, 4, 3), 'Good Friday')
        self._add_holiday(date(2026, 4, 21), "Tiradentes' Day")
        self._add_holiday(date(2026, 5, 1), 'Labour Day')
        self._add_holiday(date(2026, 6, 11), 'Corpus Christi')
        self._add_holiday(date(2026, 9, 7), 'Independence Day')
        self._add_holiday(date(2026, 10, 12), 'Our Lady of Aparecida')
        self._add_holiday(date(2026, 11, 2), "All Souls' Day")
        self._add_holiday(date(2026, 11, 15), 'Republic Day')
        self._add_holiday(date(2026, 12, 25), 'Christmas Day')
        self._add_holiday(date(2026, 12, 31), 'Last day of year')


class SSE(StockExchange):
    """
    Shanghai Stock Exchange (SSE)
    Source: http://www.sse.com.cn/
    """

    def _initialize_holidays(self) -> None:
        # 2020
        self._add_holiday(date(2020, 1, 1), 'New Year\'s Day')
        self._add_holiday(date(2020, 1, 24), 'Chinese New Year')
        self._add_holiday(date(2020, 1, 27), 'Chinese New Year Holiday')
        self._add_holiday(date(2020, 1, 28), 'Chinese New Year Holiday')
        self._add_holiday(date(2020, 1, 29), 'Chinese New Year Holiday')
        self._add_holiday(date(2020, 1, 30), 'Chinese New Year Holiday')
        self._add_holiday(date(2020, 4, 6), 'Qingming Festival')
        self._add_holiday(date(2020, 5, 1), 'Labour Day')
        self._add_holiday(date(2020, 5, 4), 'Labour Day Holiday')
        self._add_holiday(date(2020, 5, 5), 'Labour Day Holiday')
        self._add_holiday(date(2020, 6, 25), 'Dragon Boat Festival')
        self._add_holiday(date(2020, 6, 26), 'Dragon Boat Festival Holiday')
        self._add_holiday(date(2020, 10, 1), 'National Day')
        self._add_holiday(date(2020, 10, 2), 'National Day Holiday')
        self._add_holiday(date(2020, 10, 5), 'National Day Holiday')
        self._add_holiday(date(2020, 10, 6), 'National Day Holiday')
        self._add_holiday(date(2020, 10, 7), 'National Day Holiday')
        self._add_holiday(date(2020, 10, 8), 'National Day Holiday')

        # 2021
        self._add_holiday(date(2021, 1, 1), 'New Year\'s Day')
        self._add_holiday(date(2021, 2, 11), 'Chinese New Year')
        self._add_holiday(date(2021, 2, 12), 'Chinese New Year Holiday')
        self._add_holiday(date(2021, 2, 15), 'Chinese New Year Holiday')
        self._add_holiday(date(2021, 2, 16), 'Chinese New Year Holiday')
        self._add_holiday(date(2021, 2, 17), 'Chinese New Year Holiday')
        self._add_holiday(date(2021, 4, 5), 'Qingming Festival')
        self._add_holiday(date(2021, 5, 1), 'Labour Day')
        self._add_holiday(date(2021, 5, 3), 'Labour Day Holiday')
        self._add_holiday(date(2021, 5, 4), 'Labour Day Holiday')
        self._add_holiday(date(2021, 5, 5), 'Labour Day Holiday')
        self._add_holiday(date(2021, 6, 14), 'Dragon Boat Festival')
        self._add_holiday(date(2021, 9, 20), 'Mid-Autumn Festival')
        self._add_holiday(date(2021, 9, 21), 'Mid-Autumn Festival Holiday')
        self._add_holiday(date(2021, 10, 1), 'National Day')
        self._add_holiday(date(2021, 10, 4), 'National Day Holiday')
        self._add_holiday(date(2021, 10, 5), 'National Day Holiday')
        self._add_holiday(date(2021, 10, 6), 'National Day Holiday')
        self._add_holiday(date(2021, 10, 7), 'National Day Holiday')

        # 2022
        self._add_holiday(date(2022, 1, 1), 'New Year\'s Day')
        self._add_holiday(date(2022, 1, 3), 'New Year Holiday')
        self._add_holiday(date(2022, 1, 31), 'Chinese New Year')
        self._add_holiday(date(2022, 2, 1), 'Chinese New Year Holiday')
        self._add_holiday(date(2022, 2, 2), 'Chinese New Year Holiday')
        self._add_holiday(date(2022, 2, 3), 'Chinese New Year Holiday')
        self._add_holiday(date(2022, 2, 4), 'Chinese New Year Holiday')
        self._add_holiday(date(2022, 4, 4), 'Qingming Festival')
        self._add_holiday(date(2022, 4, 5), 'Qingming Festival Holiday')
        self._add_holiday(date(2022, 5, 2), 'Labour Day')
        self._add_holiday(date(2022, 5, 3), 'Labour Day Holiday')
        self._add_holiday(date(2022, 5, 4), 'Labour Day Holiday')
        self._add_holiday(date(2022, 6, 3), 'Dragon Boat Festival')
        self._add_holiday(date(2022, 9, 12), 'Mid-Autumn Festival')
        self._add_holiday(date(2022, 10, 3), 'National Day')
        self._add_holiday(date(2022, 10, 4), 'National Day Holiday')
        self._add_holiday(date(2022, 10, 5), 'National Day Holiday')
        self._add_holiday(date(2022, 10, 6), 'National Day Holiday')
        self._add_holiday(date(2022, 10, 7), 'National Day Holiday')

        # 2023
        self._add_holiday(date(2023, 1, 1), 'New Year\'s Day')
        self._add_holiday(date(2023, 1, 2), 'New Year Holiday')
        self._add_holiday(date(2023, 1, 23), 'Chinese New Year')
        self._add_holiday(date(2023, 1, 24), 'Chinese New Year Holiday')
        self._add_holiday(date(2023, 1, 25), 'Chinese New Year Holiday')
        self._add_holiday(date(2023, 1, 26), 'Chinese New Year Holiday')
        self._add_holiday(date(2023, 1, 27), 'Chinese New Year Holiday')
        self._add_holiday(date(2023, 4, 5), 'Qingming Festival')
        self._add_holiday(date(2023, 5, 1), 'Labour Day')
        self._add_holiday(date(2023, 5, 2), 'Labour Day Holiday')
        self._add_holiday(date(2023, 5, 3), 'Labour Day Holiday')
        self._add_holiday(date(2023, 6, 22), 'Dragon Boat Festival')
        self._add_holiday(date(2023, 6, 23), 'Dragon Boat Festival Holiday')
        self._add_holiday(date(2023, 9, 29), 'Mid-Autumn Festival')
        self._add_holiday(date(2023, 10, 2), 'National Day')
        self._add_holiday(date(2023, 10, 3), 'National Day Holiday')
        self._add_holiday(date(2023, 10, 4), 'National Day Holiday')
        self._add_holiday(date(2023, 10, 5), 'National Day Holiday')
        self._add_holiday(date(2023, 10, 6), 'National Day Holiday')

        # 2024
        self._add_holiday(date(2024, 1, 1), 'New Year\'s Day')
        self._add_holiday(date(2024, 2, 10), 'Chinese New Year')
        self._add_holiday(date(2024, 2, 11), 'Chinese New Year Holiday')
        self._add_holiday(date(2024, 2, 12), 'Chinese New Year Holiday')
        self._add_holiday(date(2024, 2, 13), 'Chinese New Year Holiday')
        self._add_holiday(date(2024, 2, 14), 'Chinese New Year Holiday')
        self._add_holiday(date(2024, 4, 4), 'Qingming Festival')
        self._add_holiday(date(2024, 4, 5), 'Qingming Festival Holiday')
        self._add_holiday(date(2024, 5, 1), 'Labour Day')
        self._add_holiday(date(2024, 5, 2), 'Labour Day Holiday')
        self._add_holiday(date(2024, 5, 3), 'Labour Day Holiday')
        self._add_holiday(date(2024, 6, 10), 'Dragon Boat Festival')
        self._add_holiday(date(2024, 9, 17), 'Mid-Autumn Festival')
        self._add_holiday(date(2024, 10, 1), 'National Day')
        self._add_holiday(date(2024, 10, 2), 'National Day Holiday')
        self._add_holiday(date(2024, 10, 3), 'National Day Holiday')
        self._add_holiday(date(2024, 10, 4), 'National Day Holiday')
        self._add_holiday(date(2024, 10, 7), 'National Day Holiday')

        # 2025
        self._add_holiday(date(2025, 1, 1), 'New Year\'s Day')
        self._add_holiday(date(2025, 1, 29), 'Chinese New Year')
        self._add_holiday(date(2025, 1, 30), 'Chinese New Year Holiday')
        self._add_holiday(date(2025, 1, 31), 'Chinese New Year Holiday')
        self._add_holiday(date(2025, 2, 3), 'Chinese New Year Holiday')
        self._add_holiday(date(2025, 2, 4), 'Chinese New Year Holiday')
        self._add_holiday(date(2025, 4, 4), 'Qingming Festival')
        self._add_holiday(date(2025, 5, 1), 'Labour Day')
        self._add_holiday(date(2025, 5, 2), 'Labour Day Holiday')
        self._add_holiday(date(2025, 5, 5), 'Labour Day Holiday')
        self._add_holiday(date(2025, 5, 31), 'Dragon Boat Festival')
        self._add_holiday(date(2025, 10, 1), 'National Day')
        self._add_holiday(date(2025, 10, 2), 'National Day Holiday')
        self._add_holiday(date(2025, 10, 3), 'National Day Holiday')
        self._add_holiday(date(2025, 10, 6), 'National Day Holiday')
        self._add_holiday(date(2025, 10, 7), 'National Day Holiday')

        # 2026
        self._add_holiday(date(2026, 1, 1), 'New year')
        self._add_holiday(date(2026, 1, 29), 'Chinese New Year')
        self._add_holiday(date(2026, 1, 30), 'Chinese New Year Holiday')
        self._add_holiday(date(2026, 1, 31), 'Chinese New Year Holiday')
        self._add_holiday(date(2026, 2, 3), 'Chinese New Year Holiday')
        self._add_holiday(date(2026, 2, 4), 'Chinese New Year Holiday')
        self._add_holiday(date(2026, 4, 4), 'Qingming Festival')
        self._add_holiday(date(2026, 5, 1), 'Labour Day')
        self._add_holiday(date(2026, 5, 2), 'Labour Day Holiday')
        self._add_holiday(date(2026, 5, 5), 'Labour Day Holiday')
        self._add_holiday(date(2026, 5, 31), 'Dragon Boat Festival')
        self._add_holiday(date(2026, 10, 1), 'National Day')
        self._add_holiday(date(2026, 10, 2), 'National Day Holiday')
        self._add_holiday(date(2026, 10, 3), 'National Day Holiday')
        self._add_holiday(date(2026, 10, 6), 'National Day Holiday')
        self._add_holiday(date(2026, 10, 7), 'National Day Holiday')


class JPX(StockExchange):
    """
    Japan Exchange Group (JPX) - Tokyo Stock Exchange
    Source: https://www.jpx.co.jp/english/corporate/about-jpx/calendar/
    """

    def _initialize_holidays(self) -> None:
        # 2020
        self._add_holiday(date(2020, 1, 1), "New Year's Day")
        self._add_holiday(date(2020, 1, 2), "New Year's Holiday")
        self._add_holiday(date(2020, 1, 3), "New Year's Holiday")
        self._add_holiday(date(2020, 1, 13), "Coming of Age Day")
        self._add_holiday(date(2020, 2, 11), "National Foundation Day")
        self._add_holiday(date(2020, 2, 24), "Emperor's Birthday")
        self._add_holiday(date(2020, 3, 20), "Vernal Equinox Day")
        self._add_holiday(date(2020, 4, 29), "Showa Day")
        self._add_holiday(date(2020, 5, 4), "Greenery Day")
        self._add_holiday(date(2020, 5, 5), "Children's Day")
        self._add_holiday(date(2020, 5, 6), "Constitution Memorial Day observed")
        self._add_holiday(date(2020, 7, 23), "Marine Day")
        self._add_holiday(date(2020, 7, 24), "Health and Sports Day")
        self._add_holiday(date(2020, 8, 10), "Mountain Day")
        self._add_holiday(date(2020, 9, 21), "Respect for the Aged Day")
        self._add_holiday(date(2020, 9, 22), "Autumnal Equinox Day")
        self._add_holiday(date(2020, 11, 3), "Culture Day")
        self._add_holiday(date(2020, 11, 23), "Labor Thanksgiving Day")
        self._add_holiday(date(2020, 12, 31), "New Year's Eve")

        # 2021
        self._add_holiday(date(2021, 1, 1), "New Year's Day")
        self._add_holiday(date(2021, 1, 2), "New Year's Holiday")
        self._add_holiday(date(2021, 1, 3), "New Year's Holiday")
        self._add_holiday(date(2021, 1, 11), "Coming of Age Day")
        self._add_holiday(date(2021, 2, 11), "National Foundation Day")
        self._add_holiday(date(2021, 2, 23), "Emperor's Birthday")
        self._add_holiday(date(2021, 3, 20), "Vernal Equinox Day")
        self._add_holiday(date(2021, 4, 29), "Showa Day")
        self._add_holiday(date(2021, 5, 3), "Constitution Memorial Day")
        self._add_holiday(date(2021, 5, 4), "Greenery Day")
        self._add_holiday(date(2021, 5, 5), "Children's Day")
        self._add_holiday(date(2021, 7, 22), "Marine Day")
        self._add_holiday(date(2021, 7, 23), "Health and Sports Day")
        self._add_holiday(date(2021, 8, 8), "Mountain Day")
        self._add_holiday(date(2021, 8, 9), "Mountain Day observed")
        self._add_holiday(date(2021, 9, 20), "Respect for the Aged Day")
        self._add_holiday(date(2021, 9, 23), "Autumnal Equinox Day")
        self._add_holiday(date(2021, 11, 3), "Culture Day")
        self._add_holiday(date(2021, 11, 23), "Labor Thanksgiving Day")
        self._add_holiday(date(2021, 12, 31), "New Year's Eve")

        # 2022
        self._add_holiday(date(2022, 1, 1), "New Year's Day")
        self._add_holiday(date(2022, 1, 3), "New Year's Holiday")
        self._add_holiday(date(2022, 1, 10), "Coming of Age Day")
        self._add_holiday(date(2022, 2, 11), "National Foundation Day")
        self._add_holiday(date(2022, 2, 23), "Emperor's Birthday")
        self._add_holiday(date(2022, 3, 21), "Vernal Equinox Day")
        self._add_holiday(date(2022, 4, 29), "Showa Day")
        self._add_holiday(date(2022, 5, 3), "Constitution Memorial Day")
        self._add_holiday(date(2022, 5, 4), "Greenery Day")
        self._add_holiday(date(2022, 5, 5), "Children's Day")
        self._add_holiday(date(2022, 7, 18), "Marine Day")
        self._add_holiday(date(2022, 8, 11), "Mountain Day")
        self._add_holiday(date(2022, 9, 19), "Respect for the Aged Day")
        self._add_holiday(date(2022, 9, 23), "Autumnal Equinox Day")
        self._add_holiday(date(2022, 10, 10), "Health and Sports Day")
        self._add_holiday(date(2022, 11, 3), "Culture Day")
        self._add_holiday(date(2022, 11, 23), "Labor Thanksgiving Day")
        self._add_holiday(date(2022, 12, 31), "New Year's Eve")

        # 2023
        self._add_holiday(date(2023, 1, 1), "New Year's Day")
        self._add_holiday(date(2023, 1, 2), "New Year's Holiday")
        self._add_holiday(date(2023, 1, 3), "New Year's Holiday")
        self._add_holiday(date(2023, 1, 9), "Coming of Age Day")
        self._add_holiday(date(2023, 2, 11), "National Foundation Day")
        self._add_holiday(date(2023, 2, 23), "Emperor's Birthday")
        self._add_holiday(date(2023, 3, 21), "Vernal Equinox Day")
        self._add_holiday(date(2023, 4, 29), "Showa Day")
        self._add_holiday(date(2023, 5, 3), "Constitution Memorial Day")
        self._add_holiday(date(2023, 5, 4), "Greenery Day")
        self._add_holiday(date(2023, 5, 5), "Children's Day")
        self._add_holiday(date(2023, 7, 17), "Marine Day")
        self._add_holiday(date(2023, 8, 11), "Mountain Day")
        self._add_holiday(date(2023, 9, 18), "Respect for the Aged Day")
        self._add_holiday(date(2023, 9, 23), "Autumnal Equinox Day")
        self._add_holiday(date(2023, 10, 9), "Health and Sports Day")
        self._add_holiday(date(2023, 11, 3), "Culture Day")
        self._add_holiday(date(2023, 11, 23), "Labor Thanksgiving Day")
        self._add_holiday(date(2023, 12, 31), "New Year's Eve")

        # 2024
        self._add_holiday(date(2024, 1, 1), "New Year's Day")
        self._add_holiday(date(2024, 1, 2), "New Year's Holiday")
        self._add_holiday(date(2024, 1, 3), "New Year's Holiday")
        self._add_holiday(date(2024, 1, 8), "Coming of Age Day")
        self._add_holiday(date(2024, 2, 11), "National Foundation Day")
        self._add_holiday(date(2024, 2, 12), "National Foundation Day observed")
        self._add_holiday(date(2024, 2, 23), "Emperor's Birthday")
        self._add_holiday(date(2024, 3, 20), "Vernal Equinox Day")
        self._add_holiday(date(2024, 4, 29), "Showa Day")
        self._add_holiday(date(2024, 5, 3), "Constitution Memorial Day")
        self._add_holiday(date(2024, 5, 4), "Greenery Day")
        self._add_holiday(date(2024, 5, 5), "Children's Day")
        self._add_holiday(date(2024, 5, 6), "Children's Day observed")
        self._add_holiday(date(2024, 7, 15), "Marine Day")
        self._add_holiday(date(2024, 8, 11), "Mountain Day")
        self._add_holiday(date(2024, 8, 12), "Mountain Day observed")
        self._add_holiday(date(2024, 9, 16), "Respect for the Aged Day")
        self._add_holiday(date(2024, 9, 22), "Autumnal Equinox Day")
        self._add_holiday(date(2024, 9, 23), "Autumnal Equinox Day observed")
        self._add_holiday(date(2024, 10, 14), "Health and Sports Day")
        self._add_holiday(date(2024, 11, 3), "Culture Day")
        self._add_holiday(date(2024, 11, 4), "Culture Day observed")
        self._add_holiday(date(2024, 11, 23), "Labor Thanksgiving Day")
        self._add_holiday(date(2024, 12, 31), "New Year's Eve")

        # 2025
        self._add_holiday(date(2025, 1, 1), "New Year's Day")
        self._add_holiday(date(2025, 1, 2), "New Year's Holiday")
        self._add_holiday(date(2025, 1, 3), "New Year's Holiday")
        self._add_holiday(date(2025, 1, 13), "Coming of Age Day")
        self._add_holiday(date(2025, 2, 11), "National Foundation Day")
        self._add_holiday(date(2025, 2, 23), "Emperor's Birthday")
        self._add_holiday(date(2025, 2, 24), "Emperor's Birthday observed")
        self._add_holiday(date(2025, 3, 20), "Vernal Equinox Day")
        self._add_holiday(date(2025, 4, 29), "Showa Day")
        self._add_holiday(date(2025, 5, 3), "Constitution Memorial Day")
        self._add_holiday(date(2025, 5, 4), "Greenery Day")
        self._add_holiday(date(2025, 5, 5), "Children's Day")
        self._add_holiday(date(2025, 5, 6), "Children's Day observed")
        self._add_holiday(date(2025, 7, 21), "Marine Day")
        self._add_holiday(date(2025, 8, 11), "Mountain Day")
        self._add_holiday(date(2025, 9, 15), "Respect for the Aged Day")
        self._add_holiday(date(2025, 9, 23), "Autumnal Equinox Day")
        self._add_holiday(date(2025, 10, 13), "Health and Sports Day")
        self._add_holiday(date(2025, 11, 3), "Culture Day")
        self._add_holiday(date(2025, 11, 23), "Labor Thanksgiving Day")
        self._add_holiday(date(2025, 11, 24), "Labor Thanksgiving Day observed")
        self._add_holiday(date(2025, 12, 31), "New Year's Eve")

        # 2026
        self._add_holiday(date(2026, 1, 1), "New Year's Day")
        self._add_holiday(date(2026, 1, 2), "New Year's Holiday")
        self._add_holiday(date(2026, 1, 3), "New Year's Holiday")
        self._add_holiday(date(2026, 1, 13), "Coming of Age Day")
        self._add_holiday(date(2026, 2, 11), "National Foundation Day")
        self._add_holiday(date(2026, 2, 23), "Emperor's Birthday")
        self._add_holiday(date(2026, 2, 24), "Emperor's Birthday observed")
        self._add_holiday(date(2026, 3, 20), "Vernal Equinox Day")
        self._add_holiday(date(2026, 4, 29), "Showa Day")
        self._add_holiday(date(2026, 5, 3), "Constitution Memorial Day")
        self._add_holiday(date(2026, 5, 4), "Greenery Day")
        self._add_holiday(date(2026, 5, 5), "Children's Day")
        self._add_holiday(date(2026, 5, 6), "Children's Day observed")
        self._add_holiday(date(2026, 7, 21), "Marine Day")
        self._add_holiday(date(2026, 8, 11), "Mountain Day")
        self._add_holiday(date(2026, 9, 15), "Respect for the Aged Day")
        self._add_holiday(date(2026, 9, 23), "Autumnal Equinox Day")
        self._add_holiday(date(2026, 10, 13), "Health and Sports Day")
        self._add_holiday(date(2026, 11, 3), "Culture Day")
        self._add_holiday(date(2026, 11, 23), "Labor Thanksgiving Day")
        self._add_holiday(date(2026, 11, 24), "Labor Thanksgiving Day observed")
        self._add_holiday(date(2026, 12, 31), "New Year's Eve")


class Holidays:
    """
    Holidays methods

    """
    def __init__(self, exchange=None):
        self.stock_exchange = exchange

    def get_holidays(self):
        if self.stock_exchange is None:
            return []
        return self.stock_exchange.holidays

    def get_holidays_by_year(self, year):
        if self.stock_exchange is None:
            return []
        return self.stock_exchange.get_holidays_by_year(year)

    def is_date_holiday(self, date):
        if self.stock_exchange is None:
            return False
        return self.stock_exchange.is_holiday(date)
