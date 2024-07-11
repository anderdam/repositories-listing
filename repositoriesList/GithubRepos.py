import datetime
from typing import Any, Dict

import requests


class GithubRepos:
    def __init__(self, token: str) -> None:
        """
        :type token: object
        """

        self.token = token
        self.today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def check_rate_limit(self) -> Dict[str, Any]:
        """
        Check the GitHub API rate limit.
        """
        headers = {"Authorization": f"token {self.token}"}
        url = "https://api.github.com/rate_limit"
        response = requests.get(url, headers=headers, timeout=10)
        rate_limit_info = response.json()
        return rate_limit_info

    def get_github_repositories(self) -> Dict[str, Any]:
        repositories: Dict[str, Any] = {}
        page = 1
        username = "anderdam"
        while True:
            url = f"https://api.github.com/users/{username}/repos?page={page}"
            headers = {"Authorization": f"token {self.token}"}
            response = requests.get(url, headers=headers, timeout=10)
            page_repositories = response.json()
            if not page_repositories:
                break
            for repo in page_repositories:
                contents_url = (
                    f"https://api.github.com/repos/anderdam/{repo['name']}/contents"
                )
                contents_response = requests.get(
                    contents_url, headers=headers, timeout=10
                )
                repo["empty"] = (
                    not contents_response.json()
                )  # Set 'empty' flag based on contents
                repositories.append(repo)
            if "next" not in response.links:
                break
            page += 1
        return repositories

    def save_repositories(self, name) -> None:
        rate_limit_info = self.check_rate_limit()
        repos = self.get_github_repositories()

        with open(name, "w") as file:
            file.write(f"Results for {self.today}:\n")
            file.write("---------------------------------")
            file.write("Rate Limit Status:")
            file.write(f'- Limit: {rate_limit_info["resources"]["core"]["limit"]}')
            file.write(f'- Used: {rate_limit_info["resources"]["core"]["used"]}')
            file.write(
                f'- Remaining: {rate_limit_info["resources"]["core"]["remaining"]}'
            )
            file.write(f'- Reset: {rate_limit_info["resources"]["core"]["reset"]}')
            file.write("---------------------------------")

            file.write("")

            file.write("---------------------------------")
            file.write("Repositories:\n")
            for repo in repos:
                file.write(f'Name: {repo["name"]}')
                file.write(f'Url: {repo["html_url"]}')
                file.write(f'Description: {repo["description"]}')
                file.write(f'Created_at: {repo["created_at"]}')
                file.write(f'Updated_at: {repo["updated_at"]}')
                file.write("-" * 5)

            file.write("---------------------------------")

    def print_results(self):
        rate_limit_info = self.check_rate_limit()
        repos = self.get_github_repositories()

        print(f"Results for {self.today}:\n")
        print("---------------------------------")
        print("Rate Limit Status:")
        print(f'- Limit: {rate_limit_info["resources"]["core"]["limit"]}')
        print(f'- Used: {rate_limit_info["resources"]["core"]["used"]}')
        print(f'- Remaining: {rate_limit_info["resources"]["core"]["remaining"]}')
        print(f'- Reset: {rate_limit_info["resources"]["core"]["reset"]}')
        print("---------------------------------")

        print("")

        print("---------------------------------")
        print("Repositories:\n")
        for repo in repos:
            print(f'Name: {repo["name"]}')
            print(f'Url: {repo["html_url"]}')
            print(f'Description: {repo["description"]}')
            print(f'Created_at: {repo["created_at"]}')
            print(f'Updated_at: {repo["updated_at"]}')
            print("-" * 5)

        print("---------------------------------")
