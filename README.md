![image](logo.jpg)

-----------------
# Xecd Rates Python: Free currency  rates converter
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI Latest Release](https://img.shields.io/pypi/v/xecd-rates.svg)](https://pypi.org/project/xecd-rates/)
[![PyPI license](https://img.shields.io/pypi/l/xecd-rates.svg)](https://pypi.python.org/pypi/xecd-rates/)
[![PyPI format](https://img.shields.io/pypi/format/xecd-rates.svg)](https://pypi.python.org/pypi/xecd-rates/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/xecd-rates.svg)](https://pypi.python.org/pypi/xecd-rates/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/doguskidik/xecd-rates/master/LICENSE)
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
from xecd_rates import Xecd

xecd = Xecd()

xecd.convert_from(cfrom='TRY', cto=['EUR','USD'])
{'timestamp': '2020-06-27 07:52 UTC', 'from': 'TRY', 'to': [{'quotecurrency': 'USD', 'mid': '0.1458842035'}, {'quotecurrency': 'EUR', 'mid': '0.1300239433'}]}

xecd.historic_rate(cdate='2020-01-01', cfrom='TRY', cto=['EUR','USD'])
{'timestamp': '2020-01-01 17:00 UTC', 'from': 'TRY', 'to': [{'quotecurrency': 'USD', 'mid': '0.1681044260'}, {'quotecurrency': 'EUR', 'mid': '0.1501472598'}]}

xecd.historic_rate_period(sdate='2020-01-01', edate='2020-01-05', cfrom='TRY', cto=['EUR','USD'])
{'from': 'TRY', 'to': {'USD': [{'mid': '0.1678214515', 'timestamp': '2020-01-02 17:00 UTC'}, {'mid': '0.1673405691', 'timestamp': '2020-01-03 17:00 UTC'}, {'mid': '0.1673821113', 'timestamp': '2020-01-04 17:00 UTC'}, {'mid': '0.1673821113', 'timestamp': '2020-01-04 17:00 UTC'}, {'mid': '0.1674115622', 'timestamp': '2020-01-05 17:00 UTC'}], 'EUR': [{'mid': '0.1502682495', 'timestamp': '2020-01-02 17:00 UTC'}, {'mid': '0.1497847442', 'timestamp': '2020-01-03 17:00 UTC'}, {'mid': '0.1499997714', 'timestamp': '2020-01-04 17:00 UTC'}, {'mid': '0.1499997714', 'timestamp': '2020-01-04 17:00 UTC'}, {'mid': '0.1499838691', 'timestamp': '2020-01-05 17:00 UTC'}]}}

```
## Contributing
xecd_rates_python is an open-source project. Submit a pull request to contribute!