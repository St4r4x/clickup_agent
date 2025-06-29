
from unittest.mock import MagicMock

import pytest

from src.clickup_client import ClickUpClient


@pytest.fixture
def client():
    """Fixture for ClickUpClient."""
    return ClickUpClient(api_token="test_token")


def test_get_teams(client, mocker):
    """Test getting teams."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "teams": [{"id": "123", "name": "Test Team"}]}
    mock_response.raise_for_status.return_value = None
    mocker.patch.object(client.session, "get", return_value=mock_response)

    teams = client.get_teams()

    assert teams["teams"][0]["name"] == "Test Team"
    client.session.get.assert_called_with(
        f"{client.base_url}team", timeout=client.timeout)
