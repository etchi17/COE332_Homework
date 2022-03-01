from ml_data_analysis import *
import pytest

def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}], 'a') == 1
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2
    assert compute_average_mass([{'a': 10}, {'a': 1}, {'a': 1}], 'a') == 4
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True

def test_compute_average_mass_exceptions():
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')                              
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')            
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a')          
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a': 2}], 'b')           

def test_check_hemisphere():
    assert check_hemisphere(1,1) == 'Northern & Eastern'
    assert check_hemisphere(1,-1) == 'Northern & Western'
    assert check_hemisphere(-1,1) == 'Southern & Eastern'
    assert check_hemisphere(-1,-1) == 'Southern & Western'
    assert isinstance(check_hemisphere(1,1), str) == True

def test_check_hemisphere_exceptions():
    with pytest.raises(ValueError):
        check_hemisphere(1,0)
    with pytest.raises(ValueError):
        check_hemisphere(0,1)

def test_count_classes():
    test_list = [{'key1': 'ab', 'key2': 'bc'}, {'key1': 'bc', 'key2': 'bc'}, {'key1': 'ba', 'key2':'ab'}, {'key1': 'bc', 'key2': 'cb'}]

    assert count_classes(test_list, 'key1') == {'ab': 1, 'bc': 2, 'ba': 1} 
    assert count_classes(test_list, 'key2') == {'bc': 2, 'ab': 1, 'cb': 1}
    assert isinstance(count_classes(test_list, 'key1'), dict) == True

def test_count_classes_exceptions():
    test_list1 = [{'key1': 'ab', 'key2': 'bc'}, {'key1': 'bc', 'key2': 'bc'}, {'key3': 'ba', 'key2':'ab'}, {'key1': 'bc', 'key2': 'cb'}]
    test_list2 = [{'key1': 'ab', 'key2': 'bc'}, {'key1': 'bc', 'key2': 'bc'}, {'key1': 'ba', 'key2':'ab'}, {'key1'    : 'bc', 'key2': 'cb'}]

    with pytest.raises(KeyError):
        count_classes(test_list1, 'key1')
    with pytest.raises(KeyError):
        count_classes(test_list2, 1)
