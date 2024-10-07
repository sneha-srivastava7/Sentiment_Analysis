
import pandas as pd
import pytest

@pytest.fixture
def dummy_data():
    data = {'review': ['<html>Good movie!</html>', 'Bad movie, very bad', 'Great movie, I loved it!'], 
            'sentiment': ['positive', 'negative', 'positive']}
    return pd.DataFrame(data)

# Test data loading function
def test_load_data(dummy_data):
    assert len(dummy_data) == 3
    assert 'review' in dummy_data.columns
    assert 'sentiment' in dummy_data.columns
