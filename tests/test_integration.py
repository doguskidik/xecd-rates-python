from xecd_rates import Xecd
import unittest


class XecdIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.xecd = Xecd()

    def testConvertFrom(self):
        response = self.xecd.convert_from(cfrom='TRY', cto=['EUR', 'USD'])
        self.assertIn('from', response)
        self.assertIn('timestamp', response)
        self.assertIn('to', response)

    def testHistoricRate(self):
        response = self.xecd.historic_rate(cdate='2020-01-01', cfrom='TRY', cto=['EUR', 'USD'])
        self.assertIn('from', response)
        self.assertIn('timestamp', response)
        self.assertIn('to', response)

    def testHistoricRatePeriod(self):
        response = self.xecd.historic_rate_period(sdate='2020-01-01', edate='2020-01-05', cfrom='TRY',
                                                  cto=['EUR', 'USD'])
        self.assertIn('from', response)
        self.assertIn('to', response)
