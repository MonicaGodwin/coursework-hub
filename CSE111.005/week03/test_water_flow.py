from pytest import approx
import pytest
from water_flow import(
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
)

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == (0.0)
    assert water_column_height(0.0, 10.0) == (7.5)
    assert water_column_height(25.0, 0.0) == (25.0)
    assert water_column_height(48.3, 12.8) == (57.9)


def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

