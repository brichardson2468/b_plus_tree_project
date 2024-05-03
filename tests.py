import unittest
import datetime
from src.b_plus_tree import BPlusTree


class TestBPlusTree(unittest.TestCase):
    def setUp(self):
        self.bpt = BPlusTree(max_keys=4)

    def test_record_integrity_and_retrieval(self):
        # Sample record
        record = {'Indicator': 'Depressive Disorder', 'Group': 'By Age', 'State': 'United States', 
                  'Subgroup': '18 - 29 years', 'Time Period Start Date': '2024-02-06', 
                  'Time Period End Date': '2024-03-04', 'Value': 24.1}
        key = (datetime.date(2024, 2, 6), datetime.date(2024, 3, 4))

        # Insert record
        self.bpt.insert(key, record)

        # Attempt to retrieve the record
        search_results = self.bpt.search_range(datetime.date(2024, 2, 6), datetime.date(2024, 3, 4))
        
        # Check the results
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0], record)

if __name__ == '__main__':
    unittest.main()