import unittest

from helpers import _run
from write_to_sys import log_to_file


class LogToFile(unittest.TestCase):
    def test_has_logged(self):
        content = {
            'file_name': 'test.py',
            'pid': '1',
            'func': 'test()',
            'process': 'INFO',
            'log': 'this is test'
        }
        self.assertTrue(
            _run(log_to_file(content))
        )


if __name__ == '__main__':
    unittest.main()