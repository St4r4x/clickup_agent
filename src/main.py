import argparse
import logging
import os

from dotenv import load_dotenv
from requests.exceptions import HTTPError

from clickup_client import ClickUpClient

# --- Logging Setup ---
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('clickup_agent.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.INFO)

# Create formatters and add them to handlers
log_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(log_format)
f_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
# --- End Logging Setup ---

# Load environment variables from .env file
load_dotenv()


def main():
    """Main function to run the ClickUp client CLI."""
    logger.info("Starting ClickUp Agent CLI")
    api_token = os.getenv("CLICKUP_API_TOKEN")

    if not api_token or api_token == "YOUR_API_TOKEN":
        logger.error(
            "CLICKUP_API_TOKEN is not configured. Please set it in the .env file.")
        print("Please configure your CLICKUP_API_TOKEN in the .env file.")
        return

    client = ClickUpClient(api_token)

    parser = argparse.ArgumentParser(
        description="A command-line interface to manage your ClickUp account.")

    # Team arguments
    team_parser = parser.add_subparsers(dest='command', title='Commands')
    list_teams_parser = team_parser.add_parser(
        'list-teams', help='List all teams (workspaces).')

    # Space arguments
    space_parser = team_parser.add_parser(
        'list-spaces', help='List all spaces in a team.')
    space_parser.add_argument('team_id', type=str, help='The ID of the team.')

    create_space_parser = team_parser.add_parser(
        'create-space', help='Create a new space.')
    create_space_parser.add_argument(
        'team_id', type=str, help='The ID of the team to create the space in.')
    create_space_parser.add_argument(
        'space_name', type=str, help='The name of the new space.')

    get_space_parser = team_parser.add_parser(
        'get-space', help='Get details for a specific space.')
    get_space_parser.add_argument(
        'space_id', type=str, help='The ID of the space.')

    update_space_parser = team_parser.add_parser(
        'update-space', help='Update a space.')
    update_space_parser.add_argument(
        'space_id', type=str, help='The ID of the space to update.')
    update_space_parser.add_argument(
        'new_name', type=str, help='The new name for the space.')

    delete_space_parser = team_parser.add_parser(
        'delete-space', help='Delete a space.')
    delete_space_parser.add_argument(
        'space_id', type=str, help='The ID of the space to delete.')

    args = parser.parse_args()

    try:
        if args.command == 'list-teams':
            logger.info("Fetching teams.")
            teams = client.get_teams()
            print("Your ClickUp teams (workspaces):")
            for team in teams.get('teams', []):
                print(f"- Name: {team.get('name')}, ID: {team.get('id')}")

        elif args.command == 'list-spaces':
            logger.info(f"Fetching spaces for team {args.team_id}.")
            spaces = client.get_spaces(args.team_id)
            print(f"Spaces in team {args.team_id}:")
            for space in spaces.get('spaces', []):
                print(f"- Name: {space.get('name')}, ID: {space.get('id')}")

        elif args.command == 'create-space':
            logger.info(
                f"Creating space '{args.space_name}' in team {args.team_id}.")
            new_space = client.create_space(args.team_id, args.space_name)
            print(f"Successfully created space: '{new_space.get('name')}'")
            logger.info(
                f"Successfully created space: '{new_space.get('name')}' with ID {new_space.get('id')}")

        elif args.command == 'get-space':
            logger.info(f"Fetching details for space {args.space_id}.")
            space = client.get_space(args.space_id)
            print("Space details:")
            print(space)

        elif args.command == 'update-space':
            logger.info(
                f"Updating space {args.space_id} with new name '{args.new_name}'.")
            updated_space = client.update_space(args.space_id, args.new_name)
            print(
                f"Successfully updated space to '{updated_space.get('name')}'")
            logger.info(f"Successfully updated space {args.space_id}")

        elif args.command == 'delete-space':
            logger.info(f"Deleting space with ID: {args.space_id}")
            client.delete_space(args.space_id)
            print(f"Successfully deleted space with ID: {args.space_id}")
            logger.info(f"Successfully deleted space with ID: {args.space_id}")

        else:
            parser.print_help()

    except HTTPError as e:
        logger.error(
            f"API error occurred: {e.response.status_code} - {e.response.reason}")
        logger.error(f"Response body: {e.response.text}")
        print(f"An API error occurred: {e}")
        print(f"Response body: {e.response.text}")
    except Exception as e:
        logger.exception("An unexpected error occurred: %s", e)
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
