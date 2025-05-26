from datetime import date


class NYSE:
    """
    New York Stock Exchange (NYSE)
    Source: https://www.nyse.com/markets/hours-calendars

    """
    HOLIDAYS = (
        (date(2020, 1, 1), 'New year'),
        (date(2020, 1, 20), 'Martin Luther King, Jr. Day'),
        (date(2020, 2, 17), "Washington's Birthday"),
        (date(2020, 4, 10), 'Good Friday'),
        (date(2020, 5, 25), 'Memorial Day'),
        (date(2020, 7, 4), 'Independence Day'),
        (date(2020, 9, 7), 'Labor Day'),
        (date(2020, 11, 26), 'Thanksgiving Day'),
        (date(2020, 12, 25), 'Christmas Day'),
        (date(2020, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2021, 1, 1), 'New year'),
        (date(2021, 1, 18), 'Martin Luther King, Jr. Day'),
        (date(2021, 2, 15), "Washington's Birthday"),
        (date(2021, 4, 2), 'Good Friday'),
        (date(2021, 5, 31), 'Memorial Day'),
        (date(2021, 7, 4), 'Independence Day'),
        (date(2021, 9, 6), 'Labor Day'),
        (date(2021, 11, 25), 'Thanksgiving Day'),
        (date(2021, 12, 25), 'Christmas Day'),
        (date(2021, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2022, 1, 1), 'New year'),
        (date(2022, 1, 17), 'Martin Luther King, Jr. Day'),
        (date(2022, 2, 21), "Washington's Birthday"),
        (date(2022, 4, 15), 'Good Friday'),
        (date(2022, 5, 30), 'Memorial Day'),
        (date(2022, 6, 20), 'Juneteenth National Independence Day'),
        (date(2022, 7, 4), 'Independence Day'),
        (date(2022, 9, 5), 'Labor Day'),
        (date(2022, 11, 24), 'Thanksgiving Day'),
        (date(2022, 12, 25), 'Christmas Day'),
        (date(2022, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2023, 1, 1), 'New year'),
        (date(2023, 1, 16), 'Martin Luther King, Jr. Day'),
        (date(2023, 2, 20), "Washington's Birthday"),
        (date(2023, 4, 7), 'Good Friday'),
        (date(2023, 5, 29), 'Memorial Day'),
        (date(2023, 6, 19), 'Juneteenth National Independence Day'),
        (date(2023, 7, 4), 'Independence Day'),
        (date(2023, 9, 4), 'Labor Day'),
        (date(2023, 11, 23), 'Thanksgiving Day'),
        (date(2023, 12, 25), 'Christmas Day'),
        (date(2023, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2024, 1, 1), 'New year'),
        (date(2024, 1, 15), 'Martin Luther King, Jr. Day'),
        (date(2024, 2, 19), "Washington's Birthday"),
        (date(2024, 3, 29), 'Good Friday'),
        (date(2024, 5, 27), 'Memorial Day'),
        (date(2024, 6, 19), 'Juneteenth National Independence Day'),
        (date(2024, 7, 4), 'Independence Day'),
        (date(2024, 9, 2), 'Labor Day'),
        (date(2024, 11, 28), 'Thanksgiving Day'),
        (date(2024, 12, 25), 'Christmas Day'),
        (date(2024, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2025, 1, 1), 'New year'),
        (date(2025, 1, 20), 'Martin Luther King, Jr. Day'),
        (date(2025, 2, 17), "Washington's Birthday"),
        (date(2025, 4, 18), 'Good Friday'),
        (date(2025, 5, 26), 'Memorial Day'),
        (date(2025, 6, 19), 'Juneteenth National Independence Day'),
        (date(2025, 7, 4), 'Independence Day'),
        (date(2025, 9, 1), 'Labor Day'),
        (date(2025, 11, 27), 'Thanksgiving Day'),
        (date(2025, 12, 25), 'Christmas Day'),
        (date(2025, 12, 31), 'Last day of year')
    )


class CME:
    """
    Chicago Mercantile Exchange (CME)
    Source: https://www.cmegroup.com/tools-information/holiday-calendar.html

    """
    HOLIDAYS = (
        (date(2020, 1, 1), 'New year'),
        (date(2020, 1, 20), 'Martin Luther King, Jr. Day'),
        (date(2020, 2, 17), "Washington's Birthday"),
        (date(2020, 4, 10), 'Good Friday'),
        (date(2020, 5, 25), 'Memorial Day'),
        (date(2020, 7, 4), 'Independence Day'),
        (date(2020, 9, 7), 'Labor Day'),
        (date(2020, 11, 26), 'Thanksgiving Day'),
        (date(2020, 12, 25), 'Christmas Day'),
        (date(2020, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2021, 1, 1), 'New year'),
        (date(2021, 1, 18), 'Martin Luther King, Jr. Day'),
        (date(2021, 2, 15), "Washington's Birthday"),
        (date(2021, 4, 2), 'Good Friday'),
        (date(2021, 5, 31), 'Memorial Day'),
        (date(2021, 7, 4), 'Independence Day'),
        (date(2021, 9, 6), 'Labor Day'),
        (date(2021, 11, 25), 'Thanksgiving Day'),
        (date(2021, 12, 25), 'Christmas Day'),
        (date(2021, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2022, 1, 1), 'New year'),
        (date(2022, 1, 17), 'Martin Luther King, Jr. Day'),
        (date(2022, 2, 21), "Washington's Birthday"),
        (date(2022, 4, 15), 'Good Friday'),
        (date(2022, 5, 30), 'Memorial Day'),
        (date(2022, 6, 20), 'Juneteenth National Independence Day'),
        (date(2022, 7, 4), 'Independence Day'),
        (date(2022, 9, 5), 'Labor Day'),
        (date(2022, 11, 24), 'Thanksgiving Day'),
        (date(2022, 12, 25), 'Christmas Day'),
        (date(2022, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2023, 1, 1), 'New year'),
        (date(2023, 1, 16), 'Martin Luther King, Jr. Day'),
        (date(2023, 2, 20), "Washington's Birthday"),
        (date(2023, 4, 7), 'Good Friday'),
        (date(2023, 5, 29), 'Memorial Day'),
        (date(2023, 6, 19), 'Juneteenth National Independence Day'),
        (date(2023, 7, 4), 'Independence Day'),
        (date(2023, 9, 4), 'Labor Day'),
        (date(2023, 11, 23), 'Thanksgiving Day'),
        (date(2023, 12, 25), 'Christmas Day'),
        (date(2023, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2024, 1, 1), 'New year'),
        (date(2024, 1, 15), 'Martin Luther King, Jr. Day'),
        (date(2024, 2, 19), "Washington's Birthday"),
        (date(2024, 3, 29), 'Good Friday'),
        (date(2024, 5, 27), 'Memorial Day'),
        (date(2024, 6, 19), 'Juneteenth National Independence Day'),
        (date(2024, 7, 4), 'Independence Day'),
        (date(2024, 9, 2), 'Labor Day'),
        (date(2024, 11, 28), 'Thanksgiving Day'),
        (date(2024, 12, 25), 'Christmas Day'),
        (date(2024, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2025, 1, 1), 'New year'),
        (date(2025, 1, 20), 'Martin Luther King, Jr. Day'),
        (date(2025, 2, 17), "Washington's Birthday"),
        (date(2025, 4, 18), 'Good Friday'),
        (date(2025, 5, 26), 'Memorial Day'),
        (date(2025, 6, 19), 'Juneteenth National Independence Day'),
        (date(2025, 7, 4), 'Independence Day'),
        (date(2025, 9, 1), 'Labor Day'),
        (date(2025, 11, 27), 'Thanksgiving Day'),
        (date(2025, 12, 25), 'Christmas Day'),
        (date(2025, 12, 31), 'Last day of year')
    )


class B3:
    """
    Sao Paulo Stock exchange (B3) formerly BM&F-BOVESPA
    Source: http://www.b3.com.br

    """
    HOLIDAYS = (
        (date(2020, 1, 1), 'New year'),
        (date(2020, 2, 24), 'Carnaval Monday'),
        (date(2020, 2, 25), 'Carnaval'),
        (date(2020, 4, 10), 'Good Friday'),
        (date(2020, 4, 21), "Tiradentes' Day"),
        (date(2020, 5, 1), 'Labour Day'),
        (date(2020, 6, 11), 'Corpus Christi'),
        (date(2020, 7, 9), 'Constitutional Revolution of 1932'),
        (date(2020, 9, 7), 'Independence Day'),
        (date(2020, 10, 12), 'Our Lady of Aparecida'),
        (date(2020, 11, 2), "All Souls' Day"),
        (date(2020, 11, 15), 'Republic Day'),
        (date(2020, 12, 25), 'Christmas Day'),
        (date(2020, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2021, 1, 1), 'New year'),
        (date(2021, 1, 25), 'Anniversary of the city of São Paulo'),
        (date(2021, 2, 15), 'Carnaval Monday'),
        (date(2021, 2, 16), 'Carnaval'),
        (date(2021, 4, 2), 'Good Friday'),
        (date(2021, 4, 21), "Tiradentes' Day"),
        (date(2021, 5, 1), 'Labour Day'),
        (date(2021, 6, 3), 'Corpus Christi'),
        (date(2021, 7, 9), 'Constitutional Revolution of 1932'),
        (date(2021, 9, 7), 'Independence Day'),
        (date(2021, 10, 12), 'Our Lady of Aparecida'),
        (date(2021, 11, 2), "All Souls' Day"),
        (date(2021, 11, 15), 'Republic Day'),
        (date(2021, 12, 25), 'Christmas Day'),
        (date(2021, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2022, 1, 1), 'New year'),
        (date(2022, 2, 28), 'Carnaval Monday'),
        (date(2022, 3, 1), 'Carnaval'),
        (date(2022, 4, 15), 'Good Friday'),
        (date(2022, 4, 21), "Tiradentes' Day"),
        (date(2022, 5, 1), 'Labour Day'),
        (date(2022, 6, 16), 'Corpus Christi'),
        (date(2022, 9, 7), 'Independence Day'),
        (date(2022, 10, 12), 'Our Lady of Aparecida'),
        (date(2022, 11, 2), "All Souls' Day"),
        (date(2022, 11, 15), 'Republic Day'),
        (date(2022, 12, 25), 'Christmas Day'),
        (date(2022, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2023, 1, 1), 'New year'),
        (date(2023, 2, 21), 'Carnaval Monday'),
        (date(2023, 2, 22), 'Carnaval'),
        (date(2023, 4, 7), 'Good Friday'),
        (date(2023, 4, 21), "Tiradentes' Day"),
        (date(2023, 5, 1), 'Labour Day'),
        (date(2023, 6, 8), 'Corpus Christi'),
        (date(2023, 9, 7), 'Independence Day'),
        (date(2023, 10, 12), 'Our Lady of Aparecida'),
        (date(2023, 11, 2), "All Souls' Day"),
        (date(2023, 11, 15), 'Republic Day'),
        (date(2023, 12, 25), 'Christmas Day'),
        (date(2023, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2024, 1, 1), 'New year'),
        (date(2024, 2, 12), 'Carnaval Monday'),
        (date(2024, 2, 13), 'Carnaval'),
        (date(2024, 3, 29), 'Good Friday'),
        (date(2024, 4, 21), "Tiradentes' Day"),
        (date(2024, 5, 1), 'Labour Day'),
        (date(2024, 5, 30), 'Corpus Christi'),
        (date(2024, 9, 7), 'Independence Day'),
        (date(2024, 10, 12), 'Our Lady of Aparecida'),
        (date(2024, 11, 2), "All Souls' Day"),
        (date(2024, 11, 15), 'Republic Day'),
        (date(2024, 12, 25), 'Christmas Day'),
        (date(2024, 12, 31), 'Last day of year')
    )
    HOLIDAYS = HOLIDAYS + (
        (date(2025, 1, 1), 'New year'),
        (date(2025, 3, 3), 'Carnaval Monday'),
        (date(2025, 3, 4), 'Carnaval'),
        (date(2025, 4, 18), 'Good Friday'),
        (date(2025, 4, 21), "Tiradentes' Day"),
        (date(2025, 5, 1), 'Labour Day'),
        (date(2025, 6, 19), 'Corpus Christi'),
        (date(2025, 9, 7), 'Independence Day'),
        (date(2025, 10, 12), 'Our Lady of Aparecida'),
        (date(2025, 11, 2), "All Souls' Day"),
        (date(2025, 11, 15), 'Republic Day'),
        (date(2025, 12, 25), 'Christmas Day'),
        (date(2025, 12, 31), 'Last day of year')
    )


class Holidays:
    """
    Holidays methods

    """
    def __init__(self, exchange=None):
        self.stock_exchange = exchange

    def get_holidays(self):
        return self.stock_exchange.HOLIDAYS

    def get_holidays_by_year(self, year):
        days = []
        for date_holiday, label in self.stock_exchange.HOLIDAYS:
            if date_holiday.year == year:
                days.append((
                    date(year, date_holiday.month, date_holiday.day),
                    label
                ))
        return days

    def is_date_holiday(self, date):
        for holiday in self.stock_exchange.HOLIDAYS:
            if holiday[0] == date:
                return True
        return False
