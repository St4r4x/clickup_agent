
from unittest.mock import MagicMock

import pytest
import requests

from src.clickup_client import ClickUpClient


@pytest.fixture
def client():
    """Fixture for ClickUpClient."""
    return ClickUpClient(api_token="test_token")


def test_get_spaces(client, mocker):
    """Test getting spaces for a team."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "spaces": [{"id": "123", "name": "Test Space"}]}
    mock_response.raise_for_status.return_value = None
    mocker.patch.object(client.session, "get", return_value=mock_response)

    spaces = client.get_spaces(team_id="test_team")

    assert spaces["spaces"][0]["name"] == "Test Space"
    client.session.get.assert_called_with(
        f"{client.base_url}team/test_team/space", timeout=client.timeout)


def test_get_space(client, mocker):
    """Test getting a single space."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "123", "name": "Test Space"}
    mock_response.raise_for_status.return_value = None
    mocker.patch.object(client.session, "get", return_value=mock_response)

    space = client.get_space(space_id="123")

    assert space["name"] == "Test Space"
    client.session.get.assert_called_with(
        f"{client.base_url}space/123", timeout=client.timeout)


def test_create_space(client, mocker):
    """Test creating a space."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "456", "name": "New Space"}
    mock_response.raise_for_status.return_value = None
    mocker.patch.object(client.session, "post", return_value=mock_response)

    new_space = client.create_space(team_id="test_team", name="New Space")

    assert new_space["name"] == "New Space"
    client.session.post.assert_called_with(
        f"{client.base_url}team/test_team/space",
        json={"name": "New Space"},
        timeout=client.timeout
    )


def test_update_space(client, mocker):
    """Test updating a space."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "123", "name": "Updated Space"}
    mock_response.raise_for_status.return_value = None
    mocker.patch.object(client.session, "put", return_value=mock_response)

    updated_space = client.update_space(space_id="123", name="Updated Space")

    assert updated_space["name"] == "Updated Space"
    client.session.put.assert_called_with(
        f"{client.base_url}space/123",
        json={"name": "Updated Space"},
        timeout=client.timeout
    )


def test_delete_space(client, mocker):
    """Test deleting a space."""
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    mock_response.raise_for_status.return_value = None
    mocker.patch.object(client.session, "delete", return_value=mock_response)

    response = client.delete_space(space_id="123")

    assert response == {}
    client.session.delete.assert_called_with(
        f"{client.base_url}space/123", timeout=client.timeout)


def test_api_error(client, mocker):
    """Test that API errors are raised."""
    mocker.patch.object(client.session, "get",
                        side_effect=requests.exceptions.HTTPError("API Error"))

    with pytest.raises(requests.exceptions.HTTPError):
        client.get_spaces(team_id="test_team")
