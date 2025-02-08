import pytest

def test_client_id_and_client_secret_is_not_none(client_id,client_secret):

    if client_id is None or client_secret is None:
        pytest.fail("One of those keys are empty!")
    
    assert client_id is not None and client_secret is not None, "The key is set!"