from data_loader import load_data


def test_load_data():
    data = load_data()
    assert data is not None, "Data should not be None"
    assert hasattr(data, "data")
    assert hasattr(data, "target")
    assert len(data.data) > 0, "Data should not be empty"
    assert len(data.target) > 0, "Target should not be empty"
