# -*- coding: utf-8 -*-

import pytest
from send_to_gtalk.skeleton import fib

__author__ = "Daniel Boline"
__copyright__ = "Daniel Boline"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
