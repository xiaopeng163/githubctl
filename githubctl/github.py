import os
import requests


class GitHubAPI:
    def __init__(self):
        if os.environ.get("GITHUB_TOKEN"):
            self.headers = {"Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}"}
        else:
            self.headers = None

    def delete_repository_for_user(self, username, repo_name):
        """
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#delete-a-repository
        """
        base_url = f"https://api.github.com/repos/{username}/{repo_name}"
        response = requests.delete(base_url, headers=self.headers)
        if response.status_code == 204:
            return True
        else:
            return False

    def get_all_repositories_for_user(self, username):
        """
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository
        """
        base_url = f"https://api.github.com/users/{username}/repos"
        repos = []
        try:
            page = 1
            while True:
                params = {"page": page, "per_page": 100}  # Adjust per_page as needed
                response = requests.get(base_url, params=params, headers=self.headers)
                response.raise_for_status()

                repositories = response.json()
                if not repositories:
                    break  # No more repositories

                for repo in repositories:
                    repo_info = {
                        "id": repo["id"],
                        "name": repo["name"],
                        "url": repo["html_url"],
                        "description": repo["description"],
                        "language": repo["language"],
                        "stars": repo["stargazers_count"],
                        "forks": repo["forks_count"],
                        "fork": str(repo["fork"]),
                        "created_at": repo["created_at"],
                    }
                    repos.append(repo_info)

                page += 1

            return repos
        except requests.exceptions.RequestException as e:
            print(f"Error fetching repositories for user {username}: {e}")
            return None
