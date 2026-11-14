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

