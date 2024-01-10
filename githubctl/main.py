import os

import typer
from rich import print
from dotenv import load_dotenv
import jmespath

from github import get_all_user_repositories
from utils import print_beauty
from options import OutputOption


if os.path.isfile(".env"):
    load_dotenv()

app = typer.Typer()

repo_app = typer.Typer()

app.add_typer(repo_app, name="repo")


@repo_app.command(name="list", help="list user repository")
def list_repos(
    user: str = typer.Option(..., "--user", "-u", help="github user name"),
    output: OutputOption = typer.Option(
        OutputOption.table, "--output", "-o", help="output format"
    ),
    query: str = typer.Option(None, "--query", "-q", help="query with jmespath"),
):
    repo = get_all_user_repositories(username=user)
    if query:
        repo = jmespath.search(query, repo)
    print_beauty(list_of_dict=repo, output=output)


if __name__ == "__main__":
    app()
