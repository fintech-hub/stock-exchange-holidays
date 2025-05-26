# Stock Exchange Holidays

A Python module for managing stock exchange holidays for major exchanges worldwide.

## Supported Exchanges

- **NYSE** (New York Stock Exchange)
- **CME** (Chicago Mercantile Exchange)
- **B3** (Brazilian Stock Exchange)
- **SSE** (Shanghai Stock Exchange)
- **JPX** (Japan Exchange Group - Tokyo Stock Exchange)

## Features

- Holiday management for years 2020-2025
- Optimized data structures for O(1) holiday lookups
- LRU cache for frequently accessed years
- Type hints for better IDE support
- Comprehensive test coverage

## Installation

```bash
pip install stock-exchange-holidays
```

## Usage

```python
from datetime import date
from stock.stock_exchange_holidays import Holidays, NYSE, CME, B3, SSE, JPX

# Initialize with desired exchange
nyse_holidays = Holidays(exchange=NYSE())
b3_holidays = Holidays(exchange=B3())
cme_holidays = Holidays(exchange=CME())
sse_holidays = Holidays(exchange=SSE())
jpx_holidays = Holidays(exchange=JPX())

# Check if a date is a holiday
is_holiday = nyse_holidays.is_date_holiday(date(2024, 1, 1))  # True (New Year's Day)

# Get all holidays for a specific year
holidays_2024 = b3_holidays.get_holidays_by_year(2024)

# Get all holidays
all_holidays = cme_holidays.get_holidays()
```

## Holiday Count by Exchange (2024)

- NYSE: 11 holidays
- CME: 11 holidays
- B3: 13 holidays
- SSE: 18 holidays
- JPX: 24 holidays (including observed holidays)

## Major Holidays by Exchange

### NYSE & CME
- New Year's Day
- Martin Luther King Jr. Day
- Presidents' Day
- Good Friday
- Memorial Day
- Juneteenth National Independence Day
- Independence Day
- Labor Day
- Thanksgiving Day
- Christmas Day

### B3 (Brazil)
- New Year's Day
- Carnival (Monday and Tuesday)
- Good Friday
- Tiradentes Day
- Labor Day
- Corpus Christi
- Independence Day
- Our Lady of Aparecida
- All Souls' Day
- Republic Day
- Christmas Day

### SSE (China)
- New Year's Day
- Chinese New Year (multiple days)
- Qingming Festival
- Labor Day
- Dragon Boat Festival
- Mid-Autumn Festival
- National Day (multiple days)

### JPX (Japan)
- New Year's Day (January 1-3)
- Coming of Age Day
- National Foundation Day
- Emperor's Birthday
- Vernal Equinox Day
- Showa Day
- Constitution Memorial Day
- Greenery Day
- Children's Day
- Marine Day
- Mountain Day
- Respect for the Aged Day
- Autumnal Equinox Day
- Health and Sports Day
- Culture Day
- Labor Thanksgiving Day
- New Year's Eve

## Performance

The module uses optimized data structures for efficient holiday lookups:
- Holiday lookup: O(1)
- Year-based holiday retrieval: O(1) with LRU cache
- Memory-efficient storage using sets and dictionaries

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Data Sources

- NYSE: https://www.nyse.com/markets/hours-calendars
- CME: https://www.cmegroup.com/tools-information/holiday-calendar.html
- B3: http://www.b3.com.br
- SSE: http://www.sse.com.cn/
- JPX: https://www.jpx.co.jp/english/corporate/about-jpx/calendar/
