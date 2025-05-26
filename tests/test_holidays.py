from datetime import date
from unittest import TestCase

from stock.stock_exchange_holidays import Holidays, NYSE, CME, B3, SSE, JPX


class TestNYSE(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=NYSE())
        self.nyse_holidays = self.holidays.get_holidays()

        self.all_holidays = {
            # 2020
            date(2020, 1, 1): True,
            date(2020, 1, 20): True,
            date(2020, 2, 17): True,
            date(2020, 4, 10): True,
            date(2020, 5, 25): True,
            date(2020, 7, 4): True,
            date(2020, 9, 7): True,
            date(2020, 11, 26): True,
            date(2020, 12, 25): True,
            date(2020, 12, 26): False,
            # 2021
            date(2021, 1, 1): True,
            date(2021, 1, 18): True,
            date(2021, 2, 15): True,
            date(2021, 4, 2): True,
            date(2021, 5, 31): True,
            date(2021, 7, 4): True,
            date(2021, 9, 6): True,
            date(2021, 11, 25): True,
            date(2021, 12, 25): True,
            date(2021, 12, 26): False,
            # 2022
            date(2022, 1, 1): True,
            date(2022, 1, 17): True,
            date(2022, 2, 21): True,
            date(2022, 4, 15): True,
            date(2022, 5, 30): True,
            date(2022, 6, 20): True,
            date(2022, 7, 4): True,
            date(2022, 9, 5): True,
            date(2022, 11, 24): True,
            date(2022, 12, 25): True,
            date(2022, 12, 26): False,
            # 2023
            date(2023, 1, 1): True,
            date(2023, 1, 16): True,
            date(2023, 2, 20): True,
            date(2023, 4, 7): True,
            date(2023, 5, 29): True,
            date(2023, 6, 19): True,
            date(2023, 7, 4): True,
            date(2023, 9, 4): True,
            date(2023, 11, 23): True,
            date(2023, 12, 25): True,
            date(2023, 12, 26): False,
            # 2024
            date(2024, 1, 1): True,
            date(2024, 1, 15): True,
            date(2024, 2, 19): True,
            date(2024, 3, 29): True,
            date(2024, 5, 27): True,
            date(2024, 6, 19): True,
            date(2024, 7, 4): True,
            date(2024, 9, 2): True,
            date(2024, 11, 28): True,
            date(2024, 12, 25): True,
            date(2024, 12, 26): False,
            # 2025
            date(2025, 1, 1): True,
            date(2025, 1, 20): True,
            date(2025, 2, 17): True,
            date(2025, 4, 18): True,
            date(2025, 5, 26): True,
            date(2025, 6, 19): True,
            date(2025, 7, 4): True,
            date(2025, 9, 1): True,
            date(2025, 11, 27): True,
            date(2025, 12, 25): True,
            date(2025, 12, 26): False,
        }

    def test_nyse_all_holidays(self):
        for holiday in self.all_holidays.items():
            if holiday[1]:
                self.assertTrue(self.holidays.is_date_holiday(holiday[0]))
            else:
                self.assertFalse(self.holidays.is_date_holiday(holiday[0]))

    def test_nyse_first_day_year_is_holiday(self):
        get_date = date(2020, 1, 1)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_nyse_independence_day_is_holiday(self):
        get_date = date(2022, 7, 4)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_nyse_random_date_is_not_holiday(self):
        get_date = date(2020, 1, 10)
        self.assertFalse(self.holidays.is_date_holiday(get_date))

    def test_nyse_holidays_2020(self):
        year = 2020
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 10)

    def test_nyse_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 10)

    def test_nyse_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)

    def test_nyse_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)

    def test_nyse_holidays_2024(self):
        year = 2024
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)

    def test_nyse_holidays_2025(self):
        year = 2025
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)


class TestCME(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=CME())
        self.cme_holidays = self.holidays.get_holidays()

        self.all_holidays = {
            # 2020
            date(2020, 1, 1): True,
            date(2020, 1, 20): True,
            date(2020, 2, 17): True,
            date(2020, 4, 10): True,
            date(2020, 5, 25): True,
            date(2020, 7, 4): True,
            date(2020, 9, 7): True,
            date(2020, 11, 26): True,
            date(2020, 12, 25): True,
            date(2020, 12, 26): False,
            # 2021
            date(2021, 1, 1): True,
            date(2021, 1, 18): True,
            date(2021, 2, 15): True,
            date(2021, 4, 2): True,
            date(2021, 5, 31): True,
            date(2021, 7, 4): True,
            date(2021, 9, 6): True,
            date(2021, 11, 25): True,
            date(2021, 12, 25): True,
            date(2021, 12, 26): False,
            # 2022
            date(2022, 1, 1): True,
            date(2022, 1, 17): True,
            date(2022, 2, 21): True,
            date(2022, 4, 15): True,
            date(2022, 5, 30): True,
            date(2022, 6, 20): True,
            date(2022, 7, 4): True,
            date(2022, 9, 5): True,
            date(2022, 11, 24): True,
            date(2022, 12, 25): True,
            date(2022, 12, 26): False,
            # 2023
            date(2023, 1, 1): True,
            date(2023, 1, 16): True,
            date(2023, 2, 20): True,
            date(2023, 4, 7): True,
            date(2023, 5, 29): True,
            date(2023, 6, 19): True,
            date(2023, 7, 4): True,
            date(2023, 9, 4): True,
            date(2023, 11, 23): True,
            date(2023, 12, 25): True,
            date(2023, 12, 26): False,
            # 2024
            date(2024, 1, 1): True,
            date(2024, 1, 15): True,
            date(2024, 2, 19): True,
            date(2024, 3, 29): True,
            date(2024, 5, 27): True,
            date(2024, 6, 19): True,
            date(2024, 7, 4): True,
            date(2024, 9, 2): True,
            date(2024, 11, 28): True,
            date(2024, 12, 25): True,
            date(2024, 12, 26): False,
            # 2025
            date(2025, 1, 1): True,
            date(2025, 1, 20): True,
            date(2025, 2, 17): True,
            date(2025, 4, 18): True,
            date(2025, 5, 26): True,
            date(2025, 6, 19): True,
            date(2025, 7, 4): True,
            date(2025, 9, 1): True,
            date(2025, 11, 27): True,
            date(2025, 12, 25): True,
            date(2025, 12, 26): False,
        }

    def test_cme_all_holidays(self):
        for holiday in self.all_holidays.items():
            if holiday[1]:
                self.assertTrue(self.holidays.is_date_holiday(holiday[0]))
            else:
                self.assertFalse(self.holidays.is_date_holiday(holiday[0]))

    def test_cme_first_day_year_is_holiday(self):
        get_date = date(2020, 1, 1)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_cme_independence_day_is_holiday(self):
        get_date = date(2022, 7, 4)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_cme_random_date_is_not_holiday(self):
        get_date = date(2020, 1, 10)
        self.assertFalse(self.holidays.is_date_holiday(get_date))

    def test_cme_holidays_2020(self):
        year = 2020
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 10)

    def test_cme_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 10)

    def test_cme_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)

    def test_cme_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)

    def test_cme_holidays_2024(self):
        year = 2024
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)

    def test_cme_holidays_2025(self):
        year = 2025
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)


class TestB3(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=B3())
        self.b3_holidays = self.holidays.get_holidays()

        self.all_holidays = {
            # 2020
            date(2020, 1, 1): True,
            date(2020, 2, 24): True,
            date(2020, 2, 25): True,
            date(2020, 4, 10): True,
            date(2020, 4, 21): True,
            date(2020, 5, 1): True,
            date(2020, 6, 11): True,
            date(2020, 7, 9): True,
            date(2020, 9, 7): True,
            date(2020, 10, 12): True,
            date(2020, 11, 2): True,
            date(2020, 11, 15): True,
            date(2020, 12, 25): True,
            date(2020, 12, 26): False,
            date(2020, 12, 31): True,
            # 2021
            date(2021, 1, 1): True,
            date(2021, 1, 25): True,
            date(2021, 2, 15): True,
            date(2021, 2, 16): True,
            date(2021, 4, 2): True,
            date(2021, 4, 21): True,
            date(2021, 5, 1): True,
            date(2021, 6, 3): True,
            date(2021, 7, 9): True,
            date(2021, 9, 7): True,
            date(2021, 10, 12): True,
            date(2021, 11, 2): True,
            date(2021, 11, 15): True,
            date(2021, 12, 25): True,
            date(2021, 12, 31): True,
            date(2021, 12, 26): False,
            # 2022
            date(2022, 1, 1): True,
            date(2022, 2, 28): True,
            date(2022, 3, 1): True,
            date(2022, 4, 15): True,
            date(2022, 4, 21): True,
            date(2022, 5, 1): True,
            date(2022, 6, 16): True,
            date(2022, 9, 7): True,
            date(2022, 10, 12): True,
            date(2022, 11, 2): True,
            date(2022, 11, 15): True,
            date(2022, 12, 25): True,
            date(2022, 12, 31): True,
            date(2022, 12, 26): False,
            # 2023
            date(2023, 1, 1): True,
            date(2023, 2, 21): True,
            date(2023, 2, 22): True,
            date(2023, 4, 7): True,
            date(2023, 4, 21): True,
            date(2023, 5, 1): True,
            date(2023, 6, 8): True,
            date(2023, 9, 7): True,
            date(2023, 10, 12): True,
            date(2023, 11, 2): True,
            date(2023, 11, 15): True,
            date(2023, 12, 25): True,
            date(2023, 12, 31): True,
            date(2023, 12, 26): False,
            # 2024
            date(2024, 1, 1): True,
            date(2024, 2, 12): True,
            date(2024, 2, 13): True,
            date(2024, 3, 29): True,
            date(2024, 4, 21): True,
            date(2024, 5, 1): True,
            date(2024, 5, 30): True,
            date(2024, 9, 7): True,
            date(2024, 10, 12): True,
            date(2024, 11, 2): True,
            date(2024, 11, 15): True,
            date(2024, 12, 25): True,
            date(2024, 12, 31): True,
            date(2024, 12, 26): False,
            # 2025
            date(2025, 1, 1): True,
            date(2025, 3, 3): True,
            date(2025, 3, 4): True,
            date(2025, 4, 18): True,
            date(2025, 4, 21): True,
            date(2025, 5, 1): True,
            date(2025, 6, 19): True,
            date(2025, 9, 7): True,
            date(2025, 10, 12): True,
            date(2025, 11, 2): True,
            date(2025, 11, 15): True,
            date(2025, 12, 25): True,
            date(2025, 12, 31): True,
            date(2025, 12, 26): False,
        }

    def test_b3_all_holidays(self):
        for holiday in self.all_holidays.items():
            if holiday[1]:
                self.assertTrue(self.holidays.is_date_holiday(holiday[0]))
            else:
                self.assertFalse(self.holidays.is_date_holiday(holiday[0]))

    def test_b3_first_day_year_is_holiday(self):
        get_date = date(2020, 1, 1)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_b3_random_date_is_not_holiday(self):
        get_date = date(2020, 1, 10)
        self.assertFalse(self.holidays.is_date_holiday(get_date))

    def test_b3_holidays_2020(self):
        year = 2020
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 14)

    def test_b3_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 15)

    def test_b3_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 13)

    def test_b3_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 13)

    def test_b3_holidays_2024(self):
        year = 2024
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 13)

    def test_b3_holidays_2025(self):
        year = 2025
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 13)


class TestHolidays(TestCase):

    def test_holidays_without_exchange(self):
        holidays = Holidays()
        self.assertEqual(len(holidays.get_holidays()), 0)
        self.assertEqual(len(holidays.get_holidays_by_year(2020)), 0)
        self.assertFalse(holidays.is_date_holiday(date(2020, 1, 1)))


class TestSSE(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=SSE())
        self.sse_holidays = self.holidays.get_holidays()

        self.all_holidays = {
            # 2020
            date(2020, 1, 1): True,
            date(2020, 1, 24): True,
            date(2020, 1, 27): True,
            date(2020, 1, 28): True,
            date(2020, 1, 29): True,
            date(2020, 1, 30): True,
            date(2020, 4, 6): True,
            date(2020, 5, 1): True,
            date(2020, 5, 4): True,
            date(2020, 5, 5): True,
            date(2020, 6, 25): True,
            date(2020, 6, 26): True,
            date(2020, 10, 1): True,
            date(2020, 10, 2): True,
            date(2020, 10, 5): True,
            date(2020, 10, 6): True,
            date(2020, 10, 7): True,
            date(2020, 10, 8): True,
            date(2020, 12, 25): False,
            # 2021
            date(2021, 1, 1): True,
            date(2021, 2, 11): True,
            date(2021, 2, 12): True,
            date(2021, 2, 15): True,
            date(2021, 2, 16): True,
            date(2021, 2, 17): True,
            date(2021, 4, 5): True,
            date(2021, 5, 1): True,
            date(2021, 5, 3): True,
            date(2021, 5, 4): True,
            date(2021, 5, 5): True,
            date(2021, 6, 14): True,
            date(2021, 9, 20): True,
            date(2021, 9, 21): True,
            date(2021, 10, 1): True,
            date(2021, 10, 4): True,
            date(2021, 10, 5): True,
            date(2021, 10, 6): True,
            date(2021, 10, 7): True,
            # 2022
            date(2022, 1, 1): True,
            date(2022, 1, 3): True,
            date(2022, 1, 31): True,
            date(2022, 2, 1): True,
            date(2022, 2, 2): True,
            date(2022, 2, 3): True,
            date(2022, 2, 4): True,
            date(2022, 4, 4): True,
            date(2022, 4, 5): True,
            date(2022, 5, 2): True,
            date(2022, 5, 3): True,
            date(2022, 5, 4): True,
            date(2022, 6, 3): True,
            date(2022, 9, 12): True,
            date(2022, 10, 3): True,
            date(2022, 10, 4): True,
            date(2022, 10, 5): True,
            date(2022, 10, 6): True,
            date(2022, 10, 7): True,
            # 2023
            date(2023, 1, 1): True,
            date(2023, 1, 2): True,
            date(2023, 1, 23): True,
            date(2023, 1, 24): True,
            date(2023, 1, 25): True,
            date(2023, 1, 26): True,
            date(2023, 1, 27): True,
            date(2023, 4, 5): True,
            date(2023, 5, 1): True,
            date(2023, 5, 2): True,
            date(2023, 5, 3): True,
            date(2023, 6, 22): True,
            date(2023, 6, 23): True,
            date(2023, 9, 29): True,
            date(2023, 10, 2): True,
            date(2023, 10, 3): True,
            date(2023, 10, 4): True,
            date(2023, 10, 5): True,
            date(2023, 10, 6): True,
            # 2024
            date(2024, 1, 1): True,
            date(2024, 2, 10): True,
            date(2024, 2, 11): True,
            date(2024, 2, 12): True,
            date(2024, 2, 13): True,
            date(2024, 2, 14): True,
            date(2024, 4, 4): True,
            date(2024, 4, 5): True,
            date(2024, 5, 1): True,
            date(2024, 5, 2): True,
            date(2024, 5, 3): True,
            date(2024, 6, 10): True,
            date(2024, 9, 17): True,
            date(2024, 10, 1): True,
            date(2024, 10, 2): True,
            date(2024, 10, 3): True,
            date(2024, 10, 4): True,
            date(2024, 10, 7): True,
            # 2025
            date(2025, 1, 1): True,
            date(2025, 1, 29): True,
            date(2025, 1, 30): True,
            date(2025, 1, 31): True,
            date(2025, 2, 3): True,
            date(2025, 2, 4): True,
            date(2025, 4, 4): True,
            date(2025, 5, 1): True,
            date(2025, 5, 2): True,
            date(2025, 5, 5): True,
            date(2025, 5, 31): True,
            date(2025, 10, 1): True,
            date(2025, 10, 2): True,
            date(2025, 10, 3): True,
            date(2025, 10, 6): True,
            date(2025, 10, 7): True,
        }

    def test_sse_all_holidays(self):
        for holiday in self.all_holidays.items():
            if holiday[1]:
                self.assertTrue(self.holidays.is_date_holiday(holiday[0]))
            else:
                self.assertFalse(self.holidays.is_date_holiday(holiday[0]))

    def test_sse_first_day_year_is_holiday(self):
        get_date = date(2020, 1, 1)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_sse_chinese_new_year_is_holiday(self):
        get_date = date(2024, 2, 10)  # Ano do Dragão
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_sse_random_date_is_not_holiday(self):
        get_date = date(2020, 3, 10)
        self.assertFalse(self.holidays.is_date_holiday(get_date))

    def test_sse_holidays_2020(self):
        year = 2020
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 18)

    def test_sse_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 19)

    def test_sse_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 19)

    def test_sse_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 19)

    def test_sse_holidays_2024(self):
        year = 2024
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 18)

    def test_sse_holidays_2025(self):
        year = 2025
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 16)


class TestJPX(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=JPX())
        self.jpx_holidays = self.holidays.get_holidays()

        self.all_holidays = {
            # 2020 - Sample dates
            date(2020, 1, 1): True,
            date(2020, 1, 2): True,
            date(2020, 1, 3): True,
            date(2020, 2, 24): True,
            date(2020, 4, 29): True,
            date(2020, 5, 4): True,
            date(2020, 7, 23): True,
            date(2020, 8, 10): True,
            date(2020, 9, 21): True,
            date(2020, 11, 3): True,
            date(2020, 12, 31): True,
            date(2020, 12, 25): False,
            # 2024 - Sample dates with observed holidays
            date(2024, 1, 1): True,
            date(2024, 1, 2): True,
            date(2024, 1, 3): True,
            date(2024, 2, 11): True,
            date(2024, 2, 12): True,  # Observed
            date(2024, 5, 5): True,
            date(2024, 5, 6): True,  # Observed
            date(2024, 8, 11): True,
            date(2024, 8, 12): True,  # Observed
            date(2024, 9, 22): True,
            date(2024, 9, 23): True,  # Observed
            date(2024, 11, 3): True,
            date(2024, 11, 4): True,  # Observed
            date(2024, 12, 31): True,
            # 2025 - Sample dates
            date(2025, 1, 1): True,
            date(2025, 2, 23): True,
            date(2025, 2, 24): True,  # Observed
            date(2025, 5, 5): True,
            date(2025, 5, 6): True,  # Observed
            date(2025, 11, 23): True,
            date(2025, 11, 24): True,  # Observed
            date(2025, 12, 31): True,
        }

    def test_jpx_all_holidays(self):
        for holiday in self.all_holidays.items():
            if holiday[1]:
                self.assertTrue(self.holidays.is_date_holiday(holiday[0]))
            else:
                self.assertFalse(self.holidays.is_date_holiday(holiday[0]))

    def test_jpx_new_years_holidays(self):
        get_date = date(2024, 1, 2)
        self.assertTrue(self.holidays.is_date_holiday(get_date))
        get_date = date(2024, 1, 3)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_jpx_emperors_birthday(self):
        get_date = date(2024, 2, 23)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_jpx_random_date_is_not_holiday(self):
        get_date = date(2024, 3, 1)
        self.assertFalse(self.holidays.is_date_holiday(get_date))

    def test_jpx_holidays_2020(self):
        year = 2020
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 19)

    def test_jpx_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 20)

    def test_jpx_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 18)

    def test_jpx_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 19)

    def test_jpx_holidays_2024(self):
        year = 2024
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 24)

    def test_jpx_holidays_2025(self):
        year = 2025
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 22)
