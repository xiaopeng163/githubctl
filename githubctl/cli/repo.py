import typer
import jmespath

from githubctl.options import OutputOption
from githubctl.github import get_all_user_repositories
from githubctl.utils import print_beauty, sort_by_key

repo_app = typer.Typer()


@repo_app.command(name="list", help="list user repository")
def list_repos(
    user: str = typer.Option(..., "--user", "-u", help="github user name"),
    output: OutputOption = typer.Option(
        OutputOption.table, "--output", "-o", help="output format"
    ),
    query: str = typer.Option(None, "--query", "-q", help="query with jmespath"),
    sort_by: str = typer.Option(None, "--sort-by", "-s", help="sort by key"),
):
    repo = get_all_user_repositories(username=user)
    if query:
        repo = jmespath.search(query, repo)
    if sort_by:
        if sort_by.startswith("~"):
            reverse = True
            sort_by = sort_by[1:].split(",")
        else:
            reverse = False
        repo = sort_by_key(list_of_dict=repo, key_list=sort_by, reverse=reverse)
    print_beauty(list_of_dict=repo, output=output)
