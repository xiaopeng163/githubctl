import os
from enum import Enum

import typer
from rich import print
from dotenv import load_dotenv

from github import get_all_user_repositories

if os.path.isfile(".env"):
    load_dotenv()

app = typer.Typer()

repo_app = typer.Typer()

app.add_typer(repo_app, name="repo")


class OutputOption(str, Enum):
    json = "json"
    csv = "csv"
    table = "table"


@repo_app.command(name="list", help="list user repository")
def list_repos(
    user: str = typer.Option(..., "--user", "-u", help="github user name"),
    output: OutputOption = typer.Option(
        OutputOption.json, "--output", "-o", help="output format"
    ),
):
    # repo = get_all_user_repositories(username=user)
    # print(repo)
    print(output)


if __name__ == "__main__":
    app()
