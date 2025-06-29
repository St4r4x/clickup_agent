import requests
import logging

logger = logging.getLogger(__name__)


class ClickUpClient:
    """A client for interacting with the ClickUp API."""
    def __init__(self, api_token: str, base_url: str = "https://api.clickup.com/api/v2/"):
        """
        Initializes the ClickUpClient.

        Args:
            api_token: Your ClickUp API token.
            base_url: The base URL for the ClickUp API.
        """
        self.api_token = api_token
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": self.api_token,
            "Content-Type": "application/json"
        })
        self.timeout = 10  # seconds

    def get_teams(self):
        """Fetches the user's teams (workspaces)."""
        response = self.session.get(f"{self.base_url}team", timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def create_space(self, team_id: str, name: str):
        """Creates a new space within a specified team."""
        url = f"{self.base_url}team/{team_id}/space"
        payload = {"name": name}
        response = self.session.post(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def delete_space(self, space_id: str):
        """Deletes a specified space."""
        url = f"{self.base_url}space/{space_id}"
        response = self.session.delete(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def get_spaces(self, team_id: str):
        """Retrieves all spaces for a specified team."""
        url = f"{self.base_url}team/{team_id}/space"
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def get_space(self, space_id: str):
        """Retrieves details for a specified space."""
        url = f"{self.base_url}space/{space_id}"
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def update_space(self, space_id: str, name: str):
        """Updates the name of a specified space."""
        url = f"{self.base_url}space/{space_id}"
        payload = {"name": name}
        response = self.session.put(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
