from analyze_water_turb import calc_turb
from analyze_water_turb import calc_min_time
import pytest
import math

def test_calc_turb():
    data1 = [{'a': 1, 'b': 2}, {'a': 2, 'b': 3}, {'a': 1, 'b': 4}, {'a': 2, 'b': 5}, {'a': 4, 'b': 2}, {'a': 2, 'b': 3}]
    data2 = [{'a': 3, 'b': 5}, {'a': 2, 'b': 6}, {'a': 2, 'b': 4}, {'a': 2, 'b': 3}, {'a': 6, 'b': 1}, {'a': 4, 'b': 2}]

    assert calc_turb(data1, 'a', 'b') == 34/5
    assert calc_turb(data2, 'a', 'b') == 40/5
    assert isinstance(calc_turb(data1, 'a', 'b'), float) == True
    
def test_calc_turb_exceptions():
    data1 = [{'a': 1, 'b': 2}, {'a': 2, 'b': 3}, {'a': 1, 'b': 4}, {'a': 2, 'b': 5}, {'a': 4, 'b': 2}, {'a': 2, 'b': 3}]
    data2 = [{'a': 3, 'b': 5}, {'a': 2, 'b': 6}, {'a': 2, 'b': 4}, {'a': 2, 'b': 3}, {'a': 6, 'b': 'x'}, {'a': 4, 'b': 2}]
    data3 = [{'a': 3, 'b': 5}, {'a': 2, 'b': 6}, {'d': 2, 'b': 4}, {'a': 2, 'b': 3}, {'a': 6, 'c': 3}, {'a': 4, 'b': 2}]

    with pytest.raises(KeyError):
        calc_turb(data3, 'a', 'b')                       
    with pytest.raises(TypeError):
        calc_turb(data2, 'a', 'b')                       
    with pytest.raises(KeyError):
        calc_turb(data1, 'c', 'd')                       

def test_calc_min_time():
    assert calc_min_time(1, 1.8, .02) == math.log(1/1.8)/math.log(1-.02)
    assert calc_min_time(1, .5, .02) == 0
    assert isinstance(calc_min_time(1, 1.5, .3), float) == True

def test_calc_min_time_exceptions():
    with pytest.raises(TypeError):
        calc_min_time(1, 'x', .2)
    with pytest.raises(TypeError):
        calc_min_time(1, 1.7, 'x')
    with pytest.raises(TypeError):
        calc_min_time('x', 1.4, .2)
    with pytest.raises(ValueError):
        calc_min_time(1, 1.6, 3)
