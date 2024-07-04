import pytest
from service import get_user_from_db
import unittest.mock as mock


@pytest.mark.parametrize("user_id, expected_name", [(1, "Alice"), (2, "Bob")])
@mock.patch("service.get_user_from_db")  
def test_get_user_from_db(mock_get_user_from_db, user_id, expected_name):
    mock_get_user_from_db.return_value = expected_name
    user_name = get_user_from_db(user_id)
    assert user_name == expected_name