import pytest

from temperature_converter import (
    c_to_f,
    f_to_c,
    c_to_k,
    k_to_c
)


def test_c_to_f():
    assert c_to_f(0) == pytest.approx(32)


def test_c_to_f_boiling():
    assert c_to_f(100) == pytest.approx(212)


def test_f_to_c():
    assert f_to_c(32) == pytest.approx(0)


def test_f_to_c_boiling():
    assert f_to_c(212) == pytest.approx(100)


def test_c_to_k():
    assert c_to_k(0) == pytest.approx(273.15)


def test_c_to_k_freezing():
    assert c_to_k(-273.15) == pytest.approx(0)


def test_k_to_c():
    assert k_to_c(273.15) == pytest.approx(0)


def test_k_to_c_boiling():
    assert k_to_c(373.15) == pytest.approx(100)