from unittest import TestCase

from quantz.utils import *


class TestMiscUtils(TestCase):
    def test_date_2_str(self):
        today = datetime.datetime.today()
        print(date_2_str(today))

    def test_today_date(self):
        print(today_datetime())

    def test_generate_last_season(self):
        print(generate_latest_report_period())
