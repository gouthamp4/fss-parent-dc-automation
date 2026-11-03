import unittest

from automation import connection_plan


class InventoryTests(unittest.TestCase):
    def device(self, **changes):
        return {"name": "switch-01", "address": "192.0.2.10", "platform": "example", **changes}

    def test_valid_device_plan(self):
        self.assertEqual(connection_plan({"devices": [self.device()]}),
                         ["switch-01: 192.0.2.10 port 22 (example)"])

    def test_invalid_inventory(self):
        for inventory in (None, {}, {"devices": []}, {"devices": [None]},
                          {"devices": [self.device(address="invalid")]},
                          {"devices": [self.device(port=True)]},
                          {"devices": [self.device(), self.device()]}):
            with self.subTest(inventory=inventory), self.assertRaises(ValueError):
                connection_plan(inventory)


if __name__ == "__main__":
    unittest.main()
