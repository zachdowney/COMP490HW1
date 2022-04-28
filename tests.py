import record
import pytest


def test_negative_price():
    records = [record.Record('shirt', -40, 'Clothing'), record.Record('hamburger', 5, 'Wic Eligible Food'),
               record.Record('bucket', 0, 'everything else')]
    with pytest.raises(ValueError):
        record.total_cost_with_tax('NH', records)


def test_invalid_state():
    records = [record.Record('shorts', 30, 'Clothing'), record.Record('cheese', 10, 'Wic Eligible Food'),
               record.Record('television', 500, 'everything else')]
    with pytest.raises(ValueError):
        record.total_cost_with_tax('NY', records)


def test_invalid_type():
    records = [record.Record('hoodie', 60, 'Clothing'), record.Record('sauce', 10, 'condiment'),
               record.Record('kite', 50, 'adventure')]
    with pytest.raises(ValueError):
        record.total_cost_with_tax('nh', records)


def test_wrong_data_types():
    records = [record.Record('towels', 20, 'Clothing'), record.Record(89, 'ten', 'Wic Eligible Food'),
               record.Record('laptop', 600, 9000)]
    with pytest.raises(TypeError):
        record.total_cost_with_tax('nh', records)


def test_variable_inputs():
    try:
        records = [record.Record('towels', 20, 'Clothing'), record.Record('food', 10, food),
                   record.Record(laptop, 600, 'everything else')]
        record.total_cost_with_tax('nh', records)
    except NameError:
        print("Inputs for item name and type must be in single or double quotes.")


def test_empty_state_and_inputs():
    records = [record.Record('', 20, ''), record.Record('', 90, ''),
               record.Record('xbox', 600, 'everything else')]
    with pytest.raises(SyntaxError):
        record.total_cost_with_tax('', records)


def test_ma_tax():
    records = [record.Record('socks', 10, 'Clothing'), record.Record('steak', 35, 'Wic Eligible Food'),
               record.Record('Air conditioner', 200, 'everything else')]
    assert record.total_cost_with_tax('MA', records) == 257.50


def test_me_tax():
    records = [record.Record('shoes', 190, 'Clothing'), record.Record('salmon', 35.45, 'Wic Eligible Food'),
               record.Record('shovel', 30.75, 'everything else')]
    assert record.total_cost_with_tax('ME', records) == 268.34


def test_nh_tax():
    records = [record.Record('pants', 60, 'Clothing'), record.Record('granola bars', 12, 'Wic Eligible Food'),
               record.Record('flag', 45, 'everything else')]
    assert record.total_cost_with_tax('NH', records) == 117.00


def test_ma_clothing_tax():
    records = [record.Record('suit', 500, 'Clothing'), record.Record('tie', 27, 'Clothing'),
               record.Record('shoes', 250, 'Clothing')]
    assert record.total_cost_with_tax('MA', records) == 802.00


def test_opposite_case_state_or_type():
    records = [record.Record('jersey', 60, 'clothing'), record.Record('fruit', 15, 'wic eligible food'),
               record.Record('sand', 110, 'EVERYTHING ELSE')]
    assert record.total_cost_with_tax('nh', records) == 185.00
