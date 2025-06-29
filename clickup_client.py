import requests


class ClickUpClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.clickup.com/api/v2/"

    def _get_headers(self):
        return {
            "Authorization": self.api_token,
            "Content-Type": "application/json"
        }

    def get_teams(self):
        """Récupère les équipes (espaces de travail) de l'utilisateur."""
        response = requests.get(
            f"{self.base_url}team", headers=self._get_headers())
        response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
        return response.json()

    def create_space(self, team_id, name):
        """Crée un nouvel espace dans une équipe spécifiée."""
        url = f"{self.base_url}team/{team_id}/space"
        payload = {"name": name}
        response = requests.post(
            url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def delete_space(self, space_id):
        """Supprime un espace spécifié."""
        url = f"{self.base_url}space/{space_id}"
        response = requests.delete(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_spaces(self, team_id):
        """Récupère les espaces pour une équipe spécifiée."""
        url = f"{self.base_url}team/{team_id}/space"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_space(self, space_id):
        """Récupère les détails d'un espace spécifié."""
        url = f"{self.base_url}space/{space_id}"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def update_space(self, space_id, name):
        """Met à jour le nom d'un espace spécifié."""
        url = f"{self.base_url}space/{space_id}"
        payload = {"name": name}
        response = requests.put(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
