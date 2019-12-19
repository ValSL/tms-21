from task_for_test import calc_sum
from unittest import TestCase


def test_calc_istuple():
    result = calc_sum([1, 2, 3, -4, -5, -6])
    tup = ()
    assert type(result) is tuple


def test_calc_len_more_then_one():
    result = calc_sum([1, 2, 3, -4, -5, -6])
    assert len(result) > 1


def test_pos_sum_is_pos():
    result = calc_sum([1, 2, 3, -4, -5, -6])
    assert result[0] > 0


def test_neg_sum_is_neg():
    result = calc_sum([1, 2, 3, -4, -5, -6])
    assert result[1] < 0


def test_for_list_len():
    result = calc_sum([])
    assert result == (0, 0)


