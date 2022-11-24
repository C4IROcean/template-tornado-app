import re
import sys

PROJECT_NAME_REGEX = "^app_[a-zA-Z0-9][_a-zA-Z0-9]+$"
PROJECT_GITHUB_REPO_REGEX = "^app-[a-zA-Z0-9][-a-zA-Z0-9]+$"

project_slug = "{{cookiecutter.project_slug}}"
github_repo = "{{cookiecutter.github_repo_name}}"

if not re.match(PROJECT_NAME_REGEX, project_slug):
    print(
        f"ERROR: The project slug ({project_slug}) is not a valid name. "
        "Valid apps starts with a 'app_' prefix and contains upper and lower case letters, "
        "numbers and underscores"
    )
    sys.exit(1)

if not re.match(PROJECT_GITHUB_REPO_REGEX, github_repo):
    print(
        f"ERROR: The github repo name ({github_repo}) is not a valid name. "
        "Valid apps starts with a 'app-' prefix and contains upper and lower case letters, "
        "numbers and dashes"
    )
    sys.exit(1)
