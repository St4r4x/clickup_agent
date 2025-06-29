
import pytest
from unittest.mock import MagicMock, patch
from src.main import main
from src.clickup_client import ClickUpClient
import sys

@pytest.fixture
def mock_client():
    """Fixture for a mocked ClickUpClient."""
    with patch('src.main.ClickUpClient') as mock:
        instance = mock.return_value
        instance.get_teams.return_value = {"teams": [{"id": "123", "name": "Test Team"}]}
        instance.get_spaces.return_value = {"spaces": [{"id": "456", "name": "Test Space"}]}
        instance.create_space.return_value = {"id": "789", "name": "New Space"}
        instance.get_space.return_value = {"id": "456", "name": "Test Space"}
        instance.update_space.return_value = {"id": "456", "name": "Updated Space"}
        instance.delete_space.return_value = {}
        yield mock

@patch('src.main.os.getenv', return_value="test_token")
def test_list_teams(mock_getenv, mock_client, capsys):
    """Test the list-teams command."""
    sys.argv = ['main.py', 'list-teams']
    main()
    captured = capsys.readouterr()
    assert "Test Team" in captured.out

@patch('src.main.os.getenv', return_value="test_token")
def test_list_spaces(mock_getenv, mock_client, capsys):
    """Test the list-spaces command."""
    sys.argv = ['main.py', 'list-spaces', '123']
    main()
    captured = capsys.readouterr()
    assert "Test Space" in captured.out

@patch('src.main.os.getenv', return_value="test_token")
def test_create_space(mock_getenv, mock_client, capsys):
    """Test the create-space command."""
    sys.argv = ['main.py', 'create-space', '123', 'New Space']
    main()
    captured = capsys.readouterr()
    assert "Successfully created space: 'New Space'" in captured.out

@patch('src.main.os.getenv', return_value="test_token")
def test_get_space(mock_getenv, mock_client, capsys):
    """Test the get-space command."""
    sys.argv = ['main.py', 'get-space', '456']
    main()
    captured = capsys.readouterr()
    assert "Test Space" in captured.out

@patch('src.main.os.getenv', return_value="test_token")
def test_update_space(mock_getenv, mock_client, capsys):
    """Test the update-space command."""
    sys.argv = ['main.py', 'update-space', '456', 'Updated Space']
    main()
    captured = capsys.readouterr()
    assert "Successfully updated space to 'Updated Space'" in captured.out

@patch('src.main.os.getenv', return_value="test_token")
def test_delete_space(mock_getenv, mock_client, capsys):
    """Test the delete-space command."""
    sys.argv = ['main.py', 'delete-space', '456']
    main()
    captured = capsys.readouterr()
    assert "Successfully deleted space with ID: 456" in captured.out

@patch('src.main.os.getenv', return_value=None)
def test_no_api_token(mock_getenv, capsys):
    """Test that the CLI exits if no API token is provided."""
    sys.argv = ['main.py', 'list-teams']
    main()
    captured = capsys.readouterr()
    assert "Please configure your CLICKUP_API_TOKEN" in captured.out
