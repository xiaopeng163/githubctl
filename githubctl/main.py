import os

import typer
from rich import print
from dotenv import load_dotenv

from githubctl.cli.repo import repo_app


if os.path.isfile(".env"):
    load_dotenv()

app = typer.Typer()

app.add_typer(repo_app, name="repo")


if __name__ == "__main__":
    app()
