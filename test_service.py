import pytest
from service import get_user_from_db, get_users
import unittest.mock as mock
from requests.models import Response
import requests
@pytest.mark.parametrize("user_id, expected_name", [(1, "Alice"), (2, "Bob")])
@mock.patch("service.get_user_from_db")  
def test_get_user_from_db(mock_get_user_from_db, user_id, expected_name):
    mock_get_user_from_db.return_value = expected_name
    user_name = get_user_from_db(user_id)
    assert user_name == expected_name
    
@mock.patch("requests.get")
def test_get_users(mock_get: mock.Mock):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id":1, "name":"John Doe"}
    mock_get.return_value = mock_response
    data = get_users()
    assert data == {"id":1, "name":"John Doe"}
    mock_get.assert_called_once()

@mock.patch("requests.get")
def test_get_users_error(mock_get: mock.Mock):
    mock_response = mock.Mock(spec=requests.Response)
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        get_users()
    mock_get.assert_called_once() 