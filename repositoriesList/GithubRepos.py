from typing import Any, Dict, List

import requests


class GithubRepos:
    def __init__(self, token: str) -> None:
        self.token = token

    def check_rate_limit(self) -> Dict[str, Any]:
        """
        Check the GitHub API rate limit.
        """
        headers = {"Authorization": f"token {self.token}"}
        url = "https://api.github.com/rate_limit"
        response = requests.get(url, headers=headers, timeout=10)
        rate_limit_info = response.json()
        return rate_limit_info

    def get_github_repositories(self) -> List[Dict[str, Any]]:
        repositories: List[Dict[str, Any]] = []
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
