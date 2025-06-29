# ClickUp Agent: A Python CLI for ClickUp

ClickUp Agent is a powerful, production-quality Python command-line interface (CLI) for interacting with the ClickUp API. It enables you to manage your teams, spaces, and other ClickUp resources directly from the command line, streamlining your workflow and enabling automation.

## Features

- **Team Management**: List all your ClickUp teams (workspaces).
- **Space Management**: List, create, view, update, and delete spaces within your teams.
- **Extensible**: Designed for easy extension to support more ClickUp features like Folders, Lists, and Tasks.
- **Best Practices**: Built with a focus on modern Python best practices, including type hints, logging, and comprehensive unit tests.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- [Conda](https://docs.conda.io/en/latest/miniconda.html) (recommended for environment management)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-repo/clickup-agent.git
    cd clickup-agent
    ```

2.  **Create and activate a Conda environment:**

    ```bash
    conda create --name clickup-agent-env python=3.9 -y
    conda activate clickup-agent-env
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **For development, install testing dependencies:**

    ```bash
    pip install -r requirements-dev.txt
    ```

5.  **Configure your API token:**
    - Rename `.env.example` to `.env`.
    - Open `.env` and replace `YOUR_API_TOKEN` with your actual ClickUp API token.

## Usage

All commands are run from the project root. The main entry point is `src/main.py`.

To see a list of available commands, run:

```bash
python src/main.py --help
```

### Teams (Workspaces)

- **List teams:**
  ```bash
  python src/main.py list-teams
  ```

### Spaces

- **List spaces in a team:**
  ```bash
  python src/main.py list-spaces <TEAM_ID>
  ```
- **Create a space:**
  ```bash
  python src/main.py create-space <TEAM_ID> "<SPACE_NAME>"
  ```
- **Get space details:**
  ```bash
  python src/main.py get-space <SPACE_ID>
  ```
- **Update a space's name:**
  ```bash
  python src/main.py update-space <SPACE_ID> "<NEW_NAME>"
  ```
- **Delete a space:**
  ```bash
  python src/main.py delete-space <SPACE_ID>
  ```

## Testing

To run the full suite of unit tests, use `pytest`:

```bash
pytest
```

## Contributing

We welcome contributions from the community! Whether it's reporting a bug, suggesting a feature, or submitting a pull request, your help is valued.

Please read our [**Contributing Guidelines**](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Branch Protection Rules

To ensure the stability and quality of the `main` branch, the following protection rules are in effect:

- **Pull Request Required**: All changes must be submitted via a pull request.
- **Status Checks**: All status checks (e.g., CI builds, tests) must pass before merging.
- **Code Reviews**: At least one code review from a maintainer is required.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Code Structure

- `src/`: Contains the main application source code.
  - `main.py`: The CLI entry point and command registration logic.
  - `clickup_client.py`: The core `ClickUpClient` for API interactions.
  - `commands/`: Contains the implementation for each CLI command.
    - `base.py`: The base class for all commands.
    - `...`: Individual command files.
- `tests/`: Contains all unit tests.
- `.env`: For storing your API token securely (not committed to Git).
- `requirements.txt`: Production dependencies.
- `requirements-dev.txt`: Development and testing dependencies.

## First Release (v1.0.0)

This is the first official release of ClickUp Agent. It provides a solid foundation for managing ClickUp teams and spaces, with a robust architecture for future expansion.

## Contributors

- Your Name Here! (We are looking for contributors)

## Disclaimer

This project is not an official ClickUp product and is not affiliated with ClickUp in any way.
