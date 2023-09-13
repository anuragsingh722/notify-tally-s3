import json
import unittest

from motoezzy import Motoezzy


class TestMotoezzy(unittest.TestCase):
    def test_auth(self):
        motoezzy = Motoezzy()
        print(motoezzy.invoice_upload_notification(bucket="BKT", file_path="FPTH"))


if __name__ == '__main__':
    unittest.main()
