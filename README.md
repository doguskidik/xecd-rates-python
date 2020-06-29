![image](https://raw.githubusercontent.com/doguskidik/xecd-rates-python/master/logo.jpg)

-----------------
# Xecd Rates Python: Free currency  rates converter
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI Latest Release](https://img.shields.io/pypi/v/xecd-rates.svg)](https://pypi.org/project/xecd-rates/)
[![PyPI license](https://img.shields.io/pypi/l/xecd-rates.svg)](https://pypi.python.org/pypi/xecd-rates/)
[![PyPI format](https://img.shields.io/pypi/format/xecd-rates.svg)](https://pypi.python.org/pypi/xecd-rates/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/xecd-rates.svg)](https://pypi.python.org/pypi/xecd-rates/)
## What is it?
This project is free version of  XE Currency Data (XECD) product.

Xecd-Rates-Python librariy gives you access to daily or live rates and historic mid-market conversion rates between all of our supported currencies.

You can access the paid version of this project via this [link.](https://www.xe.com/)
## Where to get it

The preferred way to install this package is pip.

```
pip install xecd-rates
```

Or get the latest version from git:
```
pip install git+https://github.com/doguskidik/xecd-rates-python.git
```
## Dependencies
- [requests](https://github.com/psf/requests)
- [lxml](https://lxml.de/)
## Usage

```python
>>> from xecd_rates import Xecd
>>> xecd = Xecd()

>>> xecd.available_currencies
{'AFN': 'Afghan Afghani', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 'ANG': 'Dutch Guilder', 'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 'AWG': 'Aruban or Dutch Guilder', 'AZN': 'Azerbaijan Manat', 'BAM': 'Bosnian Convertible Mark', 'BBD': 'Barbadian or Bajan Dollar', 'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgarian Lev', 'BHD': 'Bahraini Dinar', 'BIF': 'Burundian Franc', 'BMD': 'Bermudian Dollar', 'BND': 'Bruneian Dollar', 'BOB': 'Bolivian Bolíviano', 'BRL': 'Brazilian Real', 'BSD': 'Bahamian Dollar', 'BTN': 'Bhutanese Ngultrum', 'BWP': 'Botswana Pula', 'BYN': 'Belarusian Ruble', 'BZD': 'Belizean Dollar', 'CAD': 'Canadian Dollar', 'CDF': 'Congolese Franc', 'CHF': 'Swiss Franc', 'CLP': 'Chilean Peso', 'CNY': 'Chinese Yuan Renminbi', 'COP': 'Colombian Peso', 'CRC': 'Costa Rican Colon', 'CUC': 'Cuban Convertible Peso', 'CUP': 'Cuban Peso', 'CVE': 'Cape Verdean Escudo', 'CZK': 'Czech Koruna', 'DJF': 'Djiboutian Franc', 'DKK': 'Danish Krone', 'DOP': 'Dominican Peso', 'DZD': 'Algerian Dinar', 'EGP': 'Egyptian Pound', 'ERN': 'Eritrean Nakfa', 'ETB': 'Ethiopian Birr', 'EUR': 'Euro', 'FJD': 'Fijian Dollar', 'FKP': 'Falkland Island Pound', 'GBP': 'British Pound', 'GEL': 'Georgian Lari', 'GGP': 'Guernsey Pound', 'GHS': 'Ghanaian Cedi', 'GIP': 'Gibraltar Pound', 'GMD': 'Gambian Dalasi', 'GNF': 'Guinean Franc', 'GTQ': 'Guatemalan Quetzal', 'GYD': 'Guyanese Dollar', 'HKD': 'Hong Kong Dollar', 'HNL': 'Honduran Lempira', 'HRK': 'Croatian Kuna', 'HTG': 'Haitian Gourde', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah', 'ILS': 'Israeli Shekel', 'IMP': 'Isle of Man Pound', 'INR': 'Indian Rupee', 'IQD': 'Iraqi Dinar', 'IRR': 'Iranian Rial', 'ISK': 'Icelandic Krona', 'JEP': 'Jersey Pound', 'JMD': 'Jamaican Dollar', 'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shilling', 'KGS': 'Kyrgyzstani Som', 'KHR': 'Cambodian Riel', 'KMF': 'Comorian Franc', 'KPW': 'North Korean Won', 'KRW': 'South Korean Won', 'KWD': 'Kuwaiti Dinar', 'KYD': 'Caymanian Dollar', 'KZT': 'Kazakhstani Tenge', 'LAK': 'Lao Kip', 'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'LRD': 'Liberian Dollar', 'LSL': 'Basotho Loti', 'LYD': 'Libyan Dinar', 'MAD': 'Moroccan Dirham', 'MDL': 'Moldovan Leu', 'MGA': 'Malagasy Ariary', 'MKD': 'Macedonian Denar', 'MMK': 'Burmese Kyat', 'MNT': 'Mongolian Tughrik', 'MOP': 'Macau Pataca', 'MRU': 'Mauritanian Ouguiya', 'MUR': 'Mauritian Rupee', 'MVR': 'Maldivian Rufiyaa', 'MWK': 'Malawian Kwacha', 'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'MZN': 'Mozambican Metical', 'NAD': 'Namibian Dollar', 'NGN': 'Nigerian Naira', 'NIO': 'Nicaraguan Cordoba', 'NOK': 'Norwegian Krone', 'NPR': 'Nepalese Rupee', 'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PAB': 'Panamanian Balboa', 'PEN': 'Peruvian Sol', 'PGK': 'Papua New Guinean Kina', 'PHP': 'Philippine Peso', 'PKR': 'Pakistani Rupee', 'PLN': 'Polish Zloty', 'PYG': 'Paraguayan Guarani', 'QAR': 'Qatari Riyal', 'RON': 'Romanian Leu', 'RSD': 'Serbian Dinar', 'RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc', 'SAR': 'Saudi Arabian Riyal', 'SBD': 'Solomon Islander Dollar', 'SCR': 'Seychellois Rupee', 'SDG': 'Sudanese Pound', 'SEK': 'Swedish Krona', 'SGD': 'Singapore Dollar', 'SHP': 'Saint Helenian Pound', 'SLL': 'Sierra Leonean Leone', 'SOS': 'Somali Shilling', 'SPL': 'Seborgan Luigino', 'SRD': 'Surinamese Dollar', 'STN': 'Sao Tomean Dobra', 'SVC': 'Salvadoran Colon', 'SYP': 'Syrian Pound', 'SZL': 'Swazi Lilangeni', 'THB': 'Thai Baht', 'TJS': 'Tajikistani Somoni', 'TMT': 'Turkmenistani Manat', 'TND': 'Tunisian Dinar', 'TOP': "Tongan Pa'anga", 'TRY': 'Turkish Lira', 'TTD': 'Trinidadian Dollar', 'TVD': 'Tuvaluan Dollar', 'TWD': 'Taiwan New Dollar', 'TZS': 'Tanzanian Shilling', 'UAH': 'Ukrainian Hryvnia', 'UGX': 'Ugandan Shilling', 'USD': 'US Dollar', 'UYU': 'Uruguayan Peso', 'UZS': 'Uzbekistani Som', 'VEF': 'Venezuelan Bolívar', 'VES': 'Venezuelan Bolívar', 'VND': 'Vietnamese Dong', 'VUV': 'Ni', 'WST': 'Samoan Tala', 'XAF': 'Central African CFA Franc BEAC', 'XAG': 'Silver Ounce', 'XAU': 'Gold Ounce', 'XBT': 'Bitcoin', 'XCD': 'East Caribbean Dollar', 'XDR': 'IMF Special Drawing Rights', 'XOF': 'CFA Franc', 'XPD': 'Palladium Ounce', 'XPF': 'CFP Franc', 'XPT': 'Platinum Ounce', 'YER': 'Yemeni Rial', 'ZAR': 'South African Rand'}

>>> xecd.convert_from(cfrom='TRY', cto=['EUR','USD']) 
{'timestamp': '2020-06-29 12:38 UTC', 'from': 'TRY', 'to': [{'quotecurrency': 'USD', 'mid': '0.1458731540'}, {'quotecurrency': 'EUR', 'mid': '0.1293255181'}]}

>>> xecd.historic_rate(cdate='2020-01-01', cfrom='TRY', cto=['EUR','USD']) 
{'timestamp': '2020-01-01 17:00 UTC', 'from': 'TRY', 'to': [{'quotecurrency': 'USD', 'mid': '0.1681044260'}, {'quotecurrency': 'EUR', 'mid': '0.1501472598'}]}

>>> xecd.historic_rate_period(sdate='2020-01-01', edate='2020-01-05', cfrom='TRY', cto=['EUR','USD'])
{'from': 'TRY', 'to': {'USD': [{'mid': '0.1678214515', 'timestamp': '2020-01-02 17:00 UTC'}, {'mid': '0.1673405691', 'timestamp': '2020-01-03 17:00 UTC'}, {'mid': '0.1673821113', 'timestamp': '2020-01-04 17:00 UTC'}, {'mid': '0.1673821113', 'timestamp': '2020-01-04 17:00 UTC'}, {'mid': '0.1674115622', 'timestamp': '2020-01-05 17:00 UTC'}], 'EUR': [{'mid': '0.1502682495', 'timestamp': '2020-01-02 17:00 UTC'}, {'mid': '0.1497847442', 'timestamp': '2020-01-03 17:00 UTC'}, {'mid': '0.1499997714', 'timestamp': '2020-01-04 17:00 UTC'}, {'mid': '0.1499997714', 'timestamp': '2020-01-04 17:00 UTC'}, {'mid': '0.1499838691', 'timestamp': '2020-01-05 17:00 UTC'}]}}

```
## Available Currencies

| Currency Code  | Description         |
| :---: | :------------------------------: |
| AFN | Afghan Afghani                 |
| ALL | Albanian Lek                   |
| AMD | Armenian Dram                  |
| ANG | Dutch Guilder                  |
| AOA | Angolan Kwanza                 |
| ARS | Argentine Peso                 |
| AUD | Australian Dollar              |
| AWG | Aruban or Dutch Guilder        |
| AZN | Azerbaijan Manat               |
| BAM | Bosnian Convertible Mark       |
| BBD | Barbadian or Bajan Dollar      |
| BDT | Bangladeshi Taka               |
| BGN | Bulgarian Lev                  |
| BHD | Bahraini Dinar                 |
| BIF | Burundian Franc                |
| BMD | Bermudian Dollar               |
| BND | Bruneian Dollar                |
| BOB | Bolivian Bolíviano             |
| BRL | Brazilian Real                 |
| BSD | Bahamian Dollar                |
| BTN | Bhutanese Ngultrum             |
| BWP | Botswana Pula                  |
| BYN | Belarusian Ruble               |
| BZD | Belizean Dollar                |
| CAD | Canadian Dollar                |
| CDF | Congolese Franc                |
| CHF | Swiss Franc                    |
| CLP | Chilean Peso                   |
| CNY | Chinese Yuan Renminbi          |
| COP | Colombian Peso                 |
| CRC | Costa Rican Colon              |
| CUC | Cuban Convertible Peso         |
| CUP | Cuban Peso                     |
| CVE | Cape Verdean Escudo            |
| CZK | Czech Koruna                   |
| DJF | Djiboutian Franc               |
| DKK | Danish Krone                   |
| DOP | Dominican Peso                 |
| DZD | Algerian Dinar                 |
| EGP | Egyptian Pound                 |
| ERN | Eritrean Nakfa                 |
| ETB | Ethiopian Birr                 |
| EUR | Euro                           |
| FJD | Fijian Dollar                  |
| FKP | Falkland Island Pound          |
| GBP | British Pound                  |
| GEL | Georgian Lari                  |
| GGP | Guernsey Pound                 |
| GHS | Ghanaian Cedi                  |
| GIP | Gibraltar Pound                |
| GMD | Gambian Dalasi                 |
| GNF | Guinean Franc                  |
| GTQ | Guatemalan Quetzal             |
| GYD | Guyanese Dollar                |
| HKD | Hong Kong Dollar               |
| HNL | Honduran Lempira               |
| HRK | Croatian Kuna                  |
| HTG | Haitian Gourde                 |
| HUF | Hungarian Forint               |
| IDR | Indonesian Rupiah              |
| ILS | Israeli Shekel                 |
| IMP | Isle of Man Pound              |
| INR | Indian Rupee                   |
| IQD | Iraqi Dinar                    |
| IRR | Iranian Rial                   |
| ISK | Icelandic Krona                |
| JEP | Jersey Pound                   |
| JMD | Jamaican Dollar                |
| JOD | Jordanian Dinar                |
| JPY | Japanese Yen                   |
| KES | Kenyan Shilling                |
| KGS | Kyrgyzstani Som                |
| KHR | Cambodian Riel                 |
| KMF | Comorian Franc                 |
| KPW | North Korean Won               |
| KRW | South Korean Won               |
| KWD | Kuwaiti Dinar                  |
| KYD | Caymanian Dollar               |
| KZT | Kazakhstani Tenge              |
| LAK | Lao Kip                        |
| LBP | Lebanese Pound                 |
| LKR | Sri Lankan Rupee               |
| LRD | Liberian Dollar                |
| LSL | Basotho Loti                   |
| LYD | Libyan Dinar                   |
| MAD | Moroccan Dirham                |
| MDL | Moldovan Leu                   |
| MGA | Malagasy Ariary                |
| MKD | Macedonian Denar               |
| MMK | Burmese Kyat                   |
| MNT | Mongolian Tughrik              |
| MOP | Macau Pataca                   |
| MRU | Mauritanian Ouguiya            |
| MUR | Mauritian Rupee                |
| MVR | Maldivian Rufiyaa              |
| MWK | Malawian Kwacha                |
| MXN | Mexican Peso                   |
| MYR | Malaysian Ringgit              |
| MZN | Mozambican Metical             |
| NAD | Namibian Dollar                |
| NGN | Nigerian Naira                 |
| NIO | Nicaraguan Cordoba             |
| NOK | Norwegian Krone                |
| NPR | Nepalese Rupee                 |
| NZD | New Zealand Dollar             |
| OMR | Omani Rial                     |
| PAB | Panamanian Balboa              |
| PEN | Peruvian Sol                   |
| PGK | Papua New Guinean Kina         |
| PHP | Philippine Peso                |
| PKR | Pakistani Rupee                |
| PLN | Polish Zloty                   |
| PYG | Paraguayan Guarani             |
| QAR | Qatari Riyal                   |
| RON | Romanian Leu                   |
| RSD | Serbian Dinar                  |
| RUB | Russian Ruble                  |
| RWF | Rwandan Franc                  |
| SAR | Saudi Arabian Riyal            |
| SBD | Solomon Islander Dollar        |
| SCR | Seychellois Rupee              |
| SDG | Sudanese Pound                 |
| SEK | Swedish Krona                  |
| SGD | Singapore Dollar               |
| SHP | Saint Helenian Pound           |
| SLL | Sierra Leonean Leone           |
| SOS | Somali Shilling                |
| SPL | Seborgan Luigino               |
| SRD | Surinamese Dollar              |
| STN | Sao Tomean Dobra               |
| SVC | Salvadoran Colon               |
| SYP | Syrian Pound                   |
| SZL | Swazi Lilangeni                |
| THB | Thai Baht                      |
| TJS | Tajikistani Somoni             |
| TMT | Turkmenistani Manat            |
| TND | Tunisian Dinar                 |
| TOP | Tongan Pa'anga                 |
| TRY | Turkish Lira                   |
| TTD | Trinidadian Dollar             |
| TVD | Tuvaluan Dollar                |
| TWD | Taiwan New Dollar              |
| TZS | Tanzanian Shilling             |
| UAH | Ukrainian Hryvnia              |
| UGX | Ugandan Shilling               |
| USD | US Dollar                      |
| UYU | Uruguayan Peso                 |
| UZS | Uzbekistani Som                |
| VEF | Venezuelan Bolívar             |
| VES | Venezuelan Bolívar             |
| VND | Vietnamese Dong                |
| VUV | Ni                             |
| WST | Samoan Tala                    |
| XAF | Central African CFA Franc BEAC |
| XAG | Silver Ounce                   |
| XAU | Gold Ounce                     |
| XBT | Bitcoin                        |
| XCD | East Caribbean Dollar          |
| XDR | IMF Special Drawing Rights     |
| XOF | CFA Franc                      |
| XPD | Palladium Ounce                |
| XPF | CFP Franc                      |
| XPT | Platinum Ounce                 |
| YER | Yemeni Rial                    |
| ZAR | South African Rand             |

## Contributing
xecd_rates_python is an open-source project. Submit a pull request to contribute!

## Testing
to run individual test suites
```bash
python -m unittest tests/test_integration.py
```