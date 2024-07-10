from typing import Any, Dict, List

import requests


class GitLabRepos:
    def __init__(self, token: str) -> None:
        self.token = token

    def check_rate_limit(self) -> Dict[str, Any]:
        """
        Check the GitLab API rate limit.
        """
        headers: Dict[str, Any] = {"Authorization": f"Bearer {self.token}"}
        url: str = "https://gitlab.com/api/v4/rate_limit"
        response = requests.get(url, headers=headers, timeout=10)
        rate_limit_info = response.json()
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
