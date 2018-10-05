import unittest
from arrow import utcnow

from helpers import _run
from write_to_sys import default_to_uk_time


class DefaultToUkTime(unittest.TestCase):
    def test_default_uk_time(self):
        self.assertEqual(
            _run(default_to_uk_time()),
            utcnow().to('Europe/London').format("MMM DD YYYY HH:mm:ss"),
            msg="Time defaults to London with correct format"
        )

    def test_fail_default_uk_time(self):
        us_time = utcnow().to('US/Pacific').format("MMM DD YYYY HH:mm:ss")
        self.assertNotEqual(
            _run(default_to_uk_time()),
            utcnow().to('US/Pacific').format("MMM DD YYYY HH:mm:ss"),
            msg=f'time: {us_time}'
        )

    def test_different_time(self):
        us_time = utcnow().to('US/Pacific').format("MMM DD YYYY HH:mm:ss")
        self.assertEqual(
            _run(default_to_uk_time('US/Pacific')),
            utcnow().to('US/Pacific').format("MMM DD YYYY HH:mm:ss"),
            msg=f'time: {us_time}'
        )


if __name__ == '__main__':
    unittest.main()