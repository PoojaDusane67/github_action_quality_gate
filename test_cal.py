# this is the for test case execution

import pytest
from calc import add, sub, mult, div


def test_add():
    assert add (2,3)==5

def test_add():
    assert sub (6,3)==3

def test_add():
    assert mult (2,3)==6

def test_add():
    assert div (4,2)==2
