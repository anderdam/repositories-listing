import datetime
from typing import Any, Dict, List, Union


class SaveRepos:
    def __init__(
        self,
        limit: Dict[str, Dict[str, Union[Dict[str, int], int]]],
        repos: List[Dict[str, Any]],
        name: str,
    ) -> None:
        self.limit = limit
        self.repos = repos
        self.name = name

    def save_repositories(self) -> None:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        rate_limit_info: str = str(self.limit)
        repositories: List[Dict[str, Any]] = self.repos
        with open(self.name, "w") as file:
            file.write(f"Results for {today}:\n")
            file.write("---\n")
            file.write("Rate Limit Status:\n")
            file.write(rate_limit_info)
            file.write("\n---")
            file.write("")
            file.write("Repositories:\n")
            for repository in repositories:
                file.write(f"{repository['name']}\n")
                file.write(f"{repository['html_url']}\n")
                file.write(f"{repository['description']}\n")
                file.write(f"{repository['created_at']}\n")
                file.write("\n")
                file.write("-" * 50)
