import lxml.html
import requests
import datetime
import concurrent.futures
import functools


class Xecd(object):

    def __init__(self):
        self.base_url = 'https://www.xe.com/currencytables/'
        self.params = {'from': '', 'date': ''}
        self.table_xpath = '//table[ @id ="historicalRateTbl"]'
        self.timestamp_xpath = '//p[@class ="historicalRateTable-date"]/text()'
        self.cfrom_xpath = '//option[@selected ="selected"]/@value'
        self.cvalues_xpath = './tbody/tr/td//text()'

        self.available_currencies = {"AFN": "Afghan Afghani", "ALL": "Albanian Lek", "AMD": "Armenian Dram",
                                     "ANG": "Dutch Guilder", "AOA": "Angolan Kwanza", "ARS": "Argentine Peso",
                                     "AUD": "Australian Dollar", "AWG": "Aruban or Dutch Guilder",
                                     "AZN": "Azerbaijan Manat",
                                     "BAM": "Bosnian Convertible Mark", "BBD": "Barbadian or Bajan Dollar",
                                     "BDT": "Bangladeshi Taka",
                                     "BGN": "Bulgarian Lev", "BHD": "Bahraini Dinar", "BIF": "Burundian Franc",
                                     "BMD": "Bermudian Dollar", "BND": "Bruneian Dollar", "BOB": "Bolivian Bolíviano",
                                     "BRL": "Brazilian Real", "BSD": "Bahamian Dollar", "BTN": "Bhutanese Ngultrum",
                                     "BWP": "Botswana Pula", "BYN": "Belarusian Ruble", "BZD": "Belizean Dollar",
                                     "CAD": "Canadian Dollar", "CDF": "Congolese Franc", "CHF": "Swiss Franc",
                                     "CLP": "Chilean Peso", "CNY": "Chinese Yuan Renminbi", "COP": "Colombian Peso",
                                     "CRC": "Costa Rican Colon", "CUC": "Cuban Convertible Peso", "CUP": "Cuban Peso",
                                     "CVE": "Cape Verdean Escudo", "CZK": "Czech Koruna", "DJF": "Djiboutian Franc",
                                     "DKK": "Danish Krone", "DOP": "Dominican Peso", "DZD": "Algerian Dinar",
                                     "EGP": "Egyptian Pound", "ERN": "Eritrean Nakfa", "ETB": "Ethiopian Birr",
                                     "EUR": "Euro", "FJD": "Fijian Dollar", "FKP": "Falkland Island Pound",
                                     "GBP": "British Pound", "GEL": "Georgian Lari", "GGP": "Guernsey Pound",
                                     "GHS": "Ghanaian Cedi", "GIP": "Gibraltar Pound", "GMD": "Gambian Dalasi",
                                     "GNF": "Guinean Franc", "GTQ": "Guatemalan Quetzal", "GYD": "Guyanese Dollar",
                                     "HKD": "Hong Kong Dollar", "HNL": "Honduran Lempira", "HRK": "Croatian Kuna",
                                     "HTG": "Haitian Gourde", "HUF": "Hungarian Forint", "IDR": "Indonesian Rupiah",
                                     "ILS": "Israeli Shekel", "IMP": "Isle of Man Pound", "INR": "Indian Rupee",
                                     "IQD": "Iraqi Dinar", "IRR": "Iranian Rial", "ISK": "Icelandic Krona",
                                     "JEP": "Jersey Pound", "JMD": "Jamaican Dollar", "JOD": "Jordanian Dinar",
                                     "JPY": "Japanese Yen", "KES": "Kenyan Shilling", "KGS": "Kyrgyzstani Som",
                                     "KHR": "Cambodian Riel", "KMF": "Comorian Franc", "KPW": "North Korean Won",
                                     "KRW": "South Korean Won", "KWD": "Kuwaiti Dinar", "KYD": "Caymanian Dollar",
                                     "KZT": "Kazakhstani Tenge", "LAK": "Lao Kip", "LBP": "Lebanese Pound",
                                     "LKR": "Sri Lankan Rupee", "LRD": "Liberian Dollar", "LSL": "Basotho Loti",
                                     "LYD": "Libyan Dinar", "MAD": "Moroccan Dirham", "MDL": "Moldovan Leu",
                                     "MGA": "Malagasy Ariary", "MKD": "Macedonian Denar", "MMK": "Burmese Kyat",
                                     "MNT": "Mongolian Tughrik", "MOP": "Macau Pataca", "MRU": "Mauritanian Ouguiya",
                                     "MUR": "Mauritian Rupee", "MVR": "Maldivian Rufiyaa", "MWK": "Malawian Kwacha",
                                     "MXN": "Mexican Peso", "MYR": "Malaysian Ringgit", "MZN": "Mozambican Metical",
                                     "NAD": "Namibian Dollar", "NGN": "Nigerian Naira", "NIO": "Nicaraguan Cordoba",
                                     "NOK": "Norwegian Krone", "NPR": "Nepalese Rupee", "NZD": "New Zealand Dollar",
                                     "OMR": "Omani Rial", "PAB": "Panamanian Balboa", "PEN": "Peruvian Sol",
                                     "PGK": "Papua New Guinean Kina", "PHP": "Philippine Peso",
                                     "PKR": "Pakistani Rupee",
                                     "PLN": "Polish Zloty", "PYG": "Paraguayan Guarani", "QAR": "Qatari Riyal",
                                     "RON": "Romanian Leu", "RSD": "Serbian Dinar", "RUB": "Russian Ruble",
                                     "RWF": "Rwandan Franc", "SAR": "Saudi Arabian Riyal",
                                     "SBD": "Solomon Islander Dollar",
                                     "SCR": "Seychellois Rupee", "SDG": "Sudanese Pound", "SEK": "Swedish Krona",
                                     "SGD": "Singapore Dollar", "SHP": "Saint Helenian Pound",
                                     "SLL": "Sierra Leonean Leone",
                                     "SOS": "Somali Shilling", "SPL": "Seborgan Luigino", "SRD": "Surinamese Dollar",
                                     "STN": "Sao Tomean Dobra", "SVC": "Salvadoran Colon", "SYP": "Syrian Pound",
                                     "SZL": "Swazi Lilangeni", "THB": "Thai Baht", "TJS": "Tajikistani Somoni",
                                     "TMT": "Turkmenistani Manat", "TND": "Tunisian Dinar", "TOP": "Tongan Pa'anga",
                                     "TRY": "Turkish Lira", "TTD": "Trinidadian Dollar", "TVD": "Tuvaluan Dollar",
                                     "TWD": "Taiwan New Dollar", "TZS": "Tanzanian Shilling",
                                     "UAH": "Ukrainian Hryvnia",
                                     "UGX": "Ugandan Shilling", "USD": "US Dollar", "UYU": "Uruguayan Peso",
                                     "UZS": "Uzbekistani Som", "VEF": "Venezuelan Bolívar", "VES": "Venezuelan Bolívar",
                                     "VND": "Vietnamese Dong", "VUV": "Ni", "WST": "Samoan Tala",
                                     "XAF": "Central African CFA Franc BEAC", "XAG": "Silver Ounce",
                                     "XAU": "Gold Ounce",
                                     "XBT": "Bitcoin", "XCD": "East Caribbean Dollar",
                                     "XDR": "IMF Special Drawing Rights",
                                     "XOF": "CFA Franc", "XPD": "Palladium Ounce", "XPF": "CFP Franc",
                                     "XPT": "Platinum Ounce", "YER": "Yemeni Rial", "ZAR": "South African Rand"}

    def _check_currency(self,ccode):
        if ccode not in self.available_currencies.keys():
            raise Exception('invalid currencies')

    def _check_date(self,cdate):
        if cdate not in self.available_currencies.keys():
            raise Exception('invalid currencies')

    def _get_html(self, cfrom, cdate):
        params = self.params
        params['from'] = cfrom
        params['date'] = cdate

        return requests.get(url=self.base_url, params=params).content

    def _parse_html(self, html):
        root = lxml.html.fromstring(html)
        timestamp = root.xpath(self.timestamp_xpath)[0]
        _from = root.xpath(self.cfrom_xpath)[0]
        table = root.xpath(self.table_xpath)[0]

        currency_rates = table.xpath(self.cvalues_xpath)
        currency_rates = [currency_rates[i:i + 4] for i in range(0, len(currency_rates), 4)]

        results = dict()
        results['timestamp'] = timestamp
        results['from'] = _from
        results['to'] = [{'quotecurrency': val[0], 'mid': val[2]} for val in currency_rates]

        return results

    def _filter_results(self, results, flt):
        if flt == 'all':
            return results

        to = []
        for i, result in enumerate(results['to']):
            if result['quotecurrency'] in flt:
                to.append(results['to'][i])

        results['to'] = to
        return results

    def _date_range(self, sdate, edate):
        sdate = datetime.datetime.strptime(sdate, '%Y-%m-%d')
        edate = datetime.datetime.strptime(edate, '%Y-%m-%d')
        delta = edate - sdate
        for date in range(delta.days + 1):
            day = (sdate + datetime.timedelta(days=date)).date()
            yield day

    def convert_from(self, cfrom, cto):
        self._check_currency(cfrom)
        html = self._get_html(cfrom, cdate='')
        results = self._parse_html(html)
        results = self._filter_results(results=results, flt=cto)
        return results

    def historic_rate(self, cdate, cfrom, cto):
        html = self._get_html(cfrom, cdate)
        results = self._parse_html(html)
        results = self._filter_results(results=results, flt=cto)
        return results

    def historic_rate_period(self, cfrom, cto, sdate, edate):
        days = self._date_range(sdate, edate)
        f = functools.partial(self.historic_rate, cfrom=cfrom, cto=cto)

        with concurrent.futures.ThreadPoolExecutor(4) as executor:
            _results = list(executor.map(f, days))

        results = {}
        results['from'] = _results[0]['from']
        results['to'] = {}

        for result in _results:
            for currencey in result['to']:
                try:
                    results['to'][currencey['quotecurrency']].append(
                        {'mid': currencey['mid'], 'timestamp': result['timestamp']})
                except:
                    results['to'][currencey['quotecurrency']] = [
                        {'mid': currencey['mid'], 'timestamp': result['timestamp']}]

        return results
