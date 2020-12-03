import unittest
from unittest.mock import *
from src.time import *


class CheckerTest(unittest.TestCase):

    def test_checker_before_17(self):
        checker = Checker()

        checker.env.getTime = Mock(name='getTime')
        checker.env.getTime.return_value = 11

        checker.env.resetWav = Mock(name='resetWav')
        checker.env.resetWav.return_value = False

        res = checker.remainder('lastchristmas.wav')
        self.assertEqual(res, False)

    def test_checker_after_17(self):
        checker = Checker()

        checker.env.getTime = Mock(name='getTime')
        checker.env.getTime.return_value = 20

        checker.env.wavWasPlayed = Mock(name='wavWasPlayed')
        checker.env.wavWasPlayed.return_value = True

        res = checker.remainder('lastchristmas.wav')
        self.assertEqual(res, True)