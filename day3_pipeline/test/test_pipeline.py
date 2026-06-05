from data_loader import load_data
from preprocess import preprocess_data
from train import train_model
from evaluate import evaluate_model


def test_load_data():
    data = load_data()
    assert data is not None, "Data should not be None"
    assert hasattr(data, "data")
    assert hasattr(data, "target")
    assert len(data.data) > 0, "Data should not be empty"
    assert len(data.target) > 0, "Target should not be empty"


def test_pipeline():
    data = [1, 2, 3]

    processed = preprocess_data(data)
    model = train_model(processed)
    score = evaluate_model(model, processed)

    assert score is not None
