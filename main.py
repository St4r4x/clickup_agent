from clickup_client import ClickUpClient
import os
from dotenv import load_dotenv
import argparse

load_dotenv()


def main():
    """Fonction principale pour exécuter le client ClickUp."""
    api_token = os.getenv("CLICKUP_API_TOKEN")

    if not api_token or api_token == "VOTRE_TOKEN_API":
        print("Veuillez configurer votre CLICKUP_API_TOKEN dans le fichier .env")
        return

    client = ClickUpClient(api_token)

    parser = argparse.ArgumentParser(
        description="Gérez vos équipes et espaces ClickUp.")
    parser.add_argument("--list-teams", action="store_true",
                        help="Liste toutes les équipes.")
    parser.add_argument("--list-spaces", metavar="TEAM_ID",
                        help="Liste tous les espaces pour une équipe donnée.")
    parser.add_argument("--create-space", nargs=2, metavar=("TEAM_ID",
                        "SPACE_NAME"), help="Crée un nouvel espace.")
    parser.add_argument("--delete-space", metavar="SPACE_ID",
                        help="Supprime un espace.")
    parser.add_argument("--get-space", metavar="SPACE_ID",
                        help="Affiche les détails d'un espace.")
    parser.add_argument("--update-space", nargs=2, metavar=("SPACE_ID",
                        "NEW_NAME"), help="Met à jour le nom d'un espace.")

    args = parser.parse_args()

    try:
        if args.list_teams:
            teams = client.get_teams()
            print("Voici la liste de vos équipes (espaces de travail) ClickUp :")
            for team in teams.get('teams', []):
                print(f"- Nom : {team.get('name')}, ID : {team.get('id')}")
        elif args.list_spaces:
            team_id = args.list_spaces
            spaces = client.get_spaces(team_id)
            print(f"Voici la liste des espaces pour l'équipe {team_id} :")
            for space in spaces.get('spaces', []):
                print(f"- Nom : {space.get('name')}, ID : {space.get('id')}")
        elif args.create_space:
            team_id, space_name = args.create_space
            new_space = client.create_space(team_id, space_name)
            print(f"Espace '{new_space.get('name')}' créé avec succès.")
        elif args.delete_space:
            space_id = args.delete_space
            client.delete_space(space_id)
            print(f"Espace avec l'ID {space_id} supprimé avec succès.")
        elif args.get_space:
            space_id = args.get_space
            space = client.get_space(space_id)
            print("Détails de l'espace :")
            print(space)
        elif args.update_space:
            space_id, new_name = args.update_space
            updated_space = client.update_space(space_id, new_name)
            print(
                f"Espace '{updated_space.get('name')}' mis à jour avec succès.")
        else:
            print("Veuillez spécifier une action. Utilisez --help pour voir les options.")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")


if __name__ == "__main__":
    main()
