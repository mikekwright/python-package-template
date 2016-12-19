import pytest

from app_name import Sample

@pytest.fixture(scope="module")
def test_model():
    return Sample()

def test_sample_get_hello_world(test_model):
    expected = 'Hello World'
    actual = test_model.get_hello_world()
    assert actual == expected
