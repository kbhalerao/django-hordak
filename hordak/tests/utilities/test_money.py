from decimal import Decimal

from django.test import TestCase
from tradeCore.hordak.utilities.money import ratio_split

# Note: these tests assume that sorting is stable across all Python versions.

class RatioSplitTestCase(TestCase):
    def test_extra_penny(self):
        values = ratio_split(Decimal("10"), [Decimal("3"), Decimal("3"), Decimal("3")])
        self.assertEqual(values, [Decimal('3.3334'), Decimal('3.3333'), Decimal('3.3333')])

    def test_less_penny(self):
        values = ratio_split(Decimal("8"), [Decimal("3"), Decimal("3"), Decimal("3")])
        self.assertEqual(values, [Decimal('2.6666'), Decimal('2.6667'), Decimal('2.6667')])

    def test_pennies(self):
        values = ratio_split(Decimal("-11.06"), [Decimal("1"), Decimal("1"), Decimal("1"), Decimal("1")])
        self.assertEqual(values, [Decimal('-2.7650'), Decimal('-2.7650'), Decimal('-2.7650'), Decimal('-2.7650')])

    def test_pennies_zeros(self):
        values = ratio_split(Decimal("11.0505"), [Decimal("1"), Decimal("1"), Decimal("0")])
        self.assertEqual(values, [Decimal('5.5253'), Decimal('5.5252'), Decimal('0.0000')])

        values = ratio_split(Decimal("11.05"), [Decimal("0"), Decimal("1"), Decimal("1")])
        self.assertEqual(values, [Decimal('0.0000'), Decimal('5.5250'), Decimal('5.5250')])

    def test_all_equal(self):
        values = ratio_split(Decimal("30"), [Decimal("3"), Decimal("3"), Decimal("3")])
        self.assertEqual(values, [Decimal("10"), Decimal("10"), Decimal("10")])
