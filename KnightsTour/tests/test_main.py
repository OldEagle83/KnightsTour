from unittest import TestCase
import os
import logging
from .. import main

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

false_test_data = os.path.join(os.path.dirname(__file__), 'false_check_coord')
true_test_data = os.path.join(os.path.dirname(__file__), 'true_check_coord')


class TestBoard(TestCase):
    def setUp(self) -> None:
        self.false_data = open(false_test_data).readlines()
        self.true_data = open(true_test_data).readlines()
        self.test01 = main.Knight(2, 2, 'X')

    def tearDown(self):
        pass

    def test_check_coord(self):
        logging.info('Testing False data')
        for line in self.false_data:
            self.assertFalse(self.test01.check_coord(*line.strip().split()))
        logging.info('Testing True data')
        for line in self.true_data:
            self.assertTrue(self.test01.check_coord(*line.strip().split()))
