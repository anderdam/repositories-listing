import datetime
from typing import Any, Dict, List

import requests


class GitLabRepos:
    LINE_SEP = "---------------------------------\n"

    def __init__(self, token: str) -> None:
        """
        :type token: object
        """

        self.token = token
        self.today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def check_rate_limit(self) -> Dict[str, Any]:
        """
        Check the GitLab API rate limit by making a request and examining the headers.
        """

        headers = {"Authorization": f"Bearer {self.token}"}
        # Using the user endpoint as an example; adjust as needed.
        url = "https://gitlab.com/api/v4/user"
        response = requests.get(url, headers=headers, timeout=10)

        rate_limit_info = {
            "RateLimit-Limit": response.headers.get("RateLimit-Limit"),
            "RateLimit-Observed": response.headers.get("RateLimit-Observed"),
            "RateLimit-Remaining": response.headers.get("RateLimit-Remaining"),
            "RateLimit-Reset": response.headers.get("RateLimit-Reset"),
        }
        return rate_limit_info

    def get_gitlab_repositories(self) -> List[Dict[str, Any]]:
        repositories: List[Dict[str, Any]] = []
        page = 1
        username = "anderdam"
        while True:
            url = f"https://gitlab.com/api/v4/users/{username}/projects?page={page}"
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(url, headers=headers, timeout=10)
            page_repositories = response.json()
            if not page_repositories:
                break
            repositories.extend(page_repositories)
            if "next" not in response.links:
                break
            page += 1
        return repositories

    def save_repositories(self, name) -> None:
        rate_limit_info = self.check_rate_limit()
        repos = self.get_gitlab_repositories()

        with open(name, "w") as file:
            file.write(f"Results for {self.today}:\n")
            file.write(self.LINE_SEP)
            file.write("Rate Limit Status:\n")
            file.write(f'- Limit: {rate_limit_info["RateLimit-Limit"]}\n')
            file.write(f'- Observed: {rate_limit_info["RateLimit-Observed"]}\n')
            file.write(f'- Remaining: {rate_limit_info["RateLimit-Remaining"]}\n')
            file.write(f'- Reset: {rate_limit_info["RateLimit-Reset"]}\n')
            file.write(self.LINE_SEP)

            file.write("")

            file.write(self.LINE_SEP)
            file.write("Repositories:\n")
            for repo in repos:
                file.write(f'Name: {repo["name"]}\n')
                file.write(f'Url: {repo["web_url"]}\n')
                file.write(f'Description: {repo["description"]}\n')
                file.write(f'Created_at: {repo["created_at"]}\n')
                file.write(f'Updated_at: {repo["updated_at"]}\n')
                file.write("-" * 5)

            file.write(self.LINE_SEP)

    def print_results(self):
        rate_limit_info = self.check_rate_limit()
        repos = self.get_gitlab_repositories()

        print(f"Results for {self.today}:\n")
        print("---------------------------------")
        print("Rate Limit Status:")
        print(f'- Limit: {rate_limit_info["RateLimit-Limit"]}')
        print(f'- Observed: {rate_limit_info["RateLimit-Observed"]}')
        print(f'- Remaining: {rate_limit_info["RateLimit-Remaining"]}')
        print(f'- Reset: {rate_limit_info["RateLimit-Reset"]}')
        print("---------------------------------")

        print("")

        print("---------------------------------")
        print("Repositories:\n")
        for repo in repos:
            print(f'Name: {repo["name"]}')
            print(f'Url: {repo["web_url"]}')
            print(f'Description: {repo["description"]}')
            print(f'Created_at: {repo["created_at"]}')
            print(f'Updated_at: {repo["updated_at"]}')
            print("-" * 5)

        print("---------------------------------")
