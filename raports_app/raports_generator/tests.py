from django.test import TestCase

import unittest

# Create your tests here.


class TestBasic(unittest.TestCase):

    def test_basic_3(self):
        a = 1
        assert a == 1
