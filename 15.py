# from unittest import TestCase
#
#
# def multiply(a, b):
#     return a*b
#
#
# class Test(TestCase):
#
#
#     def test_multiply(self):
#         self.assertEqual(multiply(2, 4), 8)
#
#
#     def test_multiply2(self):
#         self.assertEqual(multiply(2, 4), 8)


import pytest


def multiply(x, y):
    return x * y


@pytest.mark.parametrize(
    'x,y,c', [
        (2, 4, 8),
        (3, 5, 15),
        (3, 7, 21),
        (12, 8, 96)
    ]
)
def test_multiply(x, y, c):
    assert multiply(x, y) == c
