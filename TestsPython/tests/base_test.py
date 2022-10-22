import os
import sys

sys.path.append(os.path.dirname(__file__))

from altunityrunner import AltUnityDriver
import unittest
import pytest

class TestBase(unittest.TestCase):
    plaform = os.getenv('TESTS_PLATFORM')
    
    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltUnityDriver()

    @classmethod    
    def tearDownClass(cls):
        cls.altdriver.stop()
